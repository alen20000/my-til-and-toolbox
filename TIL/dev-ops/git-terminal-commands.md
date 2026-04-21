## 身分環境設定


### Check now setting
```git config --list``` - 顯示本機的全部git設定

```git config user.email``` - 檢視本機的git mail setting

### 基礎設定
```git config --global user.email "xxx@mail.com"```
-設定要配合github上帳號的mail，才會收到綠色框框的打卡紀錄

```git config --global user.name "alen20000"```
-設定本機的git name

補充:訊息去github看自己的最準。
點擊網頁右上角你的頭像。

點選 Settings（設定）。

在左側選單找到 Emails。

右邊畫面看到 Primary email address，那個就是自己的信箱。

以下是重設心得:最近電腦送修 用備用電腦寫repo 遇到git權限問題
現在git很聰明了，很方便。
```
1. 先在瀏覽器登入 github

2. 設定好上方兩個資訊

3. clone一個repo 在Push

4. push repo，會卡住然後會跳一個視窗

5. 點擊「Sign in with your browser」，開始在瀏覽器授權，顯示成功後，push自動上去
```

## 查詢log
```git log``` - 查看提交的commit record
```git log -n 5`` - 這樣可以查看近五筆紀錄
```git remote -v``` - 檢查專案與哪個github repo綁定


## Branch 指令
```git branch``` - 查看該專案目前哪個branch
``` git checkout -b <新分支名> ``` - 新建 branch


## 糾正指令
```git rm --cached <檔案名稱>``` - 有時候，檔案push上去，但後來才加到ignore，這時檔案還會在git上，要用這指令刪除本機的git快取，在push一次，git上的repo的該檔才會消失。

```git reset``` - 應用在，不小心 git add  ，但是還沒有 commit 時
```git reset HEAD~1``` -接續上行，若不小心commit了，就用這指令整個退回

```git commit --amend -m "新的 commit 訊息"``` - 用於修正最後一次 commit，他會直接覆蓋最後一次commit


## 還原指令
git還原是以每次 commit 為版本分點，範圍是整個專案資料夾，意思是，就算你某次commit 一個模組，但回原會作用在當時你分點的所有檔案。

1 - 短暫還原:確認一下之前的代碼怎麼寫，看完還要回到現在

指令：```git checkout <版本號>```  ps.版本號用log指令查

特點：這不會刪除任何東西。你想回來時，只需輸入 git checkout main 即可。


2 - 退回某版本:新改動不會變，但你寫好的代碼檔案不會消失，它們會變成「未提交」的狀態。感覺是拿來修正紀錄，保持紀錄乾淨。

```git reset --soft <版本號>``` - 指令原樣
```git reset --soft HEAD~1``` - 回到上一版本

3 - 整個刪除:返回點到目前的點的commit紀錄全刪除，找不回來。
```git reset --hard <版本號>``` - 指令原樣
```git reset --hard HEAD~1``` - 回到上一版本