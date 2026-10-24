@echo off
chcp 65001 > nul
title Tool Kịch Bản AI YouTube (50-60 Prompt)

echo ======================================================================
echo          TOOL KỊCH BẢN VIDEO AI YOUTUBE (50-60 PROMPT)
echo               Tuân thủ quy chuẩn theo Rule.txt
echo ======================================================================
echo.

cd /d "%~dp0"

echo [*] Kiểm tra Python...
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [ERROR] Không tìm thấy Python trên máy tính! Vui lòng cài đặt Python 3.10+
    pause
    exit /b 1
)

echo [*] Đang khởi động máy chủ Web UI...
echo [*] Trình duyệt sẽ tự động mở tại: http://127.0.0.1:8000
echo.
python server.py

pause
