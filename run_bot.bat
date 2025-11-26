@echo off
REM Premium Referat Bot - Ishga Tushirish Skripti
REM Windows uchun

echo.
echo ========================================
echo   PREMIUM REFERAT BOT - ISHGA TUSHIRISH
echo ========================================
echo.

REM Python versiyasini tekshirish
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python o'rnatilmagan!
    echo https://python.org/downloads dan yuklab oling
    pause
    exit /b 1
)

echo [OK] Python topildi
echo.

REM .env faylini tekshirish
if not exist ".env" (
    echo ERROR: .env fayli topilmadi!
    echo SETUP.md faylini o'qing va .env faylini yarating
    pause
    exit /b 1
)

echo [OK] .env fayli topildi
echo.

REM Kutubxonalarni tekshirish
echo Kutubxonalarni tekshirish...
python -c "import telegram, openai, dotenv" 2>nul
if errorlevel 1 (
    echo [!] Kutubxonalar o'rnatilmagan
    echo Kutubxonalarni o'rnatish...
    pip install -r requirements.txt
    if errorlevel 1 (
        echo ERROR: Kutubxonalarni o'rnatib bo'lmadi!
        pause
        exit /b 1
    )
)

echo [OK] Kutubxonalar o'rnatilgan
echo.

REM Sozlamalarni tekshirish
echo Sozlamalarni tekshirish...
python test_setup.py
if errorlevel 1 (
    echo [!] Ba'zi muammolar bor
    echo SETUP.md faylini o'qing
    pause
    exit /b 1
)

echo.
echo ========================================
echo   HAMMASI TAYYOR! BOT ISHGA TUSHMOTADA...
echo ========================================
echo.

REM Bot'ni ishga tushirish
python bot_advanced.py

pause
