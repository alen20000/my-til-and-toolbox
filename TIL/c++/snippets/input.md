# C++ 輸入防呆與筆記

## 1. 處理 `std::cin` 輸入錯誤（無限迴圈防禦）
當使用者輸入非預期格式（如字母、中文）給 `int` 變數時，`cin` 會進入鎖死狀態（Fail State）。

### 解決方法：
```cpp
if (!(std::cin >> choice)) {
    std::cout << "輸入格式錯誤！\n";
    
    // 1. 解除故障鎖死狀態
    std::cin.clear();
    
    // 2. 清空緩衝區垃圾與換行符號（加上括號防止 Windows 巨集衝突）
    // max 還有個坑，就是會卡到微軟的巨集
    // 這時候 在標頭引用 加上`#define NOMINMAX`
    std::cin.ignore((std::numeric_limits<std::streamsize>::max)(), '\n');
    
    continue;
}
```
* Note: 記著，cin之類的操作，就貼上這兩行


## 控制台打印中文

* 問題：在 C++ 裡用 std::cout 或寬字元印中文時，畫面上直接一片空白，而且編譯器完全不報錯。

* 原因：Windows 預設的終端機編碼不是 UTF-8，且 C++ 的全域地區設定（locale）預設不支援中文寬字元。

* 方法*：在 main 函式最前面加上這兩行：
```
// 強制切換 Windows 主控台為 UTF-8 編碼
system("chcp 65001 > nul");

// 設定全域地區支援繁體中文 UTF-8
std::locale::global(std::locale("zh_TW.UTF-8"));
```
