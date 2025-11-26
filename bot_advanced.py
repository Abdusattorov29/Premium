import sys
import os

print("=== RAILWAY DEBUG ===")
print("Current working directory:", os.getcwd())
print("Script location:", os.path.dirname(os.path.abspath(__file__)))
print("Python path:", sys.path)
print("Files in directory:")
for file in os.listdir('.'):
    if file.endswith('.py'):
        print(f"  - {file}")
print("=====================")

# payment_system mavjudligini tekshirish
payment_system_path = './payment_system.py'
if os.path.exists(payment_system_path):
    print("✅ payment_system.py FOUND")
else:
    print("❌ payment_system.py NOT FOUND")
    print("Available .py files:", [f for f in os.listdir('.') if f.endswith('.py')])


import os
import logging
from dotenv import load_dotenv
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, File
from telegram.request import HTTPXRequest
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    CallbackQueryHandler,
    filters,
    ContextTypes,
    ConversationHandler
)
from openai import OpenAI
import json
from datetime import datetime
from typing import Dict, Optional, List
from payment_system import PricingSystem, PaymentTracker, AdminCard

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
TELEGRAM_ADMIN_ID = int(os.getenv('TELEGRAM_ADMIN_ID', '0'))
client = OpenAI(api_key=OPENAI_API_KEY)

# Conversation states
TOPIC, LEVEL, PAGE_RANGE, PAGE_COUNT, FORMAT, WORK_TYPE, ADDITIONAL_INFO, PAYMENT_CONFIRMATION = range(8)

# Work type options
WORK_TYPES = {
    'referat': {'name': '📝 Referat', 'icon': '📝'},
    'presentation': {'name': '🎬 Taqdimot (Presentation)', 'icon': '🎬'},
    'independent_work': {'name': '✍️ Mustaqil Ish', 'icon': '✍️'}
}

# Initialize services
pricing_system = PricingSystem()
payment_tracker = PaymentTracker()
admin_card = AdminCard()

class ReferatBot:
    def __init__(self):
        self.user_data = {}
        self.user_history = {}
        self.active_payments = {}  # payment_id -> user_id
        self.last_openai_error: Optional[str] = None
    
    async def start(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
        """Start the bot and ask for topic"""
        user_id = update.effective_user.id
        username = update.effective_user.first_name or "User"
        
        self.user_data[user_id] = {}
        
        if user_id not in self.user_history:
            self.user_history[user_id] = []
        
        welcome_text = f"""
👋 Assalomu alaykum, {username}! 

🎓 *Premium Referat Bot*'ga xush kelibsiz!

💎 *Nima xususiyatlari bor:*
✨ Professional referatlar yaratish
📚 Turli ta'lim darajalariga mos (Maktab, Kollejj, Universitet, Magistratura)
📄 Turli hajmlar (1-20 bet)
💳 Xavfsiz to'lov tizimi
✅ Admin tasdiqlash

━━━━━━━━━━━━━━━━━━

*Referat mavzusini kiriting:*
(Masalan: O'zbekistonning tarixiy rivojlanishi, Informatika, Biologiya, va hokazo)
        """
        await update.message.reply_text(welcome_text, parse_mode='Markdown')
        return TOPIC
    
    async def get_topic(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
        """Get the topic from user"""
        user_id = update.effective_user.id
        topic = update.message.text.strip()
        
        if len(topic) < 5:
            await update.message.reply_text(
                "❌ Mavzu juda qisqa! Kamida 5 ta belgi kiriting.\n\nQayta urinib ko'ring:"
            )
            return TOPIC
        
        self.user_data[user_id]['topic'] = topic
        
        # Create inline keyboard for work type selection
        keyboard = [
            [InlineKeyboardButton("📝 Referat", callback_data='worktype_referat')],
            [InlineKeyboardButton("🎬 Taqdimot (Presentation)", callback_data='worktype_presentation')],
            [InlineKeyboardButton("✍️ Mustaqil Ish", callback_data='worktype_independent_work')]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        
        await update.message.reply_text(
            f"✅ Mavzu: *{topic}*\n\n📚 Endi ishning turini tanlang:",
            reply_markup=reply_markup,
            parse_mode='Markdown'
        )
        return WORK_TYPE
    
    async def get_level(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
        """Handle level selection"""
        query = update.callback_query
        await query.answer()
        user_id = query.from_user.id
        
        level_map = {
            'level_school': ('school', '🎒 Maktab (8-11 sinflar)'),
            'level_college': ('college', '🏫 Kollejj'),
            'level_university': ('university', '🎓 Universitet'),
            'level_master': ('master', '📚 Magistratura')
        }
        
        level_code, level_name = level_map[query.data]
        self.user_data[user_id]['level'] = level_code
        self.user_data[user_id]['level_name'] = level_name
        
        # Create inline keyboard for page ranges
        keyboard = [
            [InlineKeyboardButton("📄 1-5 bet", callback_data='range_1-5')],
            [InlineKeyboardButton("📕 5-10 bet", callback_data='range_5-10')],
            [InlineKeyboardButton("📗 10-15 bet", callback_data='range_10-15')],
            [InlineKeyboardButton("📘 15-20 bet", callback_data='range_15-20')]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        
        await query.edit_message_text(
            f"✅ Ta'lim darajasi: {level_name}\n\n"
            f"📄 Ishning nechi betdan iborat bo'lishi kerak?\n\n"
            "Diapazoni tanlang:",
            reply_markup=reply_markup
        )
        
        return PAGE_RANGE

    async def get_work_type(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
        """Handle work type selection"""
        query = update.callback_query
        await query.answer()
        user_id = query.from_user.id
        
        worktype_map = {
            'worktype_referat': ('referat', '📝 Referat'),
            'worktype_presentation': ('presentation', '🎬 Taqdimot (Presentation)'),
            'worktype_independent_work': ('independent_work', '✍️ Mustaqil Ish')
        }
        
        worktype_code, worktype_name = worktype_map[query.data]
        self.user_data[user_id]['work_type'] = worktype_code
        self.user_data[user_id]['work_type_name'] = worktype_name
        
        # Create inline keyboard for level selection
        keyboard = [
            [InlineKeyboardButton("🎒 Maktab (8-11 sinflar)", callback_data='level_school')],
            [InlineKeyboardButton("🏫 Kollejj", callback_data='level_college')],
            [InlineKeyboardButton("🎓 Universitet", callback_data='level_university')],
            [InlineKeyboardButton("📚 Magistratura", callback_data='level_master')]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        
        await query.edit_message_text(
            f"✅ Ish turi: {worktype_name}\n\n"
            f"🎓 Endi ta'lim darajasini tanlang:",
            reply_markup=reply_markup
        )
        
        return LEVEL
    
    async def get_page_range(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
        """Handle page range selection"""
        query = update.callback_query
        await query.answer()
        user_id = query.from_user.id
        
        range_map = {
            'range_1-5': ('1-5', 3),
            'range_5-10': ('5-10', 7),
            'range_10-15': ('10-15', 12),
            'range_15-20': ('15-20', 18)
        }
        
        range_code, default_pages = range_map[query.data]
        self.user_data[user_id]['page_range'] = range_code
        self.user_data[user_id]['default_pages'] = default_pages
        
        min_page, max_page = map(int, range_code.split('-'))
        
        await query.edit_message_text(
            f"✅ Diapazon: {range_code} bet\n\n"
            f"📝 Aniq nechta bet kerak? ({min_page}-{max_page} oralig'ida)\n\n"
            f"Raqam kiriting:"
        )
        
        return PAGE_COUNT
    
    async def get_page_count(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
        """Get exact page count"""
        user_id = update.effective_user.id
        
        try:
            pages = int(update.message.text.strip())
            page_range = self.user_data[user_id]['page_range']
            min_page, max_page = map(int, page_range.split('-'))
            
            if pages < min_page or pages > max_page:
                await update.message.reply_text(
                    f"❌ Betlar soni {min_page}-{max_page} oralig'ida bo'lishi kerak!\n\nQayta kiriting:"
                )
                return PAGE_COUNT
        except ValueError:
            await update.message.reply_text(
                "❌ Faqat raqam kiriting!\n\nMasalan: 5, 10, 15"
            )
            return PAGE_COUNT
        
        self.user_data[user_id]['pages'] = pages
        
        # Create format selection keyboard
        keyboard = [
            [InlineKeyboardButton("📝 Oddiy matn", callback_data='format_text')],
            [InlineKeyboardButton("📋 Struktura bilan", callback_data='format_structured')],
            [InlineKeyboardButton("✍️ Chuqur tahlili bilan", callback_data='format_detailed')]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        
        await update.message.reply_text(
            f"✅ Betlar soni: {pages}\n\n"
            f"📖 Referatning formatini tanlang:",
            reply_markup=reply_markup
        )
        
        return FORMAT
    
    async def get_format(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
        """Handle format selection and show pricing"""
        query = update.callback_query
        await query.answer()
        user_id = query.from_user.id
        
        format_map = {
            'format_text': ('text', '📝 Oddiy matn'),
            'format_structured': ('structured', '📋 Struktura bilan'),
            'format_detailed': ('detailed', '✍️ Chuqur tahlili bilan')
        }
        
        format_type, format_name = format_map[query.data]
        self.user_data[user_id]['format'] = format_type
        self.user_data[user_id]['format_name'] = format_name
        
        # Check if additional info needed (for presentation and independent work)
        work_type = self.user_data[user_id]['work_type']
        
        if work_type in ['presentation', 'independent_work']:
            # Ask for additional information
            await query.edit_message_text(
                "📋 *Qo'shimcha Ma'lumotlar Kerak*\n\n"
                "Iltimos, quyidagi ma'lumotlarni kiriting (ketma-ket):\n\n"
                "1️⃣ *Universitet/Maktab/Kollejj nomi*\n"
                "(Masalan: Tashkent Axborot Texnologiyalari Universiteti)",
                parse_mode='Markdown'
            )
            return ADDITIONAL_INFO
        else:
            # For referat, go directly to pricing
            return await self._show_pricing(query, user_id)
    
    async def _show_pricing(self, query, user_id: int) -> int:
        """Show pricing information"""
        pages = self.user_data[user_id]['pages']
        level = self.user_data[user_id]['level']
        work_type = self.user_data[user_id]['work_type']
        format_type = self.user_data[user_id]['format']
        format_name = self.user_data[user_id]['format_name']
        
        price_info = pricing_system.calculate_price(pages, level, format_type, work_type)
        
        # Show pricing and ask for confirmation
        work_type_name = self.user_data[user_id]['work_type_name']
        
        price_text = f"""
💰 *NARX HISOBOTI*

📊 *Sizning tanlashingiz:*
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 Mavzu: {self.user_data[user_id]['topic']}
📚 Ish turi: {work_type_name}
🎓 Ta'lim darajasi: {self.user_data[user_id]['level_name']}
📄 Betlar soni: {pages} ta
📋 Format: {format_name}
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

💵 *Narx hisoboti:*
• Asosiy narx: {price_info['base_price']:,} UZS
• Sifat koeffitsiyenti: x{price_info['quality_multiplier']}
• Format koeffitsiyenti: x{price_info['format_multiplier']}
• Ish turi koeffitsiyenti: x{price_info.get('worktype_multiplier', 1.0)}
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
💳 *JAMI: {price_info['final_price']:,} UZS*
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

✅ Tasdiqlaysizmi?
        """
        
        keyboard = [
            [InlineKeyboardButton("✅ Ha, to'lov qilaman", callback_data='payment_confirm')],
            [InlineKeyboardButton("❌ Bekor qilish", callback_data='payment_cancel')]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        
        self.user_data[user_id]['price_info'] = price_info
        
        await query.edit_message_text(price_text, reply_markup=reply_markup, parse_mode='Markdown')
        
        return PAYMENT_CONFIRMATION
    
    async def get_additional_info(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
        """Get additional information for presentation and independent work"""
        user_id = update.effective_user.id
        work_type = self.user_data[user_id]['work_type']
        
        if 'step' not in self.user_data[user_id]:
            # Step 1: University/Institute name
            self.user_data[user_id]['university_name'] = update.message.text.strip()
            self.user_data[user_id]['step'] = 1
            
            await update.message.reply_text(
                "2️⃣ *O'quvchining ismi va familiyasi*\n\n"
                "Masalan: Sardor Alimov"
            )
            return ADDITIONAL_INFO
        
        elif self.user_data[user_id]['step'] == 1:
            # Step 2: Student name
            self.user_data[user_id]['student_name'] = update.message.text.strip()
            self.user_data[user_id]['step'] = 2
            
            await update.message.reply_text(
                "3️⃣ *O'qituvchi (Mudavvir) ismi va familiyasi*\n\n"
                "Masalan: Prof. Dr. Xasan Karimov"
            )
            return ADDITIONAL_INFO
        
        elif self.user_data[user_id]['step'] == 2:
            # Step 3: Teacher name
            self.user_data[user_id]['teacher_name'] = update.message.text.strip()
            self.user_data[user_id]['step'] = None
            
            # Now show pricing
            # Create a fake query object for _show_pricing
            class FakeQuery:
                async def edit_message_text(self, text, reply_markup=None, parse_mode=None):
                    await update.message.reply_text(text, reply_markup=reply_markup, parse_mode=parse_mode)
            
            fake_query = FakeQuery()
            return await self._show_pricing(fake_query, user_id)
    
    async def handle_payment_decision(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
        """Handle payment confirmation or cancellation"""
        query = update.callback_query
        await query.answer()
        user_id = query.from_user.id
        username = query.from_user.username or query.from_user.first_name
        
        if query.data == 'payment_cancel':
            await query.edit_message_text(
                "❌ Bekor qilindi.\n\n/start'ni bosing yangi referat yaratish uchun."
            )
            return ConversationHandler.END
        
        # Create payment record
        payment = payment_tracker.create_payment(
            user_id=user_id,
            username=username,
            amount=self.user_data[user_id]['price_info']['final_price'],
            topic=self.user_data[user_id]['topic'],
            level=self.user_data[user_id]['level'],
            pages=self.user_data[user_id]['pages'],
            format_type=self.user_data[user_id]['format'],
            work_type=self.user_data[user_id]['work_type'],
            university_name=self.user_data[user_id].get('university_name', ''),
            student_name=self.user_data[user_id].get('student_name', ''),
            teacher_name=self.user_data[user_id].get('teacher_name', '')
        )
        
        self.active_payments[payment['payment_id']] = user_id
        self.user_data[user_id]['payment_id'] = payment['payment_id']
        
        # Send payment instruction
        payment_instruction = admin_card.get_payment_instruction()
        
        await query.edit_message_text(
            payment_instruction
        )
        
        # Send invoice-like message
        invoice_text = f"""
📋 *TO'LOV QUITI*

🆔 To'lov ID: `{payment['payment_id']}`
💳 Summa: {payment['amount']:,} UZS
👤 Foydalanuvchi: @{username}
📌 Mavzu: {payment['topic']}
🎓 Darajasi: {payment['level']}
📄 Betlar: {payment['pages']}

⏰ Yaratilgan: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}

✅ Chekni yuborganingizdan keyin biroz kutib turing!
        """
        
        await query.message.reply_text(invoice_text)
        
        await query.message.reply_text(
            "📸 Endi chekni yuboring:\n\n"
            "Kartadan to'lov chekining rasmini yuboring.\n"
            "Admin 5 daqiqa ichida tasdiqlab javob beradi."
        )
        
        return PAYMENT_CONFIRMATION
    
    async def receive_payment_receipt(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
        """Receive payment receipt from user"""
        user_id = update.effective_user.id
        
        if user_id not in self.user_data or 'payment_id' not in self.user_data[user_id]:
            await update.message.reply_text(
                "❌ Avval /start'ni bosib referat tanlovini tugatilishini kutamiz."
            )
            return ConversationHandler.END
        
        payment_id = self.user_data[user_id]['payment_id']
        payment = payment_tracker.get_payment(payment_id)
        
        # Save receipt photo
        if update.message.photo:
            photo = update.message.photo[-1]
            receipt_data = {
                'amount': payment['amount'],
                'timestamp': datetime.now().isoformat(),
                'photo_file_id': photo.file_id
            }
            
            self.user_data[user_id]['receipt_data'] = receipt_data
            
            # Send to admin for confirmation
            await self.send_to_admin_for_approval(context, payment, photo.file_id, user_id)
            
            await update.message.reply_text(
                "✅ Chek qabul qilindi!\n\n"
                "Admin onlayn kutmoqda... (Odatda 5 daqiqa)"
            )
            
            return ConversationHandler.END
        else:
            await update.message.reply_text(
                "❌ Iltimos, rasim yuboring (chek rasimi).\n\n"
                "Screenshot yoki rasmni yuboring:"
            )
            return PAYMENT_CONFIRMATION
    
    async def send_to_admin_for_approval(self, context: ContextTypes.DEFAULT_TYPE, 
                                        payment: Dict, photo_file_id: str, user_id: int) -> None:
        """Send payment receipt to admin for approval"""
        
        if not TELEGRAM_ADMIN_ID:
            logger.warning("Admin ID o'rnatilmagan!")
            return
        
        username = payment['username'] or f"User {user_id}"
        
        approval_text = f"""
🔔 *YANGI TO'LOV TASDIQLANISHI KERAK*

👤 *Foydalanuvchi ma'lumotlari:*
├ Telegram ID: `{user_id}`
├ Foydalanuvchi: @{username}
└ Sana: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}

💳 *To'lov ma'lumotlari:*
├ To'lov ID: `{payment['payment_id']}`
├ Summa: {payment['amount']:,} UZS
└ Status: KUTIB TURYAPTI

📚 *Referat ma'lumotlari:*
├ Mavzu: {payment['topic']}
├ Darajasi: {payment['level']}
├ Betlar: {payment['pages']}
└ Format: {payment['format']}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📸 To'lov chekini tekshiring (rasmda ko'rish mumkin).

Quyidagi tugmalardan birini bosing:
        """
        
        keyboard = [
            [
                InlineKeyboardButton("✅ Tasdiqlash", callback_data=f'admin_approve_{payment["payment_id"]}'),
                InlineKeyboardButton("❌ Rad etish", callback_data=f'admin_reject_{payment["payment_id"]}')
            ]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        
        try:
            # Send message with photo (plain text caption to avoid entity parse errors)
            await context.bot.send_photo(
                chat_id=TELEGRAM_ADMIN_ID,
                photo=photo_file_id,
                caption=approval_text,
                reply_markup=reply_markup,
            )
        except Exception as e:
            logger.error(f"Admin'ga xabar yuborishda xato: {str(e)}")
    
    async def admin_approve_payment(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        """Admin approve payment"""
        query = update.callback_query
        await query.answer()

        # Extract payment_id from callback
        payment_id = query.data.replace('admin_approve_', '')
        payment = payment_tracker.get_payment(payment_id)

        if not payment:
            logger.error(f"❌ To'lov topilmadi: {payment_id}")
            await query.answer("❌ To'lov topilmadi!", show_alert=True)
            return

        # Update payment status
        payment_tracker.update_payment_status(payment_id, 'confirmed')

        user_id = payment['user_id']
        logger.info(f"✅ To'lov tasdiqlandi: payment_id={payment_id}, user_id={user_id}")

        # Generate referat
        referat = await self.generate_referat(
            topic=payment['topic'],
            level=payment['level'],
            pages=payment['pages'],
            format_type=payment['format'],
            work_type=payment.get('work_type', 'referat')
        )

        if not referat:
            # Generation failed — notify admin and user
            err = self.last_openai_error or 'Unknown error'
            logger.error(f"❌ Referat yaratishda xato: {err} (payment_id={payment_id})")
            try:
                await context.bot.send_message(
                    chat_id=TELEGRAM_ADMIN_ID,
                    text=(f"⚠️ Referat yaratishda xato.\n"
                          f"To'lov ID: {payment_id}\n"
                          f"User: @{payment.get('username')}\n"
                          f"Xato: {err}"),
                )
            except Exception:
                logger.exception("Adminga xato haqida xabar yuborishda xato")

            # Inform user
            try:
                await context.bot.send_message(
                    chat_id=user_id,
                    text=("❌ Serverda xatolik yuz berdi va referat yaratib bo'lmadi."
                          " Iltimos, birozdan so'ng qayta urinib ko'ring."),
                )
            except Exception:
                logger.exception("Foydalanuvchiga xato haqida xabar yuborishda xato")

            # Update payment status to failed
            payment_tracker.update_payment_status(payment_id, 'failed', 'Referat yaratilmadi')

            # Update admin message (either caption or text)
            confirm_text = f"❌ Referat yaratishda xato!\nTo'lov ID: {payment_id}\nXato: {err}"
            try:
                if query.message and (getattr(query.message, 'photo', None) or getattr(query.message, 'document', None)):
                    await query.edit_message_caption(confirm_text)
                else:
                    await query.edit_message_text(confirm_text)
            except Exception:
                logger.exception("Admin xabarini yangilashda xato")

            return

        # If referat generated, send it to the user
        try:
            chunks = [referat[i:i+4000] for i in range(0, len(referat), 4000)]
            for chunk in chunks:
                await context.bot.send_message(chat_id=user_id, text=chunk)

            # Success message to user
            try:
                await context.bot.send_message(
                    chat_id=user_id,
                    text=("✅ REFERAT TAYYOR!\n\n"
                          "Sizning referatingiz tayyor va yuborildi.\n"
                          "Dars o'qituvchiga bering va 5 ballik baholang! 🌟\n\n"
                          "/start - yangi referat yaratish"),
                )
            except Exception:
                logger.exception("Foydalanuvchiga muvaffaqiyat xabarini yuborishda xato")

            # Update admin message (either caption or text)
            confirm_text = f"✅ To'lov tasdiqlandi!\nTo'lov ID: {payment_id}\nUser: @{payment.get('username')}\nReferat yuborildi."
            try:
                if query.message and (getattr(query.message, 'photo', None) or getattr(query.message, 'document', None)):
                    await query.edit_message_caption(confirm_text)
                else:
                    await query.edit_message_text(confirm_text)
            except Exception:
                logger.exception("Admin xabarini yangilashda xato")

            logger.info(f"✅ Referat muvaffaqiyatli yuborildi: user_id={user_id}")

        except Exception as e:
            logger.error(f"❌ Referatni yuborishda xato: {str(e)}", exc_info=True)
            await query.answer(f"❌ Xato: {str(e)}", show_alert=True)
    
    async def admin_reject_payment(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        """Admin reject payment"""
        query = update.callback_query
        await query.answer()
        
        payment_id = query.data.replace('admin_reject_', '')
        payment = payment_tracker.get_payment(payment_id)
        
        if not payment:
            await query.answer("❌ To'lov topilmadi!", show_alert=True)
            return
        
        # Update payment status
        payment_tracker.update_payment_status(payment_id, 'rejected', 'Chek tasdiqlanmadi')
        
        user_id = payment['user_id']
        
        try:
            # Inform user (plain text)
            await context.bot.send_message(
                chat_id=user_id,
                text=("❌ TO'LOV RAD ETILDI\n\n"
                      "Sizning to'lovingiz tasdiqlanmadi.\n\n"
                      "Sabablari:\n"
                      "• Chekda summa noto'g'ri\n"
                      "• Chekda vaqt ko'rinmaydi\n"
                      "• Boshqa sabab\n\n"
                      "Iltimos, qayta to'lovni urinib ko'ring yoki admin'ga murojaat qiling.\n\n"
                      "/start - qayta urinish"),
            )

            # Update admin message (either caption or text)
            confirm_text = (f"✅ To'lov rad etildi!\n\n"
                            f"To'lov ID: {payment_id}\n"
                            f"User: @{payment.get('username')}\n"
                            f"Foydalanuvchi bildirishnoma oldi.")
            try:
                if query.message and (getattr(query.message, 'photo', None) or getattr(query.message, 'document', None)):
                    await query.edit_message_caption(confirm_text)
                else:
                    await query.edit_message_text(confirm_text)
            except Exception:
                logger.exception("Admin xabarini yangilashda xato (reject)")
        
        except Exception as e:
            logger.error(f"Rad etish xabari yuborishda xato: {str(e)}")

    
    async def button_callback(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        """Handle button callbacks"""
        query = update.callback_query
        await query.answer()
        user_id = query.from_user.id
        
        if query.data == 'restart':
            await self.start(update, context)
        elif query.data == 'history':
            await self.show_history(query, user_id)
        elif query.data == 'help':
            await self.show_help(query)
    
    async def show_history(self, query, user_id) -> None:
        """Show user's history"""
        if not self.user_history.get(user_id):
            await query.edit_message_text("📚 Tarixcha bo'sh.")
            return
        
        history_text = "📚 *Sizning tarixchangiz:*\n\n"
        for i, item in enumerate(self.user_history[user_id][-5:], 1):
            history_text += (
                f"{i}. {item['topic']}\n"
                f"   📍 {item['level']} | {item['pages']} bet\n"
                f"   🕐 {item['date']}\n\n"
            )
        
        await query.edit_message_text(history_text, parse_mode='Markdown')
    
    async def show_help(self, query) -> None:
        """Show help"""
        help_text = """
📚 *Premium Referat Bot - Yordam*

🤖 Bot nima qila oladi:
• 📝 Har qanday mavzu bo'yicha referat yaratish
• 🎬 Taqdimot (Presentation) yaratish
• ✍️ Mustaqil ish yaratish
• Turli ta'lim darajalariga mos materiallar
• Sozlanadigan betlar soni
• Turli formatlar (oddiy, strukturali, chuqur)

📋 Buyruqlar:
/start - Yangi ish yaratish
/help - Yordam ko'rish
/cancel - Bekor qilish

💡 Maslahatlar:
• Mavzuni aniq va batafsil kiriting
• To'g'ri ta'lim darajasini tanlang
• Betlar sonini qarama-qarshicha o'ylang
• Turini hisobga olib tanlang (referat/presentation/mustaqil ish)

❓ Savol bo'lsa, bot administratoriga murojaat qiling.
        """
        await query.edit_message_text(help_text, parse_mode='Markdown')
    
    async def generate_referat(self, topic: str, level: str, pages: int, format_type: str, work_type: str = 'referat') -> str:
        """Generate referat, presentation, or independent work using OpenAI"""
        try:
            level_descriptions = {
                'school': '8-11 sinflar uchun sodda va tushunarliroq',
                'college': 'Kollejj uchun o\'rta darajali',
                'university': 'Universitet uchun chuqur va ilmiy',
                'master': 'Magistratura uchun juda chuqur va tahliliy'
            }
            
            format_instructions = {
                'text': 'Sodda matn formatida',
                'structured': 'Oltin belgilar va sarlavhalar bilan yaxshi strukturali',
                'detailed': 'Batafsil tahlil, statistika, fikr-mulohaza va ilmiy dalillar bilan'
            }
            
            # Get additional info if needed
            university_name = self.user_data.get(self.user_data.get('current_user_id'), {}).get('university_name', '')
            student_name = self.user_data.get(self.user_data.get('current_user_id'), {}).get('student_name', '')
            teacher_name = self.user_data.get(self.user_data.get('current_user_id'), {}).get('teacher_name', '')
            
            # Find user_id from context
            user_id = None
            for uid, data in self.user_data.items():
                if data.get('topic') == topic and data.get('pages') == pages:
                    user_id = uid
                    university_name = data.get('university_name', '')
                    student_name = data.get('student_name', '')
                    teacher_name = data.get('teacher_name', '')
                    break
            
            # Work type specific instructions
            work_type_instructions = {
                'referat': {
                    'title': 'REFERAT',
                    'description': 'Batafsil va ilmiy referat',
                    'structure': """
1. 📌 **KIRISH** (1 bet)
   - Mavzuning dolzarbligi va mashhur olimlar fikri
   - Muammaning aktualligi
   - Referat maqsadi va vazifalari
   - Tadqiqot predmeti va ob'ekti

2. 🔍 **ASOSIY QISMLAR** ({pages-2} bet)
   - Tarixiy background va rivojlanish
   - Teorik asoslari va ta'riflar
   - Amaliy qoq'lami va misollari
   - Zamonaviy masalalar va muammalar

3. ✅ **XULOSA VA NATIJALAR** (1 bet)
   - Asosiy topilmalar
   - Mustahkam xulosalar
   - Mavzu bo'yicha umumiy fikr

4. 💡 **TAVSIYALAR VA KELAJAK ISTIQBOLLARI**
"""
                },
                'presentation': {
                    'title': 'TAQDIMOT (PRESENTATION)',
                    'description': 'Slaydlar uchun tashkil etilgan taqdimot matni',
                    'structure': """
1. 🎯 **SARLAVHA SLAYD**
   - Taqdimot sarlavhasi
   - Mavzu
   - Muallif
   - Sana

2. 📋 **KONTENT SLAYDLARI** ({pages-2} slayd)
   MUHIM: Har bir slaydning sarlavhasi va matnini yozing:
   - Slayd 1: [Sarlavha] - [Matn 100-200 so'z]
   - Slayd 2: [Sarlavha] - [Matn 100-200 so'z]
   - va hokazo...
   
   Har bir slayd uchun:
   • Rasmlar/grafikalar tavsiyalari
   • Asosiy fikrlar
   • Qo'llanmalar

3. ✅ **XULOSA SLAYD**
   - Asosiy topilmalar
   - Rahbarnoma va tavsiyalar

⭐ *MUHIM:* Har bir slaydning sarlavhasini va matnini alohida ko'rsating!
"""
                },
                'independent_work': {
                    'title': 'MUSTAQIL ISH',
                    'description': 'Mustaqil ish uchun tashkil etilgan material',
                    'structure': """
1. 📌 **KIRISH**
   - Ish maqsadi va vazifalari
   - Tadqiqat ob'ekti va predmeti
   - Tadqiqatning dolzarbligi

2. 🔍 **NAZARIY ASOSLARI**
   - Asosiy tushunchalar va ta'riflar
   - Ilmiy g'oyalar va nazariyalar
   - Olimlar fikri-mulohazalari

3. 📊 **AMALIY QISMLAR VA TAHLIL**
   - Tadqiqat metodi va usuli
   - Olingan ma'lumotlar
   - Tafsilotli tahlil
   - Grafikalar va jadvallar tavsiyalari

4. 💭 **O'Z XULOSALARI VA FIK'R-MULOHAZALARI**
   - Mustaqil xulosalar
   - Shaxsiy fikr-mulohazalari
   - Tilaklar va maslahatlar

5. ✅ **UMUMIY XULOSA**

6. 📚 **MANBALAR RO'YXATI** (tafsiya etsagina)
"""
                }
            }
            
            current_worktype = work_type_instructions.get(work_type, work_type_instructions['referat'])
            
            # Calculate more tokens for better quality
            words_per_page = 350
            total_words = pages * words_per_page
            max_tokens = min(int(total_words * 1.2), 4096)
            
            # Prepare title page for presentation and independent work
            title_page = ""
            if work_type in ['presentation', 'independent_work']:
                title_page = f"""
╔════════════════════════════════════════════════════════╗
║                   BOSH SAHIFA                            ║
╚════════════════════════════════════════════════════════╝

TASHKILOT NOMI:
{university_name}

{current_worktype['title']}

MAVZU:
{topic}

TAYYORLOVCHI:
{student_name}

MUDAVVIR:
{teacher_name}

SANA:
{datetime.now().strftime("%Y-yil %B %d-kuni")}

════════════════════════════════════════════════════════

"""
            
            prompt = f"""
Siz baland darajadagi professional o'zbekcha {current_worktype['title'].lower()} yozuvchisiz va AKA (Artificial Knowledge Assistant) ekanini bilib, o'zbekcha tilida chuqur, maqolali, ilmiy va ta'lim darajasiga mos {current_worktype['description']} yozing.

🎯 *ASOSIY MA'LUMOTLAR:*
• Mavzu: {topic}
• Ta'lim darajasi: {level_descriptions.get(level, 'Universitet')}
• Format: {format_instructions.get(format_type, 'Strukturali')}
• Taxminiy hajmi: {pages} bet (~{total_words} so'z)
• Ish turi: {current_worktype['title']}
• Sifat: PREMIUM

📋 *TUZILMA VA STRUKTURASI (MAJBURIY):* {current_worktype['structure']}

🎨 *SIFAT TALABLARI:*
✓ Juda chuqur, professional va akademik uslub
✓ Misollar, statistika va faktlar (haqiqiy va mashhur)
✓ Turli manbalardan iqtiboslar
✓ Olimlar fikri va tadqiqot natijalari
✓ O'zbekcha till qoidalariga to'liq mos
✓ Ilmiy terminlar to'g'ri va xatosiz
✓ Mustahkam mantiq va uslubiy birlik
✓ Paragraf-paravandlik tizimi
✓ PREMIUM sifatida yozilgan
✓ 100% original va plagiatdan voz kechilib yozilgan

📝 *FORMATNI YAXSHI TUSHUNIB YOZING:*
"""
            
            if format_type == 'detailed':
                prompt += """
CHUQUR FORMAT: Har bir bo'limda:
- Kirish gapi
- 2-3 ta asos o'n fikrlar
- Konkret misollar va raqamlar
- Ekspert fikri yoki ilmiy dalil
- Yakun jumla
"""
            
            prompt += f"""

✅ *{current_worktype['title']} MATNI ({pages} BET):*
"""
            
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {
                        "role": "system",
                        "content": f"Siz o'zbekcha tilida {level_descriptions.get(level, 'Universitet')}, juda professional, baland sifatli va ilmiy {current_worktype['description']} yoziladigan kuchli AI assistentiisiz. Har doim O'ZBEKCHA TILIDA, TO'LIQ PROFESIONAL VA TO'G'RI JAVOB BERING. Ishni PREMIUM sifatda yozing. Ortiqcha gaplar va ayt-kitoblardan voz kechib, faqat material matni yozing."
                    },
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                temperature=0.7,
                max_tokens=max_tokens,
                top_p=0.95,
                presence_penalty=0.1,
                frequency_penalty=0.05
            )
            
            referat_text = response.choices[0].message.content
            
            # Add footer
            footer = f"""

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
✅ *{current_worktype['title']} tayyorlanganı: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}*
👤 *Sifati: PREMIUM*
📄 *Umumiy hajmi: ~{total_words} so'z*
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
            """
            
            # Combine title page + content + footer for presentation and independent work
            if work_type in ['presentation', 'independent_work']:
                return title_page + referat_text + footer
            else:
                return referat_text + footer
        except Exception as e:
            # Record last OpenAI error for higher-level handlers to inspect
            self.last_openai_error = str(e)
            logger.error(f"OpenAI xatosi: {str(e)}", exc_info=True)
            return None
    
    async def cancel(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
        """Cancel operation"""
        await update.message.reply_text(
            "❌ Bekor qilindi.\n\n/start'ni bosing yangi referat yaratish uchun."
        )
        return ConversationHandler.END
    
    async def help_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        """Send help message"""
        help_text = """
📚 *Referat Bot - Yordam*

🤖 Bot nima qila oladi:
• Har qanday mavzu bo'yicha referat yaratish
• Turli ta'lim darajalariga mos referatlar
• Sozlanadigan betlar soni
• Turli formatlar

📋 Buyruqlar:
/start - Yangi referat yaratish
/help - Yordam ko'rish
/cancel - Bekor qilish

💡 Maslahatlar:
- Mavzuni aniq va batafsil kiriting
- Ta'lim darajasini to'g'ri tanlang
- Betlar sonini qarama-qarshicha o'ylang

❓ Savol bo'lsa: @admin_username ga murojaat qiling
        """
        await update.message.reply_text(help_text, parse_mode='Markdown')

def main() -> None:
    """Start the bot"""
    if not TELEGRAM_BOT_TOKEN:
        logger.error("TELEGRAM_BOT_TOKEN muhit o'zgaruvchisida o'rnatilmagan!")
        return
    
    if not OPENAI_API_KEY:
        logger.error("OPENAI_API_KEY muhit o'zgaruvchisida o'rnatilmagan!")
        return
    
    # Create application with higher timeouts to reduce TimedOut errors
    request = HTTPXRequest(connect_timeout=20, read_timeout=60, write_timeout=60, pool_timeout=10, connection_pool_size=4)
    application = Application.builder().token(TELEGRAM_BOT_TOKEN).request(request).build()
    bot = ReferatBot()
    
    # Conversation handler
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler("start", bot.start)],
        states={
            TOPIC: [MessageHandler(filters.TEXT & ~filters.COMMAND, bot.get_topic)],
            WORK_TYPE: [CallbackQueryHandler(bot.get_work_type)],
            LEVEL: [CallbackQueryHandler(bot.get_level)],
            PAGE_RANGE: [CallbackQueryHandler(bot.get_page_range)],
            PAGE_COUNT: [MessageHandler(filters.TEXT & ~filters.COMMAND, bot.get_page_count)],
            FORMAT: [CallbackQueryHandler(bot.get_format)],
            ADDITIONAL_INFO: [MessageHandler(filters.TEXT & ~filters.COMMAND, bot.get_additional_info)],
            PAYMENT_CONFIRMATION: [
                CallbackQueryHandler(bot.handle_payment_decision),
                MessageHandler(filters.PHOTO, bot.receive_payment_receipt)
            ],
        },
        fallbacks=[CommandHandler("cancel", bot.cancel)],
    )
    
    # Add handlers
    application.add_handler(conv_handler)
    application.add_handler(CommandHandler("help", bot.help_command))
    application.add_handler(CallbackQueryHandler(bot.button_callback, pattern='^(restart|history|help)$'))
    
    # Admin handlers
    application.add_handler(
        CallbackQueryHandler(bot.admin_approve_payment, pattern='^admin_approve_')
    )
    application.add_handler(
        CallbackQueryHandler(bot.admin_reject_payment, pattern='^admin_reject_')
    )
    
    # Start bot
    logger.info("Bot ishga tushmoqda...")
    print("🤖 Premium Referat Bot ishga tushdi!")
    print("🔗 Telegram'da botingizni qidiring va /start buyrug'ini kiriting")
    print(f"💳 Admin ID: {TELEGRAM_ADMIN_ID}")
    application.run_polling()

if __name__ == '__main__':
    main()

