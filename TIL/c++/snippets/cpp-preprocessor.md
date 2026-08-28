
## Windows C++ 開發：標頭檔與巨集防護

必須寫在 `#include <windows.h>` 的「正上方」，否則無效！
```
#define WIN32_LEAN_AND_MEAN  
#define NOMINMAX            
#include <windows.h>
```
#### Note
* WIN32_LEAN_AND_MEAN : 排除不常用的 Windows 肥大標頭檔，加快編譯速度並避免衝突
* NOMINMAX 禁止 Windows 定義 min/max 巨集，防止卡到 C++ 標準庫的 

##  防止標頭檔重複包含

* 標頭檔添加以下一行
```
#pragma once
```
#### Note
* 幾乎是必用
* 這句是為了防止，標頭檔被重複引用
*