goto :SKIP_COMMENT
幫助快速啟動腳本
請手動檢查 python依賴有沒有安裝好
:SKIP_COMMENT

@echo off
chcp 65001 > nul

echo.
echo 準備開始轉換........
echo.
python convert_webp.py

pause
