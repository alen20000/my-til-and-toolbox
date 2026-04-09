解決VSC每次打開專案，編譯器要手動設定的問題

VSC會優先專案目錄下的 `.vscode`查找`settings.json`



syn:python.defaultInterpreterPath - 指定解釋器位置 。 這步驟其實就是 `ctrl`+`shift`+`p`>> `select:python interpreter` 創建的

syn:python.terminal.activateEnvironment - 自動激活環境

5

```
{
    "python.defaultInterpreterPath": ".venv\\python.exe",
    "python.terminal.activateEnvironment": true
}
```


[!] 如果沒有啟動，可能在shell層要改一下安全性

```
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

params :

    RemoteSigned - 遠端簽署模式；本地腳本不需簽名，外部腳本需要

    -Scope CurrentUser - 僅限當前使用者