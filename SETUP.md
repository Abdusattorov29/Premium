# 🚀 Telegram Bot - Ishga Tushirish Yo'riqnomasi

## 📋 Zarur Narsalar

1. **Python 3.8+** - [Python.org](https://www.python.org/downloads/)
2. **Telegram Account** - [Telegram](https://telegram.org/)
3. **OpenAI Account** - [OpenAI Platform](https://platform.openai.com/)
4. **Telegram Bot Token** - @BotFather orqali
5. **OpenAI API Key** - OpenAI Platform orqali

---

## 1️⃣ BOT TOKEN OLISH (@BotFather)

### Qadam 1: @BotFather'ga murojaat qiling
- Telegram'da qidiruv qilib `@BotFather`ni toping
- `/start` buyrug'ini kiriting

### Qadam 2: Yangi bot yaratish
- `/newbot` buyrug'ini kiriting
- Bot nomini kiriting (masalan: "PremiumReferatBot")
- Username kiriting (masalan: "premium_referat_bot")
- Olingan **TOKEN**ni saqlang ❗

### Misoliy Token:
```
1234567890:ABCdefGHIjklmnoPQRstuvWXYZ-a1b2c3d4e5f
```

---

## 2️⃣ OPENAI API KEY OLISH

### Qadam 1: OpenAI'ga ro'yxatdan o'tish
- [platform.openai.com](https://platform.openai.com/) ga boring
- Email bilan ro'yxatdan o'ting
- Telefon orqali tekshiring

### Qadam 2: API Key yaratish
1. Chapdagi menyuda **"API keys"** ni toping
2. **"Create new secret key"** ni bosing
3. Olingan **KEY**ni saqlang ❗

### Qadam 3: Kredit qo'shish (Zaruri!)
- Billing qismiga boring
- Kredit kartangizni qo'shib, balans to'ldiring
- 5-20$ dan boshlash mumkin

---

## 4️⃣ ADMIN ID OLISH (To'lov Tizimi Uchun)

### Qadam 1: Admin Bot yaratish
1. @BotFather'da `/newbot` buyrug'ini kiriting
2. "AdminHelperBot" kabi nom bering
3. Olingan token'ni saqlang

### Qadam 2: Admin ID'ni aniqlash
Bot tokenini `/start` qismi bilan test qiling:
```python
# Python terminali'da:
from telegram import Bot
bot = Bot(token="YOUR_TOKEN_HERE")
# Bot'ga xabar yuboring va Admin User ID'ni oling
```

Yoki Telegram'da @userinfobot'dan admin ID'ni olish

### Qadam 3: .env'ga kiriting
```
TELEGRAM_ADMIN_ID=123456789
```

---

## 5️⃣ ADMIN KARTA MA'LUMOTLARINI SOZLASH (To'lov Uchun)

### Qadam 1: Karta raqamini tayyorlash
Bankingizning Humo/Click/Amal kartasini tayyorlang

### Qadam 2: .env'ga Ma'lumotlar Kiriting
```env
ADMIN_CARD_NUMBER=9860-XXXX-XXXX-1234
ADMIN_CARD_HOLDER=Sizning Ismingiz
ADMIN_BANK=Humo Bank
```

### Qadam 3: To'lov Tizimini Test Qilish
```powershell
python test_payment_system.py
```

Output bo'lishi kerak:
```
✅ Narx kalkulyatori to'g'ri ishlaydi!
✅ To'lov kuzatuvchisi to'g'ri ishlaydi!
✅ Admin kartasi to'g'ri ishlay verdi!
```

---

## 6️⃣ YAKUNIY .ENV FILE

### To'liq .env fayli:
```env
# Telegram
TELEGRAM_BOT_TOKEN=1234567890:ABCdefGHIjklmnoPQRstuvWXYZ-a1b2c3d4e5f
TELEGRAM_ADMIN_ID=123456789

# OpenAI
OPENAI_API_KEY=sk-1234567890abcdefghijklmnopqrstuvwxyz
OPENAI_MODEL=gpt-3.5-turbo

# Admin Karta Ma'lumotlari
ADMIN_CARD_NUMBER=9860-XXXX-XXXX-1234
ADMIN_CARD_HOLDER=Admin Nomi
ADMIN_BANK=Humo Bank
```

---

## 7️⃣ .ENV FAYLINI SOZLASH

### Qadam 1: .env faylini ochish
VS Code'da `.env` faylini oching:

### Qadam 2: Barcha Ma'lumotlarni Kiriting
- TELEGRAM_BOT_TOKEN ✅
- TELEGRAM_ADMIN_ID ✅
- OPENAI_API_KEY ✅
- ADMIN_CARD_NUMBER ✅
- ADMIN_CARD_HOLDER ✅
- ADMIN_BANK ✅

### Qadam 3: Faylni Saqlang
`Ctrl+S` bilan saqlang

---

## 8️⃣ BOTNI ISHGA TUSHIRISH

### Qadam 1: Terminal'ni oching
```powershell
cd "c:\Users\Asus\Desktop\PremiumReferat"
```

### Qadam 2: Premium Bot'ni Ishga Tushiring
```powershell
python bot_advanced.py
```

### Qadam 3: Tekshiruv Xabar
Terminal'da ko'rish kerak:
```
🤖 Premium Referat Bot ishga tushdi!
🔗 Telegram'da botingizni qidiring va /start buyrug'ini kiriting
💳 Admin ID: 123456789
```

---

## 9️⃣ BOTNI TELEGRAM'DA TEST QILISH

### Qadam 1: Bot'ni topish
- Telegram'da o'zingiz yaratgan bot username'ni qidiring
- Botni oching

### Qadam 2: /start buyrug'ini kiriting

### Qadam 3: Referat yaratish
1. Mavzuni kiriting (masalan: "O'zbekistan tarixishi")
2. Ta'lim darajasini tanlang (masalan: "Universitet")
3. Bet diapazonini tanlang (masalan: "10-15")
4. Aniq betlar sonini kiriting (masalan: "12")
5. Formatni tanlang (masalan: "Chuqur tahlili")
6. Narxni ko'rib tasdiqlang
7. Admin kartasiga to'lov qiling
8. Chek screenshoti yuboring
9. Admin 5 daqiqa ichida tasdiqlaydi
10. Premium referat olasiz!

---

## 🔟 KO'P TAKRORLANUVCHI MUAMMOLAR

### ❌ "TELEGRAM_BOT_TOKEN muhit o'zgaruvchisida o'rnatilmagan!"

**Sabablar:**
- .env faylida token yo'q
- Token noto'g'ri kiritilgan
- .env fayli saqlanmagan

**Yechim:**
```
1. .env faylini oching
2. TELEGRAM_BOT_TOKEN='token_kiriting' deb yozing
3. Faylni saqlang (Ctrl+S)
4. Bot'ni qayta ishga tushiring
```

---

### ❌ "OPENAI_API_KEY muhit o'zgaruvchisida o'rnatilmagan!"

**Sabablar:**
- .env faylida API key yo'q
- Key noto'g'ri kiritilgan
- Billing sozlanmagan

**Yechim:**
```
1. OpenAI'da kredit qo'shing
2. .env faylida key'ni to'g'ri kiriting
3. Bot'ni qayta ishga tushiring
```

---

### ❌ "ModuleNotFoundError: No module named 'telegram'"

**Sabablar:**
- Kutubxonalar o'rnatilmagan

**Yechim:**
```powershell
pip install -r requirements.txt
```

---

### ❌ Bot xabar bermimoqda

**Sabablar:**
- Bot token noto'g'ri
- Bot ishga tushmagan
- Internet ulanmagan

**Yechim:**
```
1. Terminal'da xabar bor-yo'qligini tekshiring
2. Token'ni qayta tekshiring
3. Internet ulanishni tekshiring
4. Bot'ni qayta ishga tushiring
```

---

## 💡 ADVANCED SOZLAMALAR

### .env'ga qo'shimcha sozlamalar:
```env
TELEGRAM_BOT_TOKEN=your_token
OPENAI_API_KEY=your_api_key
TELEGRAM_ADMIN_ID=your_user_id
OPENAI_MODEL=gpt-3.5-turbo
```

### config.py'da o'zgarishlar:
```python
MAX_PAGES = 50        # Maksimal betlar
MIN_PAGES = 3         # Minimal betlar
DEFAULT_TEMPERATURE = 0.8  # Yaratishning noziqligi
```

---

## 🔧 DEBUGGING

### Terminal'da debug mode:
```python
# bot.py'da
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.DEBUG  # DEBUG yoki INFO
)
```

---

## 📞 YORDAM VA QOLLAB-QUVVATLASH

Agar muammo bo'lsa:

1. **Terminal xatolarini o'qing** - Ko'pincha javob u yerda bor
2. **API kalitlarini tekshiring** - Token va key noto'g'ri bo'lishi mumkin
3. **.env faylini tekshiring** - Kalit-qiymat juftligi to'g'ri bo'lishi kerak
4. **Internet'ni tekshiring** - API so'rovlari uchun internet kerak

---

## ✅ MUVAFFAQIYAT!

Bot'ingiz ishga tushdi! 🎉

Telegram'da `/start` buyrug'ini kiriting va referatlar yaratishni boshlang!

---

**© 2025 Premium Referat Bot**
