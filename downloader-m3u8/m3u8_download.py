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
    'Referer': 'https://google.com',
    'Origin': 'https://google.com',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 15; Pixel 9) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/150.0.0.0 Mobile Safari/537.36',
    # 'Cookie': 'session_id=xxxxx',  # Cookie拓展
}

#   ===== 依賴安裝地址 ========
M3U8D_DWONLOADER_URL = "https://github.com/nilaoda/N_m3u8DL-RE/releases/download/v0.5.1-beta/N_m3u8DL-RE_v0.5.1-beta_win-x64_20251029.zip"

# === 下載器參數 ===

DOWNLOAD_CONFIG = {
    "thread_count": "16",
    "auto_select": True,  
    "del_after_done": True,
}
class DownLoader:
    def __init__(self):
        pass

    def _check_dependencies(self):
        '''檢查是否有必要依賴 N_m3u8DL-RE

        若檢查發現沒依賴，則自動安裝指定 N_m3u8DL 版本

        Returns: True or False  
        '''

        # 路徑&檔案檢查
        if not DOWNLOADER_PATH.exists():
            DOWNLOADER_FOLDER.mkdir(exist_ok=True)

        # 如果執行檔已經存在，直接返回
        if DOWNLOADER_PATH.exists():
            return True


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
            return False
            
    def _download_m3u8(self,m3u8_url,file_name="output_vid"):
        """組裝 N_m3u8DL-RE 命令列參數並執行 subprocess 下載。

        Args:
            m3u8_url: 目標影片的 m3u8 串流網址。
            file_name: 輸出檔案的名稱（不須帶副檔名）。
        """
        
        command = [
            str(DOWNLOADER_PATH),
            m3u8_url,
            '--save-dir', str(BASE_DIR),
            '--save-name', file_name,
        ]

        # 動態加載設定
        if DOWNLOAD_CONFIG["auto_select"]:
            command.append("--auto-select")
        if DOWNLOAD_CONFIG["del_after_done"]:
            command.append("--del-after-done")

        # 執行外部命令
        subprocess.run(command)

    def run(self,url,file_name="output_vid"):
        '''封裝內部函式

        Args:
            m3u8_url: 目標影片的 m3u8 串流網址。
            file_name: 輸出檔案的名稱（不須帶副檔名）。
        
        '''
        if self._check_dependencies():
            self._download_m3u8(url,file_name)
            return


if __name__ == '__main__':
    dl = DownLoader()
    url = input("輸入 m3u8 URL: ")
    file_name = input("輸出檔案名稱: ").strip() or "output_video"
    dl.run(url,file_name)