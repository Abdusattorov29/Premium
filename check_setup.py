"""
Simple test bot for development
"""
import os
from dotenv import load_dotenv

load_dotenv()

print("=" * 60)
print("🔍 TELEGRAM BOT - SOZLAMALARNI TEKSHIRISH")
print("=" * 60)

# Check Telegram Bot Token
telegram_token = os.getenv('TELEGRAM_BOT_TOKEN')
if telegram_token and telegram_token != 'your_telegram_bot_token_here':
    print(f"✅ TELEGRAM_BOT_TOKEN: {telegram_token[:20]}... (Mavjud)")
else:
    print(f"❌ TELEGRAM_BOT_TOKEN: YO'Q YOKI TO'LIQ BO'LMAY QOLGAN")

# Check OpenAI API Key
openai_key = os.getenv('OPENAI_API_KEY')
if openai_key and openai_key != 'your_openai_api_key_here':
    print(f"✅ OPENAI_API_KEY: {openai_key[:20]}... (Mavjud)")
else:
    print(f"❌ OPENAI_API_KEY: YO'Q YOKI TO'LIQ BO'LMAY QOLGAN")

print("\n" + "=" * 60)
print("📦 KUTUBXONALARNI TEKSHIRISH")
print("=" * 60)

# Check required packages
packages = {
    'telegram': 'python-telegram-bot',
    'openai': 'openai',
    'dotenv': 'python-dotenv',
    'requests': 'requests'
}

installed = []
not_installed = []

for module, package_name in packages.items():
    try:
        __import__(module)
        installed.append(f"✅ {package_name}")
    except ImportError:
        not_installed.append(f"❌ {package_name}")

for item in installed:
    print(item)

if not_installed:
    print("\n⚠️  YO'Q KUTUBXONALAR:")
    for item in not_installed:
        print(item)
    print("\n💡 O'RNATISH UCHUN BUYRUQ:")
    print("pip install -r requirements.txt")

print("\n" + "=" * 60)
print("📋 FAYLLAR MAVJUDLIGI")
print("=" * 60)

files = ['bot.py', 'bot_advanced.py', '.env', 'requirements.txt', 'config.py']
for file in files:
    if os.path.exists(file):
        print(f"✅ {file}")
    else:
        print(f"❌ {file}")

print("\n" + "=" * 60)
print("✨ TEKSHIRISH TUGADI")
print("=" * 60)

if telegram_token and openai_key and all(os.path.exists(f) for f in files):
    print("\n✅ HAMMASI TAYYOR! Bot'ni ishga tushirishga tayyorlar:")
    print("   python bot_advanced.py")
else:
    print("\n⚠️  Ba'zi narsalar TO'LIQMAS. SETUP.md faylini o'qing.")
