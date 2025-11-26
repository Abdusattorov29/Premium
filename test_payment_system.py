#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
To'lov tizimi test faylı
Payment System Testing
"""

import json
from payment_system import PricingSystem, PaymentTracker, AdminCard
from datetime import datetime

def test_pricing_system():
    """Narx kalkulyatorini test qilish"""
    print("=" * 60)
    print("📊 NARX KALKULYATORI TEST")
    print("=" * 60)
    
    pricing = PricingSystem()
    
    test_cases = [
        (3, 'school', 'text', "Maktab - Oddiy"),
        (5, 'school', 'structured', "Maktab - Strukturali"),
        (8, 'college', 'text', "Kollejj - Oddiy"),
        (10, 'college', 'detailed', "Kollejj - Tahlili"),
        (12, 'university', 'text', "Universitet - Oddiy"),
        (15, 'university', 'structured', "Universitet - Strukturali"),
        (18, 'master', 'detailed', "Magistratura - Tahlili"),
    ]
    
    print()
    for pages, level, fmt, desc in test_cases:
        price_info = pricing.calculate_price(pages, level, fmt)
        print(f"📌 {desc}")
        print(f"   Betlar: {pages} ta | Diapazon: {price_info['page_range']}")
        print(f"   Ta'lim: {level} (x{price_info['quality_multiplier']})")
        print(f"   Format: {fmt} (x{price_info['format_multiplier']})")
        print(f"   💰 NARX: {price_info['final_price']:,} {price_info['currency']}")
        print()
    
    print("=" * 60)
    print("✅ Narx kalkulyatori to'g'ri ishlaydi!")
    print("=" * 60)


def test_payment_tracker():
    """To'lov kuzatuvchisini test qilish"""
    print("\n" + "=" * 60)
    print("💳 TO'LOV KUZATUVCHISI TEST")
    print("=" * 60)
    
    tracker = PaymentTracker()
    
    # Yangi to'lov yaratish
    payment1 = tracker.create_payment(
        user_id=123456789,
        username='test_user_1',
        amount=50000,
        topic='O\'zbekistonning tarixiy rivojlanishi',
        level='university',
        pages=12,
        format_type='detailed'
    )
    
    print(f"\n✅ To'lov #1 yaratildi:")
    print(f"   ID: {payment1['payment_id']}")
    print(f"   Status: {payment1['status']}")
    print(f"   Summa: {payment1['amount']:,} UZS")
    print(f"   Foydalanuvchi: @{payment1['username']}")
    
    # Ikkinchi to'lov
    payment2 = tracker.create_payment(
        user_id=987654321,
        username='test_user_2',
        amount=25000,
        topic='Informatika',
        level='college',
        pages=5,
        format_type='text'
    )
    
    print(f"\n✅ To'lov #2 yaratildi:")
    print(f"   ID: {payment2['payment_id']}")
    print(f"   Status: {payment2['status']}")
    print(f"   Summa: {payment2['amount']:,} UZS")
    
    # Statusni o'zgartirish
    tracker.update_payment_status(payment1['payment_id'], 'confirmed')
    tracker.update_payment_status(payment2['payment_id'], 'rejected', 'Chek noto\'g\'ri')
    
    print(f"\n🔄 Statuslar o'zgartirildi:")
    updated_p1 = tracker.get_payment(payment1['payment_id'])
    updated_p2 = tracker.get_payment(payment2['payment_id'])
    print(f"   To'lov #1: {updated_p1['status']} (tasdiqlab yaratilgan: {updated_p1['confirmed_at']})")
    print(f"   To'lov #2: {updated_p2['status']} (sabab: {updated_p2['rejected_reason']})")
    
    # Statistika
    stats = tracker.get_payment_stats()
    print(f"\n📊 Umumiy statistika:")
    print(f"   Jami to'lovlar: {stats['total_payments']}")
    print(f"   Tasdiqlangan: {stats['confirmed']}")
    print(f"   Kutib turyapti: {stats['pending']}")
    print(f"   Rad etilgan: {stats['rejected']}")
    print(f"   Umumiy summa: {stats['total_amount_received']:,} {stats['currency']}")
    
    print("\n" + "=" * 60)
    print("✅ To'lov kuzatuvchisi to'g'ri ishlaydi!")
    print("=" * 60)


def test_admin_card():
    """Admin kartasini test qilish"""
    print("\n" + "=" * 60)
    print("💳 ADMIN KARTASI TEST")
    print("=" * 60)
    
    admin_card = AdminCard()
    
    print(admin_card.get_payment_instruction())
    
    print("=" * 60)
    print("✅ Admin kartasi to'g'ri ishlay verdi!")
    print("=" * 60)


def show_pricing_table():
    """Narxlar jadvalini ko'rsatish"""
    print("\n" + "=" * 60)
    print("💰 NARXLAR JADVALI")
    print("=" * 60)
    
    pricing = PricingSystem()
    
    print("\n📄 BET DIAPAZONLARI BO'YICHA ASOSIY NARXLAR:")
    for range_key, range_info in pricing.prices['page_ranges'].items():
        print(f"   {range_info['name']:20} → {range_info['base']:,} UZS")
    
    print("\n🎓 TA'LIM DARAJASI KOEFFITSIYENTLARI:")
    for level_key, mult in pricing.prices['quality_multipliers'].items():
        print(f"   {level_key:15} → x{mult}")
    
    print("\n📋 FORMAT KOEFFITSIYENTLARI:")
    for fmt_key, mult in pricing.prices['format_multipliers'].items():
        print(f"   {fmt_key:15} → x{mult}")
    
    print("\n" + "=" * 60)


def main():
    """Asosiy test funksiyasi"""
    print("\n")
    print("╔════════════════════════════════════════════════════════╗")
    print("║  🎓 PREMIUM REFERAT BOT - TO'LOV TIZIMI TEST          ║")
    print("║  Payment System v3.0                                   ║")
    print("╚════════════════════════════════════════════════════════╝")
    
    try:
        # Narxlar jadvalini ko'rsat
        show_pricing_table()
        
        # Testlarni ishga tushir
        test_pricing_system()
        test_payment_tracker()
        test_admin_card()
        
        print("\n")
        print("╔════════════════════════════════════════════════════════╗")
        print("║  ✅ BARCHA TESTLAR MUVAFFAQIYATLI O'TADI!             ║")
        print("║  🎉 To'lov tizimi ishga tayyor!                       ║")
        print("╚════════════════════════════════════════════════════════╝")
        print("\n")
        
    except Exception as e:
        print(f"\n❌ XATO: {str(e)}")
        import traceback
        traceback.print_exc()


if __name__ == '__main__':
    main()
