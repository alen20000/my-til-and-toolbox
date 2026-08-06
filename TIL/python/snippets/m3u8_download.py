from pathlib import Path
import subprocess
'''
簡易 m3u8下載器，使用N_m3u8DL-RE.exe
路徑要調整一下，

'''
#   =====路徑設定=====
# 根目錄絕對路徑
BASE_DIR = Path(__file__).parent.resolve()
# N_m3u8DL-RE.exe 路徑
DOWNLOADER_PATH = BASE_DIR / "bin" /  "N_m3u8DL-RE.exe" 
#   ===== Header設定(依照需求修改)=====
CUSTOM_HEADERS = {
    # 'Referer': 'https://missav.ai/',
    'Origin': 'https://porncvd.com',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 15; Pixel 9) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/150.0.0.0 Mobile Safari/537.36',
    # 'Cookie': 'session_id=xxxxx',  # 需要登入態時再打開
}
def download_m3u8(m3u8_url,output_path,headers=None):

    #N_m3u8DL-RE的命令行參數
    command = [
        str(DOWNLOADER_PATH),
        m3u8_url,  # 輸入 m3u8 URL
        '--save-dir', str(BASE_DIR),  # 指定下載目錄
        '--save-name', output_path,  # 指定輸出檔案名稱（不須帶副檔名）
        '--auto-select', #自動選擇畫質最高的影片流
        '--del-after-done' ,#下載合併
        '--thread-count', '16', #提高執行緒，嘗試抓更快，防止遺失造成失效，原本預設為8

    ]
    subprocess.run(command)
    if headers:
        # 如果有自訂 headers，將其轉換為命令行參數
        for key, value in headers.items():
            command.extend(['--header', f'{key}: {value}'])

if __name__ == '__main__':
    m3u8_url = input("目標 m3u8 URL: ")  # 替換為實際的 m3u8 URL
    output_path = input("輸出檔案名稱: ").strip() or "output_video"  # 替換為你想要的輸出檔案名稱
    download_m3u8(m3u8_url,output_path)
    input("按 Enter 結束...")
