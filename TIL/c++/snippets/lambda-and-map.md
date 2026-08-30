###  std::map 綁定 Lambda 表達式

* 場景：想要用數字編號對應去呼叫不同的成員函式，不想寫 switch-case 或 if-else。

* 說明：把 std::function 裝進 std::map 裡面，並用 Lambda 表達式 ([this]) 捕捉物件指標來呼叫自己的成員函式。



```
// 假設 menuMap 的型態類似 std::map<int, std::function<void()>>

// [this]：把目前的物件指標捕捉進去，這樣才能呼叫類別內部的成員函式
menuMap[1] = [this]() { this->handleBindForegroundWindow(); };
menuMap[2] = [this]() { this->handleFindTargetWindow(); };

// 呼叫方式（例如使用者輸入代號時）：
// if (menuMap.find(input) != menuMap.end()) { menuMap[input](); }
```