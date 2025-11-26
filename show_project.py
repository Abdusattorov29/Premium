#!/usr/bin/env python3
"""
📊 Premium Referat Bot - Loyihani Tavsif
"""

import os
from pathlib import Path

def list_project_files():
    """Loyihaning barcha fayllarini ko'rsatish"""
    
    files_info = {
        "🤖 BOT FAYLLAR": {
            "bot.py": "Asosiy bot - sodda versiya",
            "bot_advanced.py": "Kuchli bot - tugma, tarixcha, formatlar",
            "config.py": "Konfiguratsiya va konstantalar",
            "logger.py": "Logging va statistika modulasi"
        },
        "⚙️ SETUP VA KONFIGURATSIYA": {
            "requirements.txt": "Zarur Python kutubxonalari",
            ".env": "API kalitlari va tavsiflar (YASHIRIN)",
            "Dockerfile": "Docker konteyner",
            "docker-compose.yml": "Docker Compose konfiguratsiyasi"
        },
        "📚 DOKUMENTASIYA": {
            "README.md": "Asosiy yo'riqnoma (Inglizcha)",
            "README_UZ.md": "Toliq yo'riqnoma (O'zbekcha)",
            "SETUP.md": "Ishga tushirish yo'riqnomasi",
            "QUICK_START.txt": "5 minut'da boshlang",
            "FAQ_HELP.md": "Ko'p soraladigan savollar",
            "PROJECT_SUMMARY.md": "Loyiha xulosa"
        },
        "🧪 TEST VA DEBUG": {
            "test_setup.py": "Barcha sozlamalarni tekshirish",
            "check_setup.py": "API kalitlarni tekshirish",
            "bot_activity.json": "Logslar (avtomat yaratiladi)"
        }
    }
    
    total_files = sum(len(v) for v in files_info.values())
    
    print("\n" + "="*70)
    print("  📦 PREMIUM REFERAT BOT - LOYIHA STRUKTURASI")
    print("="*70)
    
    for category, files in files_info.items():
        print(f"\n{category}")
        print("-" * 70)
        for filename, description in files.items():
            path = Path(filename)
            if path.exists():
                size = path.stat().st_size
                print(f"  ✅ {filename:<25} | {description:<30} ({size:>6} B)")
            else:
                print(f"  ⏳ {filename:<25} | {description:<30} (Avtomat yaratiladi)")
    
    print("\n" + "="*70)
    print(f"  Jami: {total_files} fayl")
    print("="*70)
    
    return total_files

def show_quick_commands():
    """Tezkor buyruqlar"""
    print("\n" + "="*70)
    print("  ⚡ TEZKOR BUYRUQLAR")
    print("="*70)
    print("""
  🚀 ISHGA TUSHIRISH:
     python bot_advanced.py

  🧪 TEKSHIRISH:
     python test_setup.py

  📚 DOKUMENTASIYANI O'QISH:
     - QUICK_START.txt      (5 minut'da boshlang)
     - SETUP.md             (Toliq o'rnatish)
     - FAQ_HELP.md          (Muammolar va yechimlar)
     - README_UZ.md         (O'zbekcha yo'riqnoma)

  🔧 SOZLAMALARNI O'RNATISH:
     1. @BotFather orqali token olish
     2. OpenAI API key olish
     3. .env faylida kiriting
     4. pip install -r requirements.txt
     5. python bot_advanced.py

  📊 STATISTIKA:
     Logslar bot_activity.json da saqlanadi
""")
    print("="*70 + "\n")

def show_requirements():
    """Talablar"""
    print("\n" + "="*70)
    print("  📋 TALABLAR")
    print("="*70)
    print("""
  ✅ Talablar:
     • Python 3.8+
     • Telegram Bot Token (@BotFather orqali)
     • OpenAI API Key (platform.openai.com orqali)
     • Internet ulanishi
     • 100MB bo'sh joy

  📦 Kutubxonalar:
     • python-telegram-bot==20.3
     • openai==1.3.0
     • python-dotenv==1.0.0
     • requests==2.31.0

  ☁️ Online Xizmatlar:
     • Telegram API
     • OpenAI API
     • (Opsional) Docker Hub
""")
    print("="*70 + "\n")

def show_next_steps():
    """Keyingi qadam"""
    print("\n" + "="*70)
    print("  ➡️  KEYINGI QADAM")
    print("="*70)
    print("""
  1️⃣  QUICK_START.txt faylini o'qing (5 minut)
  2️⃣  @BotFather'dan Token olish
  3️⃣  OpenAI'dan API Key olish
  4️⃣  .env faylida kiriting
  5️⃣  pip install -r requirements.txt
  6️⃣  python bot_advanced.py
  7️⃣  Telegram'da /start bosing
  8️⃣  Referat yaratishni boshlang! 🎉

  💡 MASLAHAT:
     Birinchi safar o'rnatishda 10-15 minut ketadi.
     Keyingi safalar faqat 30 sekund!
""")
    print("="*70 + "\n")

def main():
    """Asosiy funksiya"""
    
    # Fayllarni ko'rsatish
    list_project_files()
    
    # Tezkor buyruqlar
    show_quick_commands()
    
    # Talablar
    show_requirements()
    
    # Keyingi qadam
    show_next_steps()
    
    # Yakuniy xabar
    print("\n" + "="*70)
    print("  ✨ TAYYOR! Bot'ni ishga tushirishga tayyorlar!")
    print("="*70 + "\n")

if __name__ == '__main__':
    main()
