#!/usr/bin/env python3
"""
🤖 Premium Referat Bot - Test Script
Bu script bot'ning barcha sozlamalarini tekshiradi
"""

import os
import sys
from pathlib import Path

def print_header(text):
    """Sarlavha chop qilish"""
    print("\n" + "=" * 70)
    print(f"  {text}")
    print("=" * 70)

def check_file(filename):
    """Fayl mavjudligini tekshirish"""
    if os.path.exists(filename):
        size = os.path.getsize(filename)
        print(f"  ✅ {filename:<30} ({size} bytes)")
        return True
    else:
        print(f"  ❌ {filename:<30} YO'Q!")
        return False

def check_env():
    """Environment o'zgaruvchilarini tekshirish"""
    print_header("🔐 ENVIRONMENT O'ZGARUVCHILARI")
    
    from dotenv import load_dotenv
    load_dotenv()
    
    checks = {
        'TELEGRAM_BOT_TOKEN': os.getenv('TELEGRAM_BOT_TOKEN'),
        'OPENAI_API_KEY': os.getenv('OPENAI_API_KEY')
    }
    
    for var, value in checks.items():
        if value and value != f'your_{var.lower()}_here':
            print(f"  ✅ {var:<25} (To'liq)")
        else:
            print(f"  ❌ {var:<25} (TO'LIQ BO'LMAY QOLGAN)")
    
    return all(
        v and v != f'your_{k.lower()}_here' 
        for k, v in checks.items()
    )

def check_packages():
    """Kutubxonalarni tekshirish"""
    print_header("📦 KUTUBXONALAR")
    
    packages = [
        ('telegram', 'python-telegram-bot'),
        ('openai', 'openai'),
        ('dotenv', 'python-dotenv'),
        ('requests', 'requests')
    ]
    
    all_installed = True
    for module, display_name in packages:
        try:
            __import__(module)
            print(f"  ✅ {display_name:<25} Installed")
        except ImportError:
            print(f"  ❌ {display_name:<25} NOT INSTALLED")
            all_installed = False
    
    return all_installed

def check_files():
    """Zarur fayllarni tekshirish"""
    print_header("📁 FAYLLAR")
    
    required_files = [
        'bot.py',
        'bot_advanced.py',
        'config.py',
        '.env',
        'requirements.txt',
        'logger.py'
    ]
    
    results = []
    for filename in required_files:
        results.append(check_file(filename))
    
    return all(results)

def check_syntax():
    """Bot fayllarining sintaksisini tekshirish"""
    print_header("🐍 PYTHON SINTAKSISI")
    
    import py_compile
    
    files_to_check = ['bot.py', 'bot_advanced.py', 'config.py', 'logger.py']
    all_ok = True
    
    for filename in files_to_check:
        try:
            py_compile.compile(filename, doraise=True)
            print(f"  ✅ {filename:<25} Syntax OK")
        except py_compile.PyCompileError as e:
            print(f"  ❌ {filename:<25} Syntax Error!")
            print(f"     {str(e)}")
            all_ok = False
    
    return all_ok

def print_results(env_ok, packages_ok, files_ok, syntax_ok):
    """Natijalarni ko'rsatish"""
    print_header("📊 YAKUNIY NATIJA")
    
    print(f"  Environment:     {'✅ OK' if env_ok else '❌ MUAMMO'}")
    print(f"  Kutubxonalar:    {'✅ OK' if packages_ok else '❌ MUAMMO'}")
    print(f"  Fayllar:         {'✅ OK' if files_ok else '❌ MUAMMO'}")
    print(f"  Sintaksis:       {'✅ OK' if syntax_ok else '❌ MUAMMO'}")
    
    all_ok = env_ok and packages_ok and files_ok and syntax_ok
    
    print("\n" + "=" * 70)
    if all_ok:
        print("  🎉 HAMMASI TAYYOR! Bot'ni ishga tushirishga tayyor:")
        print("     python bot_advanced.py")
    else:
        print("  ⚠️  Ba'zi muammolar bor. Iltimos, quyidagini o'qing:")
        print("     - SETUP.md - To'liq o'rnatish yo'riqnomasi")
        print("     - QUICK_START.txt - Tezkor boshlanish")
    print("=" * 70 + "\n")
    
    return all_ok

def main():
    """Asosiy funksiya"""
    print("\n")
    print("  🤖 PREMIUM REFERAT BOT - TEKSHIRISH")
    print("  Version: 2.0")
    print("  Copyright © 2025")
    
    # Tekshiruvlarni o'tkazish
    env_ok = check_env()
    packages_ok = check_packages()
    files_ok = check_files()
    syntax_ok = check_syntax()
    
    # Natijalarni ko'rsatish
    all_ok = print_results(env_ok, packages_ok, files_ok, syntax_ok)
    
    # Chiqish kodi
    sys.exit(0 if all_ok else 1)

if __name__ == '__main__':
    main()
