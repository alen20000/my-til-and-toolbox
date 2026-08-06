# Windows CMD Cheat Sheet

- **標籤**: `#cmd` `#windows` `#cli` `#cheat-sheet`

##  檔案與目錄操作 (Navigation & Files)
* **`dir`**: 列出當前目錄底下的檔案與資料夾
* **`cd <path>`**: 切換到指定的路徑
* **`cd ..`**: 回到上一層目錄
* **`mkdir <folder>`**: 建立新資料夾
* **`rmdir /s /q <folder>`**: 強制刪除資料夾及其所有內容（不跳出確認提示）
* **`del <file>`**: 刪除指定的檔案

##  實用檢視與工具 (Utilities)
### 快速清空螢幕
```cmd
cls
```
### 建立樹狀目錄
```
 tree D:\[xxx folder] /f

args:
- /f 顯示各資料夾中名稱
- /a: 使用 ASCII 字元（避免終端機編碼亂碼）
```