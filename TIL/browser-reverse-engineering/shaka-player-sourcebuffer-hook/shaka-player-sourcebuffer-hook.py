import base64
import glob
import os
import subprocess
from concurrent.futures import ThreadPoolExecutor
import time
from playwright.sync_api import sync_playwright

'''
問題：
目標影片採用 Shaka Player，URL 外殼偽裝成 .png，且串流數據被包裝成像素漸層圖層，無法直接從網路層攔截並進行二進位合併。

解決方法：
放棄網路層攔截（request 事件無效），改採 瀏覽器底層程式碼注入（Code Injection）：
透過 JS Hook 攔截 SourceBuffer.prototype.appendBuffer，直接在記憶體中擷取解密後的真實影音串流。
'''

# ==================== 設定區域 ====================
TEMP_DIR = "temp_media_source"
OUTPUT_FILENAME = "final_video.mp4"
# ==================================================


def main():
    target_url = input("👉 請輸入要下載的影片網址:\n> ").strip()
    if not target_url:
        print("[錯誤] 未輸入有效的網址，程式結束。")
        return

    if not os.path.exists(TEMP_DIR):
        os.makedirs(TEMP_DIR)
    else:
        # 清空舊的暫存片段
        for f in glob.glob(os.path.join(TEMP_DIR, "*.bin")):
            os.remove(f)

    chunk_counter = [0]

    print("[*] 正在啟動瀏覽器並注入底層攔截鉤子 (Hook)...")
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        # 定義接收來自 JavaScript 傳回的二進位資料函式
        def save_chunk(b64_data):
            try:
                raw_bytes = base64.b64decode(b64_data)
                chunk_counter[0] += 1
                file_path = os.path.join(TEMP_DIR, f"chunk_{chunk_counter[0]:05d}.bin")
                with open(file_path, "wb") as f:
                    f.write(raw_bytes)
                print(
                    f"[底層記憶體攔截] 成功擷取第 {chunk_counter[0]} 個解密片段"
                    f" ({len(raw_bytes)} bytes)"
                )
            except Exception as e:
                print(f"[錯誤] 儲存記憶體片段失敗: {e}")

        # 將 Python 函式暴露給前端網頁呼叫
        page.expose_binding("saveMediaChunk", lambda source, data: save_chunk(data))

        # 在網頁載入前，注入 JS 鉤子去攔截播放器的 appendBuffer
        hook_script = """
            (function() {
                const originalAppendBuffer = SourceBuffer.prototype.appendBuffer;
                SourceBuffer.prototype.appendBuffer = function(value) {
                    try {
                        let blob = new Blob([value]);
                        let reader = new FileReader();
                        reader.onload = function() {
                            let base64data = reader.result.split(',')[1];
                            window.saveMediaChunk(base64data);
                        };
                        reader.readAsDataURL(blob);
                    } catch (err) {
                        console.log("Hook appendBuffer error", err);
                    }
                    return originalAppendBuffer.apply(this, arguments);
                };

                // 手動加入的加速邏輯 video.playbackRate 調節播放速率
                setInterval(() => {
                    const video = document.querySelector('video');
                    if (video) {
                        if (video.playbackRate !== 4.0) {
                            video.playbackRate = 4.0;
                        }
                        if (!video.muted) {
                            video.muted = true;
                        }
                    }
                }, 500);

                console.log(">>> SourceBuffer 底層 Hook 與 4x 加速已安裝！ <<<");
            })();
            """
        page.add_init_script(hook_script)

        print(f"[*] 正在前往目標頁面: {target_url}")
        page.goto(target_url)

        print("\n============================================================")
        print("[*] 進入攔截階段：")
        print("============================================================\n")

        # 互動控制
        input("當擷取足夠或影片播放完畢後，在此按下 Enter 鍵開始封裝...")

        try:
            browser.close()
        except:
            pass

    # 合併與封裝階段
    print("[*] 正在合併底層擷取到的所有二進位片段...")
    chunk_files = sorted(glob.glob(os.path.join(TEMP_DIR, "chunk_*.bin")))
    if not chunk_files:
        print("[錯誤] 沒有攔截到任何二進位片段！")
        return

    ts_output = "temp_media_merged.ts"
    with open(ts_output, "wb") as outfile:
        for f_path in chunk_files:
            with open(f_path, "rb") as infile:
                outfile.write(infile.read())

    print(f"[*] 合併完成！正在透過 FFmpeg 封裝成最終影片: {OUTPUT_FILENAME}")
    cmd = ["ffmpeg", "-y", "-i", ts_output, "-c", "copy", OUTPUT_FILENAME]
    result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    if result.returncode == 0:
        print(f"[合併完成] 影片已儲存為：{OUTPUT_FILENAME}")
    else:
        print(
            "[警告] FFmpeg 轉檔失敗，但你可以手動檢查 temp_media_merged.ts 檔案。"
        )

    # 清理暫存檔
    if os.path.exists(ts_output):
        os.remove(ts_output)


if __name__ == "__main__":
    main()