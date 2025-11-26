import os
import logging
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    filters,
    ContextTypes,
    ConversationHandler
)
from openai import OpenAI

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Initialize API clients
TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
client = OpenAI(api_key=OPENAI_API_KEY)

# Conversation states
TOPIC, LEVEL, PAGES = range(3)

class ReferatBot:
    def __init__(self):
        self.user_data = {}
    
    async def start(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
        """Start the bot and ask for topic"""
        user_id = update.effective_user.id
        self.user_data[user_id] = {}
        
        welcome_text = """
👋 Assalomu alaykum! Referat yasaydigan bot'ga xush kelibsiz!

Men sizga har qanday mavzu bo'yicha referat yozib beraman.

🎓 Ishni boshlash uchun:
1️⃣ Referat mavzusini kiriting
2️⃣ Ta'lim darajasini tanlang
3️⃣ Betlar sonini ko'rsating

Keling, boshlaylik! 📚

Referat mavzusini kiriting:
        """
        await update.message.reply_text(welcome_text)
        return TOPIC
    
    async def get_topic(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
        """Get the topic from user"""
        user_id = update.effective_user.id
        topic = update.message.text.strip()
        
        if len(topic) < 5:
            await update.message.reply_text("❌ Mavzu juda qisqa! Kamida 5 ta belgi kiriting.")
            return TOPIC
        
        self.user_data[user_id]['topic'] = topic
        
        level_text = """
🎓 Ta'lim darajasini tanlang:

1️⃣ Maktab (8-11 sinflar)
2️⃣ Kollejj
3️⃣ Universitet
4️⃣ Magistratura

Raqamni kiriting (1-4):
        """
        await update.message.reply_text(level_text)
        return LEVEL
    
    async def get_level(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
        """Get education level"""
        user_id = update.effective_user.id
        level_choice = update.message.text.strip()
        
        levels = {
            '1': 'maktab',
            '2': 'kollejj',
            '3': 'universitet',
            '4': 'magistratura'
        }
        
        if level_choice not in levels:
            await update.message.reply_text("❌ Faqat 1, 2, 3 yoki 4 raqamni kiriting!")
            return LEVEL
        
        self.user_data[user_id]['level'] = levels[level_choice]
        
        pages_text = """
📄 Referat nechi betdan iborat bo'lishi kerak?

Betlar sonini kiriting (3-50):
        """
        await update.message.reply_text(pages_text)
        return PAGES
    
    async def get_pages(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
        """Get number of pages and generate referat"""
        user_id = update.effective_user.id
        
        try:
            pages = int(update.message.text.strip())
            if pages < 3 or pages > 50:
                await update.message.reply_text("❌ Betlar soni 3 dan 50 gacha bo'lishi kerak!")
                return PAGES
        except ValueError:
            await update.message.reply_text("❌ Faqat raqam kiriting!")
            return PAGES
        
        self.user_data[user_id]['pages'] = pages
        
        # Show processing message
        await update.message.reply_text("⏳ Referat tayyorlanmoqda... Iloji boricha kutib turing (1-3 minut)...")
        
        # Generate referat
        referat = await self.generate_referat(
            topic=self.user_data[user_id]['topic'],
            level=self.user_data[user_id]['level'],
            pages=pages
        )
        
        # Send referat
        if referat:
            await update.message.reply_text(referat)
            
            # Ask if user wants to save as file
            await update.message.reply_text(
                "✅ Referat tayyor! Faylga saqlash uchun /save buyrug'ini yozing yoki yangi referat yaratish uchun /start'ni bosing."
            )
        else:
            await update.message.reply_text(
                "❌ Xato yuz berdi. Iltimos, qayta harakat qilib ko'ring. /start'ni bosing."
            )
        
        return ConversationHandler.END
    
    async def generate_referat(self, topic: str, level: str, pages: int) -> str:
        """Generate referat using OpenAI"""
        try:
            prompt = f"""
Siz professional o'zbekcha referat yozuvchisiz. Quyidagi ma'lumotlar bo'yicha chuqur, maqolali va ta'lim darajasiga mos referat yozing:

Mavzu: {topic}
Ta'lim darajasi: {level}
Taxminiy hajmi: {pages} bet (~{pages * 250} so'z)

Referat quyidagi strukturaga mos bo'lishi kerak:
1. Kirish (muammaning dolzarbligi, maqsad va vazifalari)
2. Asosiy qismlar (3-4 ta bo'lim)
3. Natija va xulosa
4. Tavsiyalar

Talabalar:
- Professional va baland sifatli matn
- Mavzu bilan bog'liq misollar va faktlar
- Tahlili va o'z fikrlar
- Qaynashli va aniq matn
- O'zbekcha til qoidalariga mos

Referat matni:
"""
            
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                temperature=0.7,
                max_tokens=3000
            )
            
            return response.choices[0].message.content
        
        except Exception as e:
            logger.error(f"Xato: {str(e)}")
            return None
    
    async def cancel(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
        """Cancel operation"""
        await update.message.reply_text(
            "❌ Bekor qilindi. /start'ni bosing yangi referat yaratish uchun."
        )
        return ConversationHandler.END
    
    async def help_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        """Send help message"""
        help_text = """
📚 Referat Bot - Yordam

🤖 Bot nima qila oladi:
• Har qanday mavzu bo'yicha referat yaratish
• Turli ta'lim darajalariga mos referatlar
• Sozlanadigan betlar soni
• PDF formatda yuklab olish

📋 Buyruqlar:
/start - Yangi referat yaratish
/help - Yordam ko'rish
/cancel - Bekor qilish

💡 Maslahatlar:
- Mavsuni aniq va batafsil kiriting
- Ta'lim darajasini to'g'ri tanlang
- Betlar sonini qarama-qarshicha o'ylang

❓ Savol bo'lsa: @admin_username ga murojaat qiling
        """
        await update.message.reply_text(help_text)

def main() -> None:
    """Start the bot"""
    if not TELEGRAM_BOT_TOKEN:
        logger.error("TELEGRAM_BOT_TOKEN muhit o'zgaruvchisida o'rnatilmagan!")
        return
    
    if not OPENAI_API_KEY:
        logger.error("OPENAI_API_KEY muhit o'zgaruvchisida o'rnatilmagan!")
        return
    
    # Create application
    application = Application.builder().token(TELEGRAM_BOT_TOKEN).build()
    bot = ReferatBot()
    
    # Conversation handler
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler("start", bot.start)],
        states={
            TOPIC: [MessageHandler(filters.TEXT & ~filters.COMMAND, bot.get_topic)],
            LEVEL: [MessageHandler(filters.TEXT & ~filters.COMMAND, bot.get_level)],
            PAGES: [MessageHandler(filters.TEXT & ~filters.COMMAND, bot.get_pages)],
        },
        fallbacks=[CommandHandler("cancel", bot.cancel)],
    )
    
    # Add handlers
    application.add_handler(conv_handler)
    application.add_handler(CommandHandler("help", bot.help_command))
    
    # Start bot
    logger.info("Bot ishga tushmoqda...")
    application.run_polling()

if __name__ == '__main__':
    main()
