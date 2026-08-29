## 安裝
* I: 進入官方網站 `https://my.qt.io/download`，登入帳號後下載`Open Souce`
* II: 下載後點擊緒開始安裝流程，我的C+是VS 2026 帶的，在安裝中選自定義安裝，要安裝 `MSVC 2022` 這版本，VS向下兼容很好不用擔心，不需要整個把肥大的QT都安裝
* III:打開VS，從上方選單`延伸模組(X)`->`管理延伸模組(M)`->搜索並安裝`Qt Visual Studio Tools`
<br>這插件是輔助VS能閱讀Qt的標頭檔

# 標頭、CMAKE設定

* 標頭宣告 `Q_OBJECT` 巨集，責向Qt的預處理氣(MOC) 預告這個類別需要擴充 Qt 的元物件功能。


* CMAKE中要在`add_executable`加入以下三行
* 還有，因為標頭檔有宣告`Q_OBJECT`巨集，所以要手動放進`add_executable` ，否則MOC掃不到路徑，就會報錯
```
    ${window_sources}
    ${controller_sources}
    ${ui_sources}
```