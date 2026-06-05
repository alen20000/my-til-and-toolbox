from pathlib import Path
import subprocess
'''
簡易 m3u8下載器，使用N_m3u8DL-RE.exe
路徑要調整一下，

'''
# 目前執行檔所在目錄
BASE_DIR = Path(__file__).parent.resolve()
DOWNLOADER_PATH = BASE_DIR / "bin" /  "N_m3u8DL-RE.exe" 

def download_m3u8(m3u8_url):

    #N_m3u8DL-RE的命令行參數
    command = [
        str(DOWNLOADER_PATH),
        m3u8_url,  # 輸入 m3u8 URL
        '--save-dir', str(BASE_DIR),  # 指定下載目錄
        '--save-name', 'output_video',  # 指定輸出檔案名稱（不帶副檔名）
        '--auto-select',
        '--del-after-done'
    ]
    subprocess.run(command)
    

if __name__ == '__main__':
    m3u8_url = ''  # 替換為實際的 m3u8 URL
    output_path = 'output_video.mp4'  # 替換為你想要的輸出檔案名稱
    download_m3u8(m3u8_url)
