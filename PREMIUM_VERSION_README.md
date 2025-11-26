# 🎓 Premium Referat Bot v3.0

## 🆕 Yangilangan Xususiyatlar

### 💳 **To'lov Tizimi**
- ✅ **Dinamik Narxlar** - diapazon va ta'lim darajasi bo'yicha
- ✅ **Admin Kartasi** - Humo, Click, Amal, va boshqa kartalar
- ✅ **Chek Tekshirishi** - Rasm orqali to'lov tasdiqlash
- ✅ **Admin Panel** - Tasdiqlash/Rad etish uchun

### 📄 **Betlar bo'yicha Variantlar**
```
1-5 bet   → 10,000 UZS (asosiy narx)
5-10 bet  → 20,000 UZS
10-15 bet → 30,000 UZS
15-20 bet → 40,000 UZS
```

### 🎓 **Ta'lim Darajasi bo'yicha Koeffitsiyentlar**
```
🎒 Maktab (8-11)   → x1.0  (asosiy)
🏫 Kollejj         → x1.3  (+30%)
🎓 Universitet      → x1.7  (+70%)
📚 Magistratura    → x2.2  (+120%)
```

### 📋 **Format Koeffitsiyentlari**
```
📝 Oddiy matn      → x1.0  (asosiy)
📋 Struktura bilan → x1.1  (+10%)
✍️ Chuqur tahlili → x1.4  (+40%)
```

### 🔐 **To'lov Oqimi**

1. **Foydalanuvchi tanlovini yaratadi:**
   - Mavzu
   - Ta'lim darajasi
   - Bet diapazoni (1-5, 5-10, 10-15, 15-20)
   - Aniq betlar soni
   - Format

2. **Narx hisob-kitoblanadi:**
   ```
   Narx = Asosiy Narx × Ta'lim Koeffitsiyenti × Format Koeffitsiyenti
   ```

3. **To'lov admin kartasiga o'tkaziladi:**
   - Karta raqami ko'rsatiladi
   - Chek screenshoti yuboriladigo
   - Admin onayini kutiladi

4. **Admin Tasdiqlash:**
   - Chekni tekshiradi
   - ✅ Tasdiqlaydi yoki ❌ Rad etadi
   - Foydalanuvchi bildirishnoma oladi

5. **Referat Yaratiladi:**
   - Premium sifatda
   - Dinamik mazmuni
   - Foydalanuvchiga yuboriladi

---

## 💰 **Narx Hisoblash Misollari**

### Maktab Talabasi - Oddiy Format
```
Mavzu: O'zbekistan tarixishi
Darajasi: Maktab (8-11 sinf)
Betlar: 5 ta
Format: Oddiy matn

Narx = 10,000 × 1.0 × 1.0 = 10,000 UZS
```

### Universitet - Chuqur Tahlili
```
Mavzu: Milliy demokratiya
Darajasi: Universitet
Betlar: 12 ta
Format: Chuqur tahlili

Narx = 30,000 × 1.7 × 1.4 = 71,400 UZS
```

### Magistratura - Premium
```
Mavzu: Siyosiy iqtisodiyot
Darajasi: Magistratura
Betlar: 18 ta
Format: Chuqur tahlili

Narx = 40,000 × 2.2 × 1.4 = 123,200 UZS
```

---

## 🛠️ **O'rnatish va Sozlash**

### 1. **Muhit O'zgaruvchilari (.env)**
```
TELEGRAM_BOT_TOKEN=your_token_here
TELEGRAM_ADMIN_ID=your_admin_id
OPENAI_API_KEY=your_openai_key

# Admin Karta Ma'lumotlari
ADMIN_CARD_NUMBER=9860-XXXX-XXXX-XXXX
ADMIN_CARD_HOLDER=Admin Nomi
ADMIN_BANK=Humo Bank
```

### 2. **Paketlarni O'rnatish**
```bash
pip install -r requirements.txt
```

### 3. **Botni Ishga Tushirish**
```bash
python bot_advanced.py
```

---

## 📊 **To'lov Tizimi Ma'lumotlari**

### Fayllar:
- `payment_system.py` - To'lov tizimi logikasi
- `payments.json` - Barcha to'lovlar tarixchasi
- `config.py` - Sozlamalar va narxlar

### Klasslar:
```python
# Narxlarni hisoblash
pricing = PricingSystem()
price = pricing.calculate_price(12, 'university', 'detailed')
# Output: {'final_price': 71400, 'currency': 'UZS', ...}

# To'lovlarni kuzatish
tracker = PaymentTracker()
payment = tracker.create_payment(user_id, username, 50000, ...)

# Admin kartasi
admin_card = AdminCard()
instruction = admin_card.get_payment_instruction()
```

---

## 🎯 **Bot Komandalar**

```
/start      - Yangi referat yaratish
/help       - Yordam ko'rish
/cancel     - Bekor qilish
```

### Admin Komandalar:
- Chek rasmiga javob bering: ✅ Tasdiqlash yoki ❌ Rad etish

---

## 📈 **Referat Sifati**

### PREMIUM Referat Xususiyatlari:
✅ Juda chuqur va ilmiy mazmun
✅ Konkret misollar va statistika
✅ Olim fikri va dalillar
✅ Professional uslub
✅ To'g'ri o'zbekcha til
✅ Akademik strukturasi
✅ 100% original (plagiatdan voz kechilib)

---

## 💳 **To'lov Misol Oqimi**

```
Foydalanuvchi: @user123
Mavzu: Tarix
Darajasi: Universitet
Bet diapazoni: 10-15
Betlar soni: 12
Format: Chuqur tahlili

Narx: 30,000 (asosiy) × 1.7 (universitet) × 1.4 (tahlili)
    = 71,400 UZS

↓

Admin karta: 9860-XXXX-XXXX-XXXX (Humo Bank)
Chek: Screenshot yuboriadi

↓

Admin chekni tekshiradi:
- Summa: 71,400 UZS ✅
- Vaqt ko'rinishi: ✅
- Status: Tasdiqlandi

↓

Bot foydalanuvchiga premium referatni yuboradi
Sifati: A+ 🌟
Hajmi: ~4,200 so'z
```

---

## 🔄 **Yangilangan To'lov Oqimi**

### Eski (v2.0):
```
Referat yaratish → Foydalanuvchi oladi (BEPUL)
```

### Yangi (v3.0):
```
Tanlov → Narx hisoblash → To'lov → Admin Tekshirish → 
Referat Yaratish → Yuborish → Baholash
```

---

## 📝 **Fayl Tuzilishi**

```
bot_advanced.py          # Asosiy bot faylı
payment_system.py        # To'lov tizimi
config.py               # Sozlamalar
payments.json           # To'lov bazasi
requirements.txt        # Paketlar
.env                   # Muhit o'zgaruvchilari
```

---

## 🚀 **Kelajakdagi Yangilashlar**

- [ ] Uzbek Bank API integratsiyasi
- [ ] Kopon va Promokodlar
- [ ] Foydalanuvchi reyting tizimi
- [ ] Admin statistika paneli
- [ ] Qayta to'lov tizimi
- [ ] Referat shablonlari

---

## ⚠️ **Muhim Eslatmalar**

1. **Admin ID'ni o'rnatilgan ekanini tekshiring:**
   ```
   TELEGRAM_ADMIN_ID ni .env da kiriting
   ```

2. **Karta raqamini himoyalang:**
   ```
   Real kartani .env da xavfsiz saqlang
   ```

3. **OpenAI Token Limitini Tekshiring:**
   ```
   Katta referatlar uchun ko'p token sarflaydi
   ```

4. **To'lov Bazasini Nishonlang:**
   ```
   payments.json muhim ma'lumot, backup qilib turing
   ```

---

## 📞 **Qo'llab-Quvvatlash**

Muammo yuzaga kelsa:
1. Loglarni tekshiring
2. .env o'zgaruvchilarini tasdiqlayin
3. OpenAI API limitini tekshiring
4. Bot tokenini qayta o'rnatib ko'ring

---

**Muvaffaqiyat tilaymiz!** 🌟
