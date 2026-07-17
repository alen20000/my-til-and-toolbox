from importlib.resources import path
from pathlib import Path
from collections import defaultdict
'''
放根目錄，抓所有MD名單
'''

ROOT_FOLDER = Path.cwd()

#過濾清單，這些檔案或資料夾不會被列入
IGNORE_LIST = {'.gitignore', '__pycache__', '.git','README.md'}

class FolderOperation:
# 資料夾操作，抓取所有md檔案路徑

    def __init__(self):
        #路徑定義
        self.root = ROOT_FOLDER
        self.output_file = ROOT_FOLDER / "output.txt"
        self.output_file.parent.mkdir(parents=True, exist_ok=True)
        
        #建立存放的字典
        self.organized_data = defaultdict(list)

    def run(self):
        self._get_categories()

    def _get_categories(self):
        #遍歷資料夾        


        for path in sorted(self.root.rglob('*.md')):

            #1.判斷是否要忽略
            if self._should_ignore(path):
                continue
            
            #1-1.取得該路檔案之目錄
            category = path.parent.name
            #1-2.取得相對路徑
            rel_path = path.relative_to(self.root)
            #1-3.將路徑加入對應的類別中，因為用defaultdict(list)建立，所以不用頭痛key是否存在或重複
            self.organized_data[category].append(f"- [{path.stem}]({rel_path.as_posix()})")

        self._write_to_file()
        
    def _should_ignore(self, path):
        # 檢查判斷，檔案或資料夾名稱在忽略清單中，或是以 . 開頭的隱藏檔案
        for part in path.parts:
            if part in IGNORE_LIST:
                return True

        if path.name.startswith('.'):
            return True

        return False
    
    def  _write_to_file(self):
        #將整理好的字典資料輸出為文本
            output_file = ROOT_FOLDER / "output.txt"
            with open(output_file, "w", encoding="utf-8") as f:
                for category in sorted(self.organized_data.keys()):
                    f.write(f"### {category}\n")
                    f.write("\n".join(self.organized_data[category]))
                    f.write("\n\n")


if __name__ == "__main__":
    folder_interate =FolderOperation().run()

