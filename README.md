# 📚 Premium Referat Bot

AI yordamida referatlar yasaydigan Telegram boti.

## ⚙️ O'rnatish

### 1. Python o'rnatish
Python 3.8+ o'rnatilgan bo'lishi kerak.

### 2. Kutubxonalarni o'rnatish
```bash
pip install -r requirements.txt
```

### 3. API Kalitlarini sozlash

#### Telegram Bot Token olish:
1. Telegramda @BotFather'ga yozing
2. `/newbot` buyrug'ini kiriting
3. Bot nomini va username'ni kiriting
4. Olingan tokenni `.env` fayliga kiriting

#### OpenAI API Key olish:
1. https://platform.openai.com ga o'ting
2. API kalitni yaratishga o'ting
3. Kalitni `.env` fayliga kiriting

### 4. .env faylini to'ldirish
```
TELEGRAM_BOT_TOKEN=YOUR_BOT_TOKEN_HERE
OPENAI_API_KEY=YOUR_API_KEY_HERE
```

## 🚀 Botni ishga tushirish

```bash
python bot.py
```

## 🎯 Botni foydalanish

### Buyruqlar:
- `/start` - Yangi referat yaratish boshlash
- `/help` - Yordam ko'rish
- `/cancel` - Amalni bekor qilish

### Referat yaratish jarayoni:
1. `/start` buyrug'ini kiriting
2. Referat mavzusini kiriting
3. Ta'lim darajasini tanlang (1-4)
4. Betlar sonini kiriting (3-50)
5. Bot referat yaratadi va sizga yuboradi

## 📋 Xususiyatlar

✨ **Kuchli AI**
- OpenAI GPT-3.5 Turbo modeli
- Professional va sifatli matnlar

📚 **Moslashtirilgan Referatlar**
- Turli ta'lim darajalariga mos
- Talab bo'yicha hajm
- Mavsuga mos mazmun

🎨 **Foydalanuvchi-do'st Interfeys**
- Oson va tushunarliroq suhbat
- Qadam-qadam ko'rsatmalar
- Tezkor xizmat

## 📝 Fayllar Tuzilishi

```
PremiumReferat/
├── bot.py              # Asosiy bot fayli
├── requirements.txt    # Zarur kutubxonalar
├── .env                # API kalitlari
└── README.md          # Dokumentasiya
```

## 🔧 Muammolar va Yechimlar

**Xato: "TELEGRAM_BOT_TOKEN muhit o'zgaruvchisida o'rnatilmagan!"**
- `.env` faylida token to'g'ri kiritilganligini tekshiring

**Xato: "OPENAI_API_KEY muhit o'zgaruvchisida o'rnatilmagan!"**
- `.env` faylida OpenAI API kalit to'g'ri kiritilganligini tekshiring

**Referatlar juda qisqa/uzun bo'lyapti**
- Betlar sonini o'zgartirishga harakat qiling

## 💡 Maslahatlar

- Mavzuni aniq va tafsili bilan kiriting
- To'g'ri ta'lim darajasini tanlang
- Katta hajmli referatlar uchun vaqt bering

## 📞 Qo'llab-quvvatlash

Savol yoki muammo bo'lsa, bot administratoriga murojaat qiling.

---

**© 2025 Premium Referat Bot. Barcha huquqlar himoyalangan.**
