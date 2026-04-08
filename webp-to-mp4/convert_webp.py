import os
import functools
import subprocess
from concurrent.futures import ThreadPoolExecutor, as_completed
from threading import Lock
from PIL import Image  

# 裝飾器
def handle_exceptions(func):
    @functools.wraps(func)
    def wrapper(self, *args, **kwargs):
        try:
            return func(self, *args, **kwargs)
        
        except Exception as e:
            self.safe_print(f" [Error] 在執行 {func.__name__} 時發生錯誤: {e}")
            return False
    return wrapper

class WebptoMp4():
    def __init__(self):
        self.success_count = 0
        self.fail_count = 0
        self.print_lock = Lock()
        self.max_workers = 10  # [!] Thread數參數，可以慢慢往上加，但太多電腦會卡死藍屏

    def safe_print(self, *args, **kwargs):
        with self.print_lock:
            print(*args, **kwargs)

    def run(self):
        print("=" * 60)
        print("    腳本啟動")
        print("=" * 60)
        
        webp_files = [f for f in os.listdir('.') if f.lower().endswith('.webp')]
        if not webp_files:
            print("[!] 沒有找到 webp 檔案！！")
            return
        
        print(f"統計共有 {len(webp_files)} 個待轉檔檔案")


        with ThreadPoolExecutor(max_workers=self.max_workers) as executor:

            futures = {
                executor.submit(self._convert_to_webp, webp_file, i, len(webp_files)): webp_file
                for i, webp_file in enumerate(webp_files, 1)
            }
        
            for future in as_completed(futures):
                if future.result():
                    self.success_count += 1 
                else:
                    self.fail_count += 1

        print("-" * 60)
        print(f"任務結束 - 成功: {self.success_count}, 失敗: {self.fail_count}")

    @handle_exceptions
    def _convert_to_webp(self, webp_file, index, total): 
        self.safe_print(f"[{index}/{total}] Processing: {webp_file}")

        #開thread ，不能放 __init__
        frames = []
        durations = []

        img = Image.open(webp_file) 

        #取參數與轉換RGB圖層(就一般看到的圖層)
        try:
            while True:

                frames.append(img.copy().convert('RGB'))
                durations.append(img.info.get('duration', 100))
                img.seek(img.tell() + 1)
        except EOFError:
            pass

        if len(frames) == 0:
            self.safe_print(f"  讀不到數據 -> {webp_file}")
            return False
        
        gif_path = webp_file.rsplit('.', 1)[0] + f'_temp_{index}.gif' # 加 index 防止線程檔名衝突
        
        #Pillowd控制image save
        frames[0].save(
            gif_path,
            save_all=True,
            append_images=frames[1:],   # frames[0].save本來就存一個frame了，要從第second開始存
            duration=durations,
            loop=0
        )

        mp4_path = webp_file.rsplit('.', 1)[0] + '.mp4'
        
        #外部調用的參數配置表
        result = subprocess.run([
            'ffmpeg', '-y', '-loglevel', 'error',
            '-i', gif_path,
            '-c:v', 'h264_nvenc',           # N卡配置:h264_nvenc;無N卡改 libx264
            '-preset', 'p4',             # NVENC 的 preset 不同，p1最快 p7最慢最好
            '-cq', '23',                #畫質控制 0最好:51最差:23 // 非n卡 -cq 改 -crf
            '-pix_fmt', 'yuv420p',
            '-movflags', '+faststart',   #網路串流 header要放在頭，雖然可能沒用到還是依通用串流通用標準
            mp4_path
        ], capture_output=True)
        
        if os.path.exists(gif_path):
            os.remove(gif_path)
        
        if result.returncode == 0:
            self.safe_print(f" [v]下載完成: {mp4_path}")
            return True
        else:
            self.safe_print(f" [x]下載失敗: {webp_file} - {result.stderr.decode()}")
            return False

if __name__ == "__main__":
    app = WebptoMp4()
    app.run()

'''
webp metadata in following...
img.info = {
    'duration':  100,      # 該幀顯示時間（毫秒）
    'loop':      0,        # 循環次數，0 = 無限
    'background': (0,0,0), # 背景色
    'timestamp': 1000,     # 該幀的時間戳
}

'''
