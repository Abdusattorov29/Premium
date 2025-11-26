# 📚 Premium Referat Bot v3.0 - To'liq Yo'riqnoma

AI yordamida professional referatlar yaratadigan Telegram bot'ning to'liq paketi, **to'lov tizimi bilan**.

## 🌟 Xususiyatlar

### ✨ Kuchli AI
- **OpenAI GPT-3.5 Turbo** - Eng yangi AI modeli
- **Professional matn** - Sifatli va maqolali referatlar
- **O'zbekcha til** - To'g'ri o'zbekcha terminologiya
- **Premium Sifat** - Yangilangan prompts bilan juda yaxshi natijalar

### 💳 **YANGI: To'lov Tizimi**
- **Dinamik Narxlar** - Diapazon va ta'lim darajasi bo'yicha
- **Admin Kartasi** - Xavfsiz to'lov o'tkazish
- **Chek Tekshirish** - Rasm orqali validatsiya
- **Admin Panel** - Tasdiqlash/Rad etish uchun

### 📚 Moslashtirilgan Referatlar
- **4 ta ta'lim darajasi** - Maktab, Kollejj, Universitet, Magistratura
- **Bet bo'yicha diapazonlar** - 1-5, 5-10, 10-15, 15-20
- **3 ta format** - Oddiy matn, Struktura bilan, Chuqur tahlili bilan

### 🎨 Foydalanuvchi-do'st
- **Tugma-tugma qo'llab-quvvatlash** - Oson interfeys
- **Narx ko'rish** - Tanlovdan oldin bilish
- **Tarixcha** - O'zingiz yaratgan referatlar tarihini ko'ring

## 📁 Fayllar Tuzilishi

```
PremiumReferat/
├── bot_advanced.py         # Premium Bot (To'lov tizimi bilan)
├── payment_system.py       # 🆕 To'lov va Narx tizimi
├── config.py               # Konfiguratsiya va narxlar
├── test_payment_system.py  # 🆕 To'lov tizimi testlari
├── check_setup.py          # Sozlamalarni tekshirish
├── requirements.txt        # Zarur kutubxonalar
├── .env                    # API kalitlari (YASHRIN!)
├── .env.example            # 🆕 .env namunasi
├── payments.json           # 🆕 To'lov bazasi
├── Dockerfile              # Docker konteyner
├── docker-compose.yml      # Docker Compose konfiguratsiyasi
├── SETUP.md                # Ishga tushirish yo'riqnomasi
├── PREMIUM_VERSION_README.md # 🆕 Premium versiya yo'riqnomasi
└── README_UZ.md            # Bu fayl
```

### 3️⃣ API Kalitlarini Sozlash
`.env` faylini oching va quyidagini kiriting:
```
TELEGRAM_BOT_TOKEN=your_token_here
OPENAI_API_KEY=your_api_key_here
```

### 4️⃣ Bot'ni Ishga Tushirish
```bash
# Advanced versiya (tavsiya etiladi)
python bot_advanced.py

# Yoki oddiy versiya
python bot.py
```

## 📖 Foydalanish

### Telegram'da Bot'ni Ochish
1. Telegram'da o'zingiz yaratgan bot'ni toping
2. `/start` buyrug'ini kiriting

### Referat Yaratish
1. **Mavzu** - O'zni qiziqtirgan mavzuni kiriting
2. **Ta'lim darajasi** - Maktab, Kollejj, Universitet yoki Magistratura'ni tanlang
3. **Betlar soni** - 3-50 bet oralig'ida raqam kiriting
4. **Format** - Oddiy, Struktura yoki Chuqur formatini tanlang
5. **Kutish** - Bot 1-3 minutda referat tayyorlaydi

### Buyruqlar
- `/start` - Yangi referat yaratishni boshlash
- `/help` - Yordam ko'rish
- `/cancel` - Bekor qilish

## ⚙️ Sozlamalar

### bot_advanced.py (tavsiya etiladi)
- **Tugma interfeysi** - Yaxshi UX
- **Tarixcha** - O'zingiz yaratgan referatlar
- **3 ta format** - Turli xil o'rnatishlar
- **Ishlab chiquvchi toolbar** - Qayta boshlash, tarixcha, yordam

### bot.py (sodda versiya)
- **Matnli retstsiya** - Sodda fikr-mulohaza
- **Tez jadval** - Kam xotira ishlatish
- **Klassik interfeys** - Oʻzgarishsiz

## 🔒 Xavfsizlik

⚠️ **Muhim:** .env faylini hech qachon baghlang, GitHub'ga yuklamang yoki boshkalarni ko'rsatmang!

### .env faylini .gitignore ga qo'shish
```
# .gitignore
.env
.env.local
.env.*.local
```

## 🐳 Docker Bilan Ishlatish (Advanced)

### O'rnatish
```bash
docker-compose up -d
```

### Bosqa olish
```bash
docker-compose down
```

### Loglarni ko'rish
```bash
docker logs premium-referat-bot
```

## 🛠️ Debugging

### Tekshirish
```bash
python check_setup.py
```

### Qo'llab-quvvatlash
- **API kalitlarini tekshiring** - .env faylida to'g'ri joylashtirilgan bo'lishi kerak
- **Internet ulanishni tekshiring** - API so'rovlari uchun zarur
- **Kutubxonalarni tekshiring** - `pip install -r requirements.txt`
- **Terminal xatolarini o'qing** - Ko'pincha yechim u yerda

## 📊 Qo'llaniladigan Mavzular

Bot har qanday mavzu bo'yicha referat yaratishi mumkin:

- 📚 **Adabiyot** - Qo'shiqlar, hikoyalar, xronologiya
- 🔬 **Fan** - Fizika, Kimya, Biologiya, Astronomiya
- 🌍 **Geografiya** - Davlatlar, shaharlar, tabiiy hodisalar
- 💻 **Texnologiya** - Dasturlash, AI, Tahlillar
- 📖 **Tarix** - Davlatlar, voqealar, kimblar
- 🏛️ **Huquq** - Qonunlar, huquqlar, majburiyatlar
- 💼 **Iqtisodiyot** - Bozor, tibbiyot, moliya
- 🎨 **San'at** - Rasmlash, musiqa, badiiyat
- Va boshqa ko'plab mavzular!

## 💡 Maslahatlar

1. **Mavzuni aniq kiriting** - "Futbol" emas, "O'zbekistonning futbol tarixiga"
2. **To'g'ri ta'lim darajasini tanlang** - Darajaga mos chuqurlik
3. **Betlar sonini mantiqan kiriting** - Katta hajm = katta vaqt
4. **Format'ni tanlang** - Qanday prezentasiya kerak
5. **Sabrli bo'ling** - Katta referatlar uchun vaqt talab qiladi

## 🐛 Muammolar va Yechimlar

### Muammo: "Bot xabar bermimoqda"
**Yechim:**
1. API kalitlarini tekshiring
2. Internet ulanishni tekshiring
3. Terminal'dagi xatolarni o'qing

### Muammo: "Xato: ModuleNotFoundError"
**Yechim:**
```bash
pip install -r requirements.txt
```

### Muammo: "Referat juda qisqa"
**Yechim:**
- Betlar sonini oshiring
- Format'ni o'zgartiring

### Muammo: "OpenAI xatosi"
**Yechim:**
1. Kredit qo'shing
2. API key'ni tekshiring
3. Tarifi'ni o'zikirtiring

## 📞 Qo'llab-quvvatlash

**To'liq o'rnatish yo'riqnomasi uchun:**
- `SETUP.md` faylini o'qing
- Terminal'dagi xatolar
- OpenAI va Telegram dokumentatsiyasi

## 🎯 Keyingi Versiyalar Uchun Rejalandi

- ✅ PDF sifatida yuklab olish
- ✅ Word formatida yuklab olish
- ✅ Tarixcha bilan saqlash
- ✅ O'zgarishni tayyorlash
- ✅ Ko'p tilida qo'llab-quvvatlash
- ✅ Ota-ona modeli (GPT-4)
- ✅ Referat shablonlari

## 📜 Litsenziya

© 2025 Premium Referat Bot. Barcha huquqlar himoyalangan.

---

## 🙏 Rahmat!

Bot'dan foydalanganingiz uchun tashakkur! Agar bot sizga yordam bergan bo'lsa, deb o'ylaymiz!

**Muvaffaqiyat tiliyavmiz! 🎉**

---

**Muallif:** AI Development Team  
**Versiya:** 2.0  
**Sifari:** 2025-01-01
