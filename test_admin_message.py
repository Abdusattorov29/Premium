#!/usr/bin/env python3
"""
Admin'ga direktli test xabar yuboring
"""
import os
import asyncio
from dotenv import load_dotenv
from telegram import Bot

load_dotenv()

TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
TELEGRAM_ADMIN_ID = int(os.getenv('TELEGRAM_ADMIN_ID', '0'))

async def send_test_message():
    """Admin'ga test xabar yubor"""
    bot = Bot(token=TELEGRAM_BOT_TOKEN)
    
    print(f"🔍 Tekshirilmoqda:")
    print(f"  Bot Token: {TELEGRAM_BOT_TOKEN[:20]}...")
    print(f"  Admin ID: {TELEGRAM_ADMIN_ID}")
    print()
    
    if not TELEGRAM_BOT_TOKEN or not TELEGRAM_ADMIN_ID:
        print("❌ XATO: Token yoki Admin ID o'rnatilmagan!")
        return
    
    try:
        # Test xabar yubor
        test_message = """
🤖 **TEST XABAR - ADMIN'GA ULANISH TEKSHIRILMOQDA**

Bu xabar admin'ga yuborildi.

Agar buni ko'ryapsiz, bot to'g'ri ishlayapti!

⏰ Test: Shaxs -> Bot -> Admin
"""
        
        print("📤 Xabar yuborilmoqda...")
        message = await bot.send_message(
            chat_id=TELEGRAM_ADMIN_ID,
            text=test_message,
            parse_mode='Markdown'
        )
        
        print(f"✅ MUVAFFAQIYAT! Xabar yuborildi:")
        print(f"   Message ID: {message.message_id}")
        print(f"   Chat ID: {message.chat_id}")
        print(f"   Vaqt: {message.date}")
        
    except Exception as e:
        print(f"❌ XATO: {type(e).__name__}")
        print(f"   Tafsili: {str(e)}")
        print()
        print("🔧 Tekshirib ko'ring:")
        print("  1. Admin ID to'g'ri yozilganmi? (/id botga yuboring)")
        print("  2. Admin botni bloklaganmi?")
        print("  3. Bot token haqiqiymu? (BotFather'da tekshiring)")
        print("  4. Internet ulanishi bormi?")

if __name__ == '__main__':
    asyncio.run(send_test_message())
