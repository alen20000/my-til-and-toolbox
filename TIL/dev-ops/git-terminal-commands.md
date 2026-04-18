## 身分環境設定


### check now setting
```git config --list``` - 顯示本機的全部git設定
```git config user.email``` - 檢視本機的git mail setting

### mail設定
```git config --global user.email "xxx@mail.com"```
-設定要配合github上帳號的mail，才會收到綠色框框的打卡紀錄


## 查詢log
```git log``` - 查看提交的commit record
```git log -n 5`` - 這樣可以查看近五筆紀錄
```git remote -v``` - 檢查專案與哪個github repo綁定


## Branch 指令
```git branch``` - 查看該專案目前哪個branch
``` git checkout -b <新分支名> ``` - 新建 branch