from pathlib import Path
import subprocess
'''
@Breif: 直接對 m3u8 連結進行下載

'''
#   =====路徑設定=====
# 根目錄絕對路徑
BASE_DIR = Path(__file__).parent.resolve()
# N_m3u8DL-RE.exe 路徑
DOWNLOADER_FOLDER = BASE_DIR / "bin"
DOWNLOADER_PATH = DOWNLOADER_FOLDER /  "N_m3u8DL-RE.exe" 
OUTPUT_PATH = BASE_DIR / "output"


#   ===== Header設定(依照需求修改)=====
CUSTOM_HEADERS = {
    # 'Referer': 'https://missav.ai/',
    'Origin': 'https://porncvd.com',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 15; Pixel 9) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/150.0.0.0 Mobile Safari/537.36',
    # 'Cookie': 'session_id=xxxxx',  # 需要登入態時再打開
}

#   ===== 依賴安裝地址 ========
M3U8D_DWONLOADER_URL = "https://github.com/nilaoda/N_m3u8DL-RE/releases/download/v0.5.1-beta/N_m3u8DL-RE_v0.5.1-beta_win-x64_20251029.zip"

class DownLoader:
    def __init__(self):
        self.m3u8_url = None

    def _check_dependencies(self):
        '''
        @Breif: 檢查是否有安裝 N_m3u8DL-RE，沒有則自動安裝
        '''

        # 路徑&檔案檢查
        if not DOWNLOADER_PATH.exists():
            DOWNLOADER_FOLDER.mkdir(exist_ok=True)

        if not DOWNLOADER_PATH.exists():
            print("缺失必要依賴，開始自動安裝...")

            import requests
            import zipfile
            import io

            try:
                res = requests.get(M3U8D_DWONLOADER_URL)
                # 若狀態不對，會跳到最近的excep，或直接報錯。主要是避免抓到空檔案然後還解壓縮
                res.raise_for_status()
                # 下載的檔案直接給記憶體，不給實體地址
                zip_data = io.BytesIO(res.content)
                # 解壓縮
                with zipfile.ZipFile(zip_data) as z:

                    exe_name = next((f for f in z.namelist() if f.endswith(".exe")), None)

                    if exe_name:
                        with open(DOWNLOADER_PATH, "wb") as f:
                            f.write(z.read(exe_name))

                        return True
                    else:
                        raise FileNotFoundError("壓縮檔內找不到執行檔 (.exe)")
                    
            except Exception as e:
                print(f"自動安裝失敗，請手動安裝:{e}")
                return
            
    def download_m3u8(self,m3u8_url):
        pass
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
    dl = DownLoader()
    dl._check_dependencies()