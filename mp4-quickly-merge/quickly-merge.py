from pathlib import Path
import  subprocess
DIR_FOLDER_PATH = Path(__file__).parent.resolve()
FOLDER_NAME = Path(DIR_FOLDER_PATH).name

class QuicklyMerge:
    
    def __init__(self):
        self.mp4_files_count = None 

        pass

    def _ensure_mp4_filrs(self):

        self.mp4_files = sorted([f for f in Path(DIR_FOLDER_PATH).iterdir() if f.suffix.lower() == ".mp4"]) # 這邊是稱名稱升序排序

        self.mp4_files_count = len(self.mp4_files)
        if not self.mp4_files_count:
            print("[!] 沒有找到 mp4 檔案")
            return
        
    def run(self):
        self._ensure_mp4_filrs()


        #創建 路徑清單
        list_path = str(DIR_FOLDER_PATH / "list_path.txt")
        with open(list_path, 'w', encoding='utf-8') as f:
            for mp4 in self.mp4_files:
                f.write(f"file '{mp4}'\n")

        try:
            output_name = str(DIR_FOLDER_PATH / f"{FOLDER_NAME}.mp4")

            result = subprocess.run([
            'ffmpeg', '-y', '-loglevel', 'error',
            # --- 關鍵：在讀取輸入前重新產生時間戳記 ---
            '-fflags', '+genpts', 
            '-f', 'concat',
            '-safe', '0',
            '-i', list_path,
            
            # --- 核心：快速拼貼 (不轉碼) ---
            '-c', 'copy', 
            
            # --- 避免短影片時間軸崩潰的保險 ---
            '-avoid_negative_ts', 'make_zero', 
            
            str(output_name)
            ], capture_output=True)

            if result.returncode == 0:
                print(f"[v] 合併完成檔案: {FOLDER_NAME}.mp4")
            else:
                print(f"[!] 合併失敗 - {result.stderr.decode()}")


        finally:
            if Path(list_path).exists():
                Path(list_path).unlink()

if __name__ == "__main__":
    print (DIR_FOLDER_PATH)
    run = QuicklyMerge()


    run.run()





"""
快速合成模板 :快速
[
    'ffmpeg', '-y', '-loglevel', 'error',
    # --- 關鍵：在讀取輸入前重新產生時間戳記 ---
    '-fflags', '+genpts', 
    '-f', 'concat',
    '-safe', '0',
    '-i', list_path,
    
    # --- 核心：快速拼貼 (不轉碼) ---
    '-c', 'copy', 
    
    # --- 避免短影片時間軸崩潰的保險 ---
    '-avoid_negative_ts', 'make_zero', 
    
    str(output_name)
]

"""
"""
CPU+編碼 : 比較慢
            [
            'ffmpeg', '-y', '-loglevel', 'error',
            '-fflags', '+genpts',  #時間戳記再生器
            '-f', 'concat',
            '-safe', '0',
            '-i', list_path,
            #----強制固定幀率
            '-r', '30',              # 強制輸出為每秒 30 格 (最穩定的標準)
            '-vsync', 'cfr',         # 強制使用 Constant Frame Rate (固定幀率模式)
            # --- CPU 編碼核心參數 ---     # list的地址
            '-map', '0:v',          # 強制選擇影片流
            '-map', '0:a?',         # 嘗試選擇音訊流，「?」代表「如果有的話就用，沒有就算了」   
            '-c:v', 'libx264',      # 指定使用 CPU 進行 H.264 編碼
            '-preset', 'medium',    # CPU 耗時與畫質的平衡 (想快一點改 veryfast)
            '-crf', '23',           # 畫質係數，23 是平衡點，越小畫質越好
            '-c:a', 'aac',          # 音訊轉成標準 AAC
            '-b:a', '128k',         # 統一音訊碼率
            '-pix_fmt', 'yuv420p',  # 提高設備相容性
            str(output_name)
            ]
"""