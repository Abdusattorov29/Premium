import json
import os
from datetime import datetime
from typing import Dict, Optional, List
import uuid

class PricingSystem:
    """Dinamik narxlar tizimi"""
    
    def __init__(self):
        self.prices = {
            'page_ranges': {
                '1-5': {'base': 1000, 'name': '1-5 bet'},
                '5-10': {'base': 2000, 'name': '5-10 bet'},
                '10-15': {'base': 3000, 'name': '10-15 bet'},
                '15-20': {'base': 4000, 'name': '15-20 bet'},
            },
            'quality_multipliers': {
                'school': 1.0,      # Maktab - 1x
                'college': 1.3,     # Kollejj - 1.3x
                'university': 1.7,  # Universitet - 1.7x
                'master': 2.2,      # Magistratura - 2.2x
            },
            'format_multipliers': {
                'text': 1.0,           # Oddiy matn
                'structured': 1.1,     # Strukturali
                'detailed': 1.4,       # Chuqur tahlili
            },
            'worktype_multipliers': {
                'referat': 1.0,              # Referat - standart
                'presentation': 0.85,       # Taqdimot - 15% chegirma
                'independent_work': 0.9,    # Mustaqil ish - 10% chegirma
            }
        }
    
    def get_page_range(self, pages: int) -> str:
        """Bet soniga qarab diapazon aniqlash"""
        if 1 <= pages <= 5:
            return '1-5'
        elif 6 <= pages <= 10:
            return '5-10'
        elif 11 <= pages <= 15:
            return '10-15'
        elif 16 <= pages <= 20:
            return '15-20'
        else:
            return '15-20'  # Maksimal diapazon
    
    def calculate_price(self, pages: int, level: str, format_type: str, work_type: str = 'referat') -> Dict:
        """Narx hisoblash"""
        page_range = self.get_page_range(pages)
        base_price = self.prices['page_ranges'][page_range]['base']
        quality_mult = self.prices['quality_multipliers'].get(level, 1.0)
        format_mult = self.prices['format_multipliers'].get(format_type, 1.0)
        worktype_mult = self.prices['worktype_multipliers'].get(work_type, 1.0)
        
        final_price = int(base_price * quality_mult * format_mult * worktype_mult)
        
        return {
            'base_price': base_price,
            'page_range': page_range,
            'quality_multiplier': quality_mult,
            'format_multiplier': format_mult,
            'worktype_multiplier': worktype_mult,
            'final_price': final_price,
            'currency': 'UZS'
        }
    
    def get_all_ranges(self) -> Dict:
        """Barcha diapazonlarni olish"""
        return self.prices['page_ranges']


class PaymentTracker:
    """To'lovlarni kuzatish tizimi"""
    
    def __init__(self, data_file: str = 'payments.json'):
        self.data_file = data_file
        self.payments = self._load_payments()
    
    def _load_payments(self) -> List[Dict]:
        """Saqlangan to'lovlarni yuklash"""
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    # Agar dict bo'lsa, bo'sh list qaytarish
                    if isinstance(data, dict):
                        return []
                    # Agar list bo'lsa, qaytarish
                    if isinstance(data, list):
                        return data
                    return []
            except:
                return []
        return []
    
    def _save_payments(self) -> None:
        """To'lovlarni saqlash"""
        with open(self.data_file, 'w', encoding='utf-8') as f:
            json.dump(self.payments, f, ensure_ascii=False, indent=2)
    
    def create_payment(self, user_id: int, username: str, amount: int, 
                      topic: str, level: str, pages: int, format_type: str, work_type: str = 'referat',
                      university_name: str = '', student_name: str = '', teacher_name: str = '') -> Dict:
        """Yangi to'lov yaratish"""
        payment_id = str(uuid.uuid4())[:8]
        
        payment = {
            'payment_id': payment_id,
            'user_id': user_id,
            'username': username,
            'amount': amount,
            'topic': topic,
            'level': level,
            'pages': pages,
            'format': format_type,
            'work_type': work_type,
            'university_name': university_name,
            'student_name': student_name,
            'teacher_name': teacher_name,
            'status': 'pending',  # pending, confirmed, rejected, completed
            'created_at': datetime.now().isoformat(),
            'confirmed_at': None,
            'rejected_reason': None
        }
        
        self.payments.append(payment)
        self._save_payments()
        
        return payment
    
    def get_payment(self, payment_id: str) -> Optional[Dict]:
        """To'lovni ID bo'yicha olish"""
        for payment in self.payments:
            if payment['payment_id'] == payment_id:
                return payment
        return None
    
    def update_payment_status(self, payment_id: str, status: str, 
                             reason: Optional[str] = None) -> bool:
        """To'lov statusini o'zgartirish"""
        for payment in self.payments:
            if payment['payment_id'] == payment_id:
                payment['status'] = status
                if status == 'confirmed':
                    payment['confirmed_at'] = datetime.now().isoformat()
                elif status == 'rejected':
                    payment['rejected_reason'] = reason or 'No reason provided'
                self._save_payments()
                return True
        return False
    
    def get_pending_payments(self) -> List[Dict]:
        """Kutib turgan to'lovlarni olish"""
        return [p for p in self.payments if p['status'] == 'pending']
    
    def get_user_payments(self, user_id: int) -> List[Dict]:
        """Foydalanuvchining barcha to'lovlarini olish"""
        return [p for p in self.payments if p['user_id'] == user_id]
    
    def get_payment_stats(self) -> Dict:
        """To'lov statistikasi"""
        total = len(self.payments)
        confirmed = len([p for p in self.payments if p['status'] == 'confirmed'])
        pending = len([p for p in self.payments if p['status'] == 'pending'])
        rejected = len([p for p in self.payments if p['status'] == 'rejected'])
        
        total_amount = sum(p['amount'] for p in self.payments if p['status'] == 'confirmed')
        
        return {
            'total_payments': total,
            'confirmed': confirmed,
            'pending': pending,
            'rejected': rejected,
            'total_amount_received': total_amount,
            'currency': 'UZS'
        }


class AdminCard:
    """Admin kartasi - to'lovlar uchun"""
    
    def __init__(self):
        self.card_info = {
            'card_number': os.getenv('ADMIN_CARD_NUMBER', '****-****-****-1234'),
            'card_holder': os.getenv('ADMIN_CARD_HOLDER', 'ADMIN NAME'),
            'bank': os.getenv('ADMIN_BANK', 'Humo Bank'),
            'account_type': 'Jismoniy shaxs',
        }
    
    def get_payment_instruction(self) -> str:
        """To'lov ko'rsatmalarini olish"""
        instruction = f"""
💳 *TO'LOV MA'LUMOTLARI*

Kartaga to'lov qiling:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🏦 Bank: {self.card_info['bank']}
💳 Karta raqami: {self.card_info['card_number']}
👤 Egasi: {self.card_info['card_holder']}
📋 Tur: {self.card_info['account_type']}
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

✅ To'lovdan so'ng CHEKNI BOT'GA YUBORING!
⏰ Admin 5 daqiqa ichida tasdiqlaydi.

⚠️ Muhim: 
• Chekda summa va vaqt ko'rinishi kerak
• Screenshot yoki rasmni yuboring
• Chek olinmaganda takrorlang
"""
        return instruction
    
    def verify_payment_receipt(self, receipt_data: Dict) -> Dict:
        """To'lov chekini tekshirish"""
        required_fields = ['amount', 'timestamp', 'receipt_image']
        
        result = {
            'is_valid': True,
            'errors': [],
            'payment_data': {}
        }
        
        for field in required_fields:
            if field not in receipt_data or not receipt_data[field]:
                result['is_valid'] = False
                result['errors'].append(f"'{field}' yo'q")
        
        if result['is_valid']:
            result['payment_data'] = {
                'amount': receipt_data.get('amount'),
                'timestamp': receipt_data.get('timestamp'),
                'verified_at': datetime.now().isoformat()
            }
        
        return result


# Foydalanishga tayyor misollar
if __name__ == "__main__":
    # Pricing
    pricing = PricingSystem()
    
    # Turli kombinatsiyalarni test qilish
    test_cases = [
        (5, 'school', 'text'),
        (8, 'college', 'structured'),
        (12, 'university', 'detailed'),
        (18, 'master', 'detailed'),
    ]
    
    print("📊 NARX KALKULYATORI TEST\n")
    for pages, level, fmt in test_cases:
        price_info = pricing.calculate_price(pages, level, fmt)
        print(f"Bet: {pages} | Darajasi: {level} | Format: {fmt}")
        print(f"  → Narx: {price_info['final_price']} {price_info['currency']}\n")
    
    # Payment Tracker
    tracker = PaymentTracker()
    
    # Test to'lov yaratish
    test_payment = tracker.create_payment(
        user_id=123456,
        username='test_user',
        amount=50000,
        topic='O\'zbekiston tarixiy rivojlanishi',
        level='university',
        pages=12,
        format_type='detailed'
    )
    
    print(f"✅ Test to'lov yaratildi: {test_payment['payment_id']}")
    print(f"   Status: {test_payment['status']}")
    print(f"   Summa: {test_payment['amount']} UZS\n")
    
    # Admin Card
    admin_card = AdminCard()
    print("💳 ADMIN KARTASI INFO:")
    print(admin_card.get_payment_instruction())
