#!/usr/bin/env python3
# PREMIUM REFERAT BOT v3.0 - START GUIDE

"""
🎓 PREMIUM REFERAT BOT v3.0 - FOYDALANUVCHI QO'LLANMASI

YANGILIKLARI v3.0:
✅ To'lov tizimi
✅ Dinamik narxlar
✅ Admin tasdiqlash
✅ Premium referatlar
"""

import os

def show_welcome():
    print("""
╔════════════════════════════════════════════════════════════╗
║                                                            ║
║   🎓 PREMIUM REFERAT BOT v3.0                             ║
║   AI-Powered Essay Generator with Payment System          ║
║                                                            ║
║   Status: ✅ TO'LIQ TAYYOR                                ║
║   Version: 3.0 Premium                                    ║
║   Release: 2025-01-26                                     ║
║                                                            ║
╚════════════════════════════════════════════════════════════╝
    """)

def show_features():
    print("""
💎 XUSUSIYATLAR:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

💳 TO'LOV TIZIMI:
  • Dinamik narxlar (diapazon va ta'lim bo'yicha)
  • Admin kartasiga xavfsiz o'tkazish
  • Chek rasm validatsiyasi
  • Admin tasdiqlash/Rad etish

📄 BET DIAPAZONLARI:
  • 1-5 bet     → 10,000 UZS (asosiy)
  • 5-10 bet    → 20,000 UZS
  • 10-15 bet   → 30,000 UZS
  • 15-20 bet   → 40,000 UZS

🎓 TA'LIM DARAJASI:
  • 🎒 Maktab (8-11)    → x1.0
  • 🏫 Kollejj          → x1.3
  • 🎓 Universitet      → x1.7
  • 📚 Magistratura     → x2.2

📋 FORMAT VARIANTLARI:
  • 📝 Oddiy matn              → x1.0
  • 📋 Struktura bilan         → x1.1
  • ✍️  Chuqur tahlili        → x1.4

✨ REFERAT SIFATI:
  • Chuqur akademik mazmun
  • Konkret misollar va statistika
  • Olimlar fikri va dalillar
  • 100% original (plagiatdan voz kechilib)
  • Professional uslub
    """)

def show_setup():
    print("""
🚀 ISHGA TUSHIRISH BOSQICHLARI:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1️⃣  TELEGRAM BOT TOKEN OLISH
   • @BotFather'ga murojaat qiling
   • /newbot buyrug'ini kiriting
   • Bot nomini bering
   • Token'ni saqlang

2️⃣  ADMIN ID ANIQLASH
   • Telegram'da @userinfobot'dan ID'ni oling
   • Yoki Bot'ga xabar yuboring va ID'ni ko'ring

3️⃣  OPENAI API KEY OLISH
   • https://platform.openai.com ga boring
   • API Keys qismida yangi key yarating
   • Kredit kartangizni qo'shing

4️⃣  .ENV FAYLINI TO'LDIRISH
   • .env faylini oching
   • Barcha API kalitlarini kiriting:
     TELEGRAM_BOT_TOKEN=xxx
     TELEGRAM_ADMIN_ID=xxx
     OPENAI_API_KEY=xxx
     ADMIN_CARD_NUMBER=9860-XXXX-XXXX-XXXX
     ADMIN_CARD_HOLDER=Admin Nomi
     ADMIN_BANK=Humo Bank

5️⃣  BOT'NI ISHGA TUSHIRISH
   • Terminal'da: python bot_advanced.py
   • "Bot ishga tushdi!" xabar ko'ring
   • Telegram'da /start qiling

6️⃣  TEST QILISH
   • Referat yaratish
   • Tanlovlarni qilish
   • Narxni ko'rish
   • Admin kartasiga to'lov
   • Chek yuborish
   • Admin tasdiqlash
   • Referat qabuli
    """)

def show_pricing():
    print("""
💰 NARXLAR JADVALI:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

              | Oddiy | Struktura | Chuqur
              |-------|-----------|-------
Maktab 1-5    | 10K   |    11K    |  14K
Kollejj 1-5   | 13K   |  14.3K    |  18.2K
Universitet   | 17K   |  18.7K    |  23.8K
Magistratura  | 22K   |   24.2K   |  30.8K
              |-------|-----------|-------
Maktab 5-10   | 20K   |    22K    |  28K
Kollejj 5-10  | 26K   |  28.6K    |  36.4K
Universitet   | 34K   |  37.4K    |  47.6K
Magistratura  | 44K   |   48.4K   |  61.6K
              |-------|-----------|-------
Maktab 10-15  | 30K   |    33K    |  42K
Kollejj 10-15 | 39K   |  42.9K    |  54.6K
Universitet   | 51K   |  56.1K    |  71.4K
Magistratura  | 66K   |   72.6K   |  92.4K
              |-------|-----------|-------
Maktab 15-20  | 40K   |    44K    |  56K
Kollejj 15-20 | 52K   |  57.2K    |  72.8K
Universitet   | 68K   |  74.8K    |  95.2K
Magistratura  | 88K   |   96.8K   | 123.2K
    """)

def show_commands():
    print("""
📱 BOT KOMANDALAR:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

FOYDALANUVCHI KOMANDALAR:
  /start      - Yangi referat yaratish
  /help       - Yordam ko'rish
  /cancel     - Bekor qilish

ADMIN KOMANDALAR:
  Chek rasmiga reply:
    ✅ Tasdiqlash tombol
    ❌ Rad etish tombol

TUGMALAR:
  • Diapazon tanlash (1-5, 5-10, 10-15, 15-20)
  • Ta'lim darajasi tanlash
  • Format tanlash
  • Tasdiqlash/Bekor qilish
    """)

def show_troubleshooting():
    print("""
🔧 MUAMMOLAR VA YECHIMLAR:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

❌ "Bot ishga tushmadi"
   ✓ .env faylini tekshiring
   ✓ Token'larni qayta tekshiring
   ✓ Internet ulanishni tekshiring

❌ "API xatosi"
   ✓ OpenAI'da kredit qo'shing
   ✓ API key'ni qayta tekshiring
   ✓ Billing'ni o'rnatilgan tekshiring

❌ "Admin bildirishnoma keldi yo'q"
   ✓ Admin ID'ni tekshiring
   ✓ Bot adminga yuborish imkonini bering

❌ "Referat qisqa yoki juda uzun"
   ✓ Betlar sonini o'zgariting
   ✓ Format'ni o'zgariting
   ✓ Mavzuni aniqroq kiriting

❌ "To'lov rada etildi"
   ✓ Chekda summa ko'rinishini tekshiring
   ✓ Chekda vaqt ko'rinishini tekshiring
   ✓ Admin'ga murojaat qiling
    """)

def show_files():
    print("""
📂 MUHIM FAYLLAR:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

ASOSIY FAYLLAR:
  • bot_advanced.py         - Premium bot
  • payment_system.py       - To'lov tizimi
  • config.py               - Sozlamalar
  • requirements.txt        - Paketlar

DOKUMENTATSIYA:
  • PREMIUM_VERSION_README.md    - Batafsil yo'riqnoma
  • QUICK_GUIDE_UZ.md            - Tezkor qo'llanma
  • SETUP.md                     - O'rnatish
  • README_UZ.md                 - O'zbekcha README

KONFIGURATSIYA:
  • .env                    - API kalitlari
  • .env.example            - Namunasi
  • payments.json           - To'lov bazasi

TESTLAR:
  • simple_test.py          - Tez testlar
  • test_payment_system.py  - To'lov testlari
  • verify_setup.py         - Tekshirish
    """)

def show_next_steps():
    print("""
📋 KEYINGI BOSQICHLAR:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

ISHGA TUSHIRISH:
  1. SETUP.md'ni to'liq o'qing
  2. .env faylini to'ldiring
  3. python verify_setup.py bilan tekshiring
  4. python bot_advanced.py bilan ishga tushiring

FOYDALANISH:
  1. Telegram'da bot'ni topib oching
  2. /start buyrug'ini kiriting
  3. Tanlovlarni qilib referat yarating
  4. Narxni ko'rib tasdiqlang
  5. To'lovni qiling
  6. Premium referatni oling

KUZATISH:
  1. Payments.json'da to'lovlarni ko'ring
  2. Admin panelida tasdiqlang
  3. Statistika tekshiring

DEBUGGING:
  1. Loglarni terminal'da o'qing
  2. check_setup.py bilan tekshiring
  3. simple_test.py bilan testlab ko'ring
    """)

def main():
    show_welcome()
    show_features()
    show_setup()
    show_pricing()
    show_commands()
    show_troubleshooting()
    show_files()
    show_next_steps()
    
    print("""
╔════════════════════════════════════════════════════════════╗
║                                                            ║
║  🎉 BOT TAYYOR!                                           ║
║                                                            ║
║  Muvaffaqiyat tilaymiz!                                   ║
║                                                            ║
║  Support: SETUP.md va README'ni o'qing                    ║
║                                                            ║
╚════════════════════════════════════════════════════════════╝
    """)

if __name__ == '__main__':
    main()
