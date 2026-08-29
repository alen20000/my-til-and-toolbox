## 基本指令
* `find_package` : 找外部套件(第三方套件)
* `target_include_directories` : 指定標頭檔（.h / .hpp）路徑
* `target_link_libraries` :　連結對應的動態庫
`add_executable` : 把原始碼編譯為執行檔

## 內建變數

* `${CMAKE_CURRENT_SOURCE_DIR}` : 此 CMakeLists.txt 檔案目前所在的資料夾絕對路徑

# Note

* 要「先找工具、建立目標」才能「對目標做設定」