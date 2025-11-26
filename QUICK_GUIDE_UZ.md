# 📚 Premium Referat Bot v3.0 - O'zbekcha Yo'riqnoma

AI yordamida professional referatlar yaratadigan Telegram bot. **To'lov tizimi bilan yangilangan!**

## 🌟 Yangiliklari v3.0

### 💳 To'lov Tizimi
- ✅ **Dinamik Narxlar** - Bet diapazoni va ta'lim darajasi bo'yicha
- ✅ **Admin Kartasi** - Xavfsiz to'lov
- ✅ **Chek Tekshirish** - Screenshot validatsiyasi  
- ✅ **Admin Panel** - Tasdiqlash/Rad etish

### 📄 Bet Diapazonlari
```
1-5 bet     → 10,000 UZS
5-10 bet    → 20,000 UZS
10-15 bet   → 30,000 UZS
15-20 bet   → 40,000 UZS
```

### 🎓 Ta'lim Darajasi Koeffitsiyentlari
```
🎒 Maktab        → x1.0  (asosiy)
🏫 Kollejj       → x1.3  (+30%)
🎓 Universitet   → x1.7  (+70%)
📚 Magistratura  → x2.2  (+120%)
```

### 📋 Format Koeffitsiyentlari
```
📝 Oddiy matn       → x1.0  (asosiy)
📋 Struktura bilan  → x1.1  (+10%)
✍️ Chuqur tahlili  → x1.4  (+40%)
```

---

## 💰 Narx Hisoblash Misolları

### 1️⃣ Maktab Talabasi
```
Betlar: 5 ta | Ta'lim: Maktab | Format: Oddiy
Narx = 10,000 × 1.0 × 1.0 = 10,000 UZS
```

### 2️⃣ Universitet Talabasi
```
Betlar: 12 ta | Ta'lim: Universitet | Format: Chuqur
Narx = 30,000 × 1.7 × 1.4 = 71,400 UZS
```

### 3️⃣ Magistrant
```
Betlar: 18 ta | Ta'lim: Magistratura | Format: Chuqur
Narx = 40,000 × 2.2 × 1.4 = 123,200 UZS
```

---

## 🚀 Ishga Tushirish

### 1️⃣ O'rnatish
```bash
pip install -r requirements.txt
```

### 2️⃣ Konfiguratsiya
`.env` faylini yarating va to'ldiring:
```
TELEGRAM_BOT_TOKEN=xxx
TELEGRAM_ADMIN_ID=xxx
OPENAI_API_KEY=xxx
ADMIN_CARD_NUMBER=9860-XXXX-XXXX-XXXX
ADMIN_CARD_HOLDER=Admin Nomi
ADMIN_BANK=Humo Bank
```

### 3️⃣ Ishga Tushirish
```bash
python bot_advanced.py
```

---

## 📱 To'lov Oqimi

1. **Foydalanuvchi tanlov qiladi**
2. **Narx hisob-kitoblanadi**
3. **Admin kartas ma'lumot ko'rsatiladi**
4. **Chek screenshoti yuboriladı**
5. **Admin tekshiradi va tasdiqlaydi**
6. **Premium referat yaratiladi**
7. **Foydalanuvchiga yuboriladi**

---

## 📂 Muhim Fayllar

| Fayl | Tavsif |
|------|--------|
| `bot_advanced.py` | Premium bot (to'lov tizimi) |
| `payment_system.py` | 🆕 To'lov tizimi |
| `config.py` | Sozlamalar va narxlar |
| `payments.json` | 🆕 To'lov bazasi |
| `test_payment_system.py` | 🆕 Testlar |

---

## 🎯 Bot Komandalar

```
/start   - Yangi referat yaratish
/help    - Yordam ko'rish
/cancel  - Bekor qilish
```

**Admin:** Chek rasmiga ✅ yoki ❌ bosing

---

## ⚙️ Premium Xususiyatlari

- ✅ Chuqur akademik mazmun
- ✅ Konkret misollar va statistika
- ✅ Olimlar fikrlari va dalillar
- ✅ To'g'ri o'zbekcha til
- ✅ Professional uslub
- ✅ 100% original

---

## 🛠️ Debugging

### Testni Ishga Tushirish
```bash
python test_payment_system.py
```

### Soklamalarni Tekshirish
```bash
python check_setup.py
```

---

## 📞 Muammolar

| Muammo | Yechim |
|--------|--------|
| Bot xabar bermimoqda | API keyni tekshiring |
| ModuleNotFoundError | `pip install -r requirements.txt` |
| To'lov rada etildi | Chekni to'g'ri yuboring |
| Referat qisqa | Betlar sonini oshiring |

---

## 📖 To'liq Yo'riqnoma

Batafsil ma'lumot uchun quyidagilarni o'qing:
- `PREMIUM_VERSION_README.md` - Premium versiya
- `SETUP.md` - Batafsil o'rnatish
- `README.md` - English versiya

---

**v3.0 Premium** 🚀 | To'lov tizimi bilan | 2025

Muvaffaqiyat tilaymiz! 🎉
