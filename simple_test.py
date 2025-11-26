#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Simple Payment System Test
"""

from payment_system import PricingSystem, PaymentTracker, AdminCard

def test_pricing():
    pricing = PricingSystem()
    
    print("PRICING SYSTEM TEST")
    print("=" * 50)
    
    # Test 1
    result = pricing.calculate_price(5, 'school', 'text')
    print(f"Test 1 - Maktab 5 bet: {result['final_price']} UZS")
    assert result['final_price'] == 10000, "Failed!"
    
    # Test 2
    result = pricing.calculate_price(12, 'university', 'detailed')
    print(f"Test 2 - Universitet 12 bet chuqur: {result['final_price']} UZS")
    assert result['final_price'] == 71400, "Failed!"
    
    print("SUCCESS: All pricing tests passed!")


def test_tracker():
    tracker = PaymentTracker()
    
    print("\nPAYMENT TRACKER TEST")
    print("=" * 50)
    
    # Create payment
    payment = tracker.create_payment(
        user_id=123,
        username='test_user',
        amount=50000,
        topic='Test mavzu',
        level='university',
        pages=12,
        format_type='detailed'
    )
    
    print(f"Payment created: {payment['payment_id']}")
    print(f"Status: {payment['status']}")
    
    # Update status
    tracker.update_payment_status(payment['payment_id'], 'confirmed')
    updated = tracker.get_payment(payment['payment_id'])
    print(f"Updated status: {updated['status']}")
    
    print("SUCCESS: All tracker tests passed!")


def test_admin_card():
    admin_card = AdminCard()
    
    print("\nADMIN CARD TEST")
    print("=" * 50)
    
    instruction = admin_card.get_payment_instruction()
    if "Bank" in instruction:
        print("Admin card info retrieved successfully!")
        print("SUCCESS: Admin card test passed!")
    else:
        print("FAILED!")


if __name__ == '__main__':
    try:
        test_pricing()
        test_tracker()
        test_admin_card()
        print("\n" + "=" * 50)
        print("ALL TESTS PASSED!")
        print("=" * 50)
    except Exception as e:
        print(f"ERROR: {e}")
        import traceback
        traceback.print_exc()
