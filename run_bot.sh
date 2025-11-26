#!/bin/bash
# Premium Referat Bot - Ishga Tushirish Skripti
# Linux/Mac uchun

echo ""
echo "========================================"
echo "  PREMIUM REFERAT BOT - ISHGA TUSHIRISH"
echo "========================================"
echo ""

# Python versiyasini tekshirish
if ! command -v python3 &> /dev/null; then
    echo "ERROR: Python o'rnatilmagan!"
    echo "https://python.org/downloads dan yuklab oling"
    exit 1
fi

echo "[OK] Python topildi"
echo ""

# .env faylini tekshirish
if [ ! -f ".env" ]; then
    echo "ERROR: .env fayli topilmadi!"
    echo "SETUP.md faylini o'qing va .env faylini yarating"
    exit 1
fi

echo "[OK] .env fayli topildi"
echo ""

# Kutubxonalarni tekshirish
echo "Kutubxonalarni tekshirish..."
python3 -c "import telegram, openai, dotenv" 2>/dev/null
if [ $? -ne 0 ]; then
    echo "[!] Kutubxonalar o'rnatilmagan"
    echo "Kutubxonalarni o'rnatish..."
    pip3 install -r requirements.txt
    if [ $? -ne 0 ]; then
        echo "ERROR: Kutubxonalarni o'rnatib bo'lmadi!"
        exit 1
    fi
fi

echo "[OK] Kutubxonalar o'rnatilgan"
echo ""

# Sozlamalarni tekshirish
echo "Sozlamalarni tekshirish..."
python3 test_setup.py
if [ $? -ne 0 ]; then
    echo "[!] Ba'zi muammolar bor"
    echo "SETUP.md faylini o'qing"
    exit 1
fi

echo ""
echo "========================================"
echo "  HAMMASI TAYYOR! BOT ISHGA TUSHMOTADA..."
echo "========================================"
echo ""

# Bot'ni ishga tushirish
python3 bot_advanced.py
