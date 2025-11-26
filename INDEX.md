# 📖 INDEX - Barcha Fayllar va Maqsadi

## 🎯 Ishni Boshlash

Agar siz yangi bo'lsangiz, **QUICK_START.txt** dan boshlang! (5 minut)

---

## 📂 FAYLLAR RO'YXATI

### 🤖 BOT FAYLLAR (Asosiy)

#### `bot.py` 
- **Maqsad:** Asosiy bot versiyasi (sodda)
- **Xususiyatlari:** Suhbat interfeysi, oddiy strukturа
- **Foydalanish:** `python bot.py`
- **O'lchami:** ~2-3 KB
- **Tavsiya:** Boshlang'ich foydalanuvchilar uchun

#### `bot_advanced.py`
- **Maqsad:** Kuchli bot versiyasi (tavsiya etiladi)
- **Xususiyatlari:** Tugmalar, tarixcha, 3 ta format
- **Foydalanish:** `python bot_advanced.py`
- **O'lchami:** ~5-6 KB
- **Tavsiya:** Barchasi uchun tavsiya etiladi

#### `config.py`
- **Maqsad:** Konfiguratsiya va konstantalar
- **Tarkibi:** Habarlar, shablonlar, sozlamalar
- **Foydalanish:** Bot'dan avtomatik import qilinadi

#### `logger.py`
- **Maqsad:** Logging va statistika
- **Xususiyatlari:** JSON log saqlaш, statistika
- **Foydalanish:** Avtomatik (bot_activity.json)

---

### ⚙️ SETUP VA KONFIGURATSIYA

#### `requirements.txt`
- **Maqsad:** Python kutubxonalari
- **Tarkibi:** 4 ta kutubxona
- **Foydalanish:** `pip install -r requirements.txt`
- **Muhim:** Birinchi narsaga o'rnatish!

#### `.env`
- **Maqsad:** API kalitlari va tavsiflar
- **Tarkibi:** TELEGRAM_BOT_TOKEN, OPENAI_API_KEY
- **Xavfsizlik:** ⚠️ YASHIRIN SAQLANG!
- **Misol:** `TELEGRAM_BOT_TOKEN=123456...`

#### `Dockerfile`
- **Maqsad:** Docker konteyner konfiguratsiyasi
- **Foydalanish:** Docker bilan (opsional)
- **Buyruq:** `docker build -t referat-bot .`

#### `docker-compose.yml`
- **Maqsad:** Docker Compose konfiguratsiyasi
- **Foydalanish:** `docker-compose up -d`
- **O'lchami:** ~5 KB

---

### 📚 DOKUMENTASIYA (O'QING!)

#### `QUICK_START.txt` ⭐ BOSHLASH UCHUN
- **Vaqti:** 5 minut
- **Maqsadi:** Tezkor boshlanish
- **Tavsiya:** Birinchisi o'qing!
- **O'lchami:** ~2 KB

#### `SETUP.md` - TO'LIQ YO'RIQNOMA
- **Vaqti:** 10-15 minut
- **Maqsadi:** Step-by-step o'rnatish
- **Tarkibi:** Token, API Key, o'rnatish, debugging
- **O'lchami:** ~8 KB

#### `FAQ_HELP.md` - MUAMMOLAR
- **Maqsadi:** Ko'p soraladigan savollar
- **Tarkibi:** Muammolar va yechimlar
- **Foydalanish:** Xato bo'lganda
- **O'lchami:** ~10 KB

#### `README.md` - ASOSIY YO'RIQNOMA
- **Tili:** Inglizcha
- **Maqsadi:** Umumiy yo'riqnoma
- **O'lchami:** ~5 KB

#### `README_UZ.md` - O'ZBEKCHA YO'RIQNOMA
- **Tili:** O'zbekcha (Lotin)
- **Maqsadi:** Toliq o'riqnoma
- **O'lchami:** ~8 KB
- **Tavsiya:** O'zbek foydalanuvchilar uchun

#### `PROJECT_SUMMARY.md` - LOYIHA XULOSA
- **Maqsadi:** Loyiha haqida ma'lumot
- **Tarkibi:** Texnika, xususiyatlar, version
- **O'lchami:** ~6 KB

#### `INDEX.md` - BU FAYL
- **Maqsadi:** Barcha fayllarni tavsif
- **Tarkibi:** File guide
- **O'lchami:** ~5 KB

---

### 🧪 TEST VA DEBUG FAYLLAR

#### `test_setup.py`
- **Maqsad:** Barcha sozlamalarni tekshirish
- **Foydalanish:** `python test_setup.py`
- **Ko'radi:** Files, packages, env, syntax
- **Tavsiya:** Ishlashdan oldin ishga tushiring

#### `check_setup.py`
- **Maqsad:** Tezkor sozlamalarni tekshirish
- **Foydalanish:** `python check_setup.py`
- **Ko'radi:** Environment, kutubxonalar, fayllar
- **O'lchami:** ~2 KB

#### `show_project.py`
- **Maqsad:** Loyihani vizualizatsiya qilish
- **Foydalanish:** `python show_project.py`
- **Ko'radi:** Fayllar, buyruqlar, next steps
- **O'lchami:** ~4 KB

#### `bot_activity.json`
- **Maqsad:** Logslar va statistika
- **Tarkibi:** JSON format'da logslar
- **Yaratiladi:** Bot ishlashda avtomatik
- **Foydalanish:** Statistika uchun

---

## 🚀 QAYERDAN BOSHLASH?

### 1. Birinchi Safar
1. **QUICK_START.txt** o'qing (5 min)
2. **Token va API Key** olish
3. `.env` faylida kiriting
4. `pip install -r requirements.txt`
5. `python bot_advanced.py`
6. Telegram'da `/start` bosing

### 2. Muammo Bo'lsa
1. **FAQ_HELP.md** o'qing
2. **test_setup.py** ishga tushiring
3. Terminal xatolarni o'qing
4. **SETUP.md** ga qarang

### 3. Chuqur O'qish Uchun
1. **README_UZ.md** o'qing
2. **PROJECT_SUMMARY.md** ni ko'ring
3. Bot kodi bilan tanishing (`bot_advanced.py`)

---

## 📋 QANDAY FILE O'QISH?

| Fayz | Uchun | O'qish Vaqti |
|------|-------|------------|
| QUICK_START.txt | 5 minut'da boshlang | 5 min |
| SETUP.md | To'liq o'rnatish | 10 min |
| FAQ_HELP.md | Muammolar | Kerak bo'lganda |
| README_UZ.md | O'zbekcha toliq | 15 min |
| PROJECT_SUMMARY.md | Teknik ma'lumot | 10 min |

---

## ⌨️ TEZKOR BUYRUQLAR

```bash
# Bot'ni ishga tushirish
python bot_advanced.py

# Sozlamalarni tekshirish
python test_setup.py

# Logslarni ko'rish
cat bot_activity.json

# Docker bilan ishga tushirish
docker-compose up -d

# Python versiyasini tekshirish
python --version

# Kutubxonalarni o'rnatish
pip install -r requirements.txt
```

---

## 🎯 FAYLLAR MERKAZI

### Muhim Fayllar ⚠️
- **`.env`** - API kalitlari (YASHIRIN!)
- **`bot_advanced.py`** - Asosiy bot
- **`requirements.txt`** - Kutubxonalar

### Dokumentasiya 📚
- **`QUICK_START.txt`** - Boshlang'ich
- **`SETUP.md`** - To'liq yo'riqnoma
- **`FAQ_HELP.md`** - Muammolar

### Debug va Test 🧪
- **`test_setup.py`** - Tekshirish
- **`bot_activity.json`** - Logslar

---

## 💡 MASLAHATLAR

1. **Fayllarni o'qing** - README'larni albatta o'qing
2. **Test qiling** - `test_setup.py` ishga tushiring
3. **Debug mode** - Xato bo'lsa logsni o'qing
4. **Docker** - Server'da Docker'dan foydalaning
5. **Security** - `.env` faylini yashirin saqlang

---

## 📞 QANDAY YORDAMLIK?

- **5 minut'da boshlash?** → `QUICK_START.txt`
- **Muammo?** → `FAQ_HELP.md`
- **Teknik ma'lumot?** → `PROJECT_SUMMARY.md`
- **To'liq yo'riqnoma?** → `SETUP.md`
- **Tekshirish?** → `python test_setup.py`

---

## ✅ CHEKLSIT - BOSHLASHDAN OLDIN

- [ ] Python 3.8+ o'rnatilgan
- [ ] Telegram Bot Token olgan
- [ ] OpenAI API Key olgan
- [ ] `.env` faylida kiritilgan
- [ ] `pip install -r requirements.txt` o'tkazilgan
- [ ] `python test_setup.py` ishladi

**Hammasi OK bo'lsa, `python bot_advanced.py` ishga tushiring!** 🚀

---

**© 2025 Premium Referat Bot**  
**Version: 2.0**  
**Oxirgi yangilanish: 2025-11-25**
