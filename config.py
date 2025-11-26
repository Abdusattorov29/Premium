import os
from dotenv import load_dotenv

load_dotenv()

# Telegram Configuration
TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN', '')
TELEGRAM_ADMIN_ID = int(os.getenv('TELEGRAM_ADMIN_ID', '0'))

# OpenAI Configuration
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY', '')
OPENAI_MODEL = os.getenv('OPENAI_MODEL', 'gpt-3.5-turbo')

# Admin Payment Configuration
ADMIN_CARD_NUMBER = os.getenv('ADMIN_CARD_NUMBER', '9860-****-****-****')
ADMIN_CARD_HOLDER = os.getenv('ADMIN_CARD_HOLDER', 'Admin')
ADMIN_BANK = os.getenv('ADMIN_BANK', 'Humo Bank')

# Bot Configuration
BOT_NAME = "Premium Referat Bot"
BOT_VERSION = "3.0"
MAX_PAGES = 20
MIN_PAGES = 1
DEFAULT_TEMPERATURE = 0.7
DEFAULT_MAX_TOKENS = 4096

# Page Ranges
PAGE_RANGES = {
    '1-5': {
        'name': '📄 1-5 bet',
        'base_price': 10000,  # UZS
        'description': 'Qisqa referat'
    },
    '5-10': {
        'name': '📕 5-10 bet',
        'base_price': 20000,
        'description': 'O\'rta hajmli referat'
    },
    '10-15': {
        'name': '📗 10-15 bet',
        'base_price': 30000,
        'description': 'Katta hajmli referat'
    },
    '15-20': {
        'name': '📘 15-20 bet',
        'base_price': 40000,
        'description': 'Juda katta hajmli referat'
    }
}

# Quality Multipliers by Education Level
QUALITY_MULTIPLIERS = {
    'school': {
        'name': '🎒 Maktab (8-11 sinflar)',
        'multiplier': 1.0,
        'style': 'sodda va tushunarliroq',
        'depth': 'o\'rta'
    },
    'college': {
        'name': '🏫 Kollejj',
        'multiplier': 1.3,
        'style': 'o\'rta darajali',
        'depth': 'chuqur'
    },
    'university': {
        'name': '🎓 Universitet',
        'multiplier': 1.7,
        'style': 'chuqur va ilmiy',
        'depth': 'juda chuqur'
    },
    'master': {
        'name': '📚 Magistratura',
        'multiplier': 2.2,
        'style': 'juda chuqur va tahliliy',
        'depth': 'ekspert darajasi'
    }
}

# Format Multipliers
FORMAT_MULTIPLIERS = {
    'text': {
        'name': '📝 Oddiy matn',
        'multiplier': 1.0,
        'description': 'Sodda matn formatida'
    },
    'structured': {
        'name': '📋 Struktura bilan',
        'multiplier': 1.1,
        'description': 'Sarlavha va ma\'lumotlar bilan'
    },
    'detailed': {
        'name': '✍️ Chuqur tahlili bilan',
        'multiplier': 1.4,
        'description': 'Tahlil, statistika va fikrlar bilan'
    }
}

# Referat Templates
REFERAT_STRUCTURE = {
    'introduction': 'KIRISH',
    'main_parts': 'ASOSIY QISMLAR',
    'conclusion': 'XULOSA',
    'recommendations': 'TAVSIYALAR'
}

# Messages
MESSAGES = {
    'start': """👋 Assalomu alaykum! 

🎓 *Premium Referat Bot*'ga xush kelibsiz!

💎 *Nima xususiyatlari bor:*
✨ Professional referatlar yaratish
📚 Turli ta'lim darajalariga mos
📄 Turli hajmlar (1-20 bet)
💳 Xavfsiz to'lov tizimi
✅ Admin tasdiqlash

━━━━━━━━━━━━━━━━━━

Keling, boshlaylik! 🚀

*Referat mavzusini kiriting:*
""",
    'topic_short': '❌ Mavzu juda qisqa! Kamida 5 ta belgi kiriting.',
    'pages_invalid': '❌ Betlar soni 1 dan 20 gacha bo\'lishi kerak!',
    'pages_not_number': '❌ Faqat raqam kiriting!',
    'generating': '⏳ Referat tayyorlanmoqda...\n\nIltimos, kutib turing (1-3 minut)...',
    'success': '✅ Referat tayyor!',
    'error': '❌ Xato yuz berdi. Qayta harakat qilib ko\'ring.',
    'cancelled': '❌ Bekor qilindi.\n\n/start\'ni bosing.',
    'payment_instruction': '💳 Quyidagi karta raqamiga to\'lov qiling:',
    'payment_waiting': '⏳ Admin tasdiqlashini kutib turyapmiz...',
    'payment_confirmed': '✅ To\'lov tasdiqlandi! Referat tayyorlanmoqda...',
    'payment_rejected': '❌ To\'lov rad etildi. Qayta urinib ko\'ring.'
}

# Currency
CURRENCY = 'UZS'

# Payment status options
PAYMENT_STATUS = {
    'pending': 'Kutib turyapti',
    'confirmed': 'Tasdiqlandi',
    'rejected': 'Rad etildi',
    'completed': 'Tugallandi'
}

