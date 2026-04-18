### html 與 javascript 的串聯
- 說明:測時時，可以直接把js的scipt寫在 htlm的</body>之前，但考量到擴充性與耦合問題，還是要解耦比較建議。<br>
- 作法:在底部添加兩行路徑引用
- 目錄結構 (Convention):
Flask 預設會自動尋找以下名稱的資料夾，建議遵循此規範，應該也是網頁開發社群的約定習慣
  * `template` 資料夾:render_template() 會來這裡找 HTML
  * `static` 資料夾:js放在外部的話，要加{{ url_for('static', filename='index.js') }}，來指定位置，如下方代碼
 
```
<script src="index.js"></script>
<script src="{{ url_for('static', filename='index.js') }}"></script>
</body>
</html>
```


### Flask 與 Blueprint 的串接
* 根目錄的 main.py: 作為入口，啟動實例
* 根目錄 routes 資料夾:定義 Blueprint物件 ， 一個 blueprint 下可以有很多route ， 專案越大以後，可以以功能來做拆分。


### 一些flask的內建工具與核心零件

* 核心零件
  * Werkzeug：路由、WSGI 網路協議的「心臟」。

  * Jinja2：把 Python 變數塞進 HTML 的「美編師」。

  * Itsdangerous：負責加密與 Session 安全的「保全」。

  * Click：讓你能執行 flask run 指令的「儀表板」。

  * MarkupSafe：防止網頁被惡意代碼攻擊（XSS）的「過濾網」。
  
* 專案的「骨肉分離」架構  PS.這裡比較繞，因為要在模組間串聯
  * Flask 實務上強迫我們把檔案分開，這就是所謂的「解耦」：

  * App.py (主機)：負責插電啟動，註冊 Blueprint 模組。

  * routes/ (導遊)：負責處理網址，用 render_template 開門，或用 jsonify 丟資料。

  * templates/ (骨架)：放 HTML，負責網頁長相。

  * static/ (裝潢)：放 JS/CSS。在 HTML 裡必須用 url_for 才能正確抓到它們。

* 核心功能組件
這 6 個內建 API 就能搞定 80% 的工作：

  * Flask / Blueprint：組織工具。把大專案拆成小模組，像插頭一樣對接。

  * render_template：渲染工具。把 Python 的指令變成瀏覽器看得懂的網頁。

  * url_for：路徑工具。這是在 HTML 裡找 static 檔案的「導航」。

  * request：接收工具。看使用者傳了什麼資料過來。

  * jsonify：傳送工具。把資料打包成 JSON，專門給 JS 的 fetch 吃。
