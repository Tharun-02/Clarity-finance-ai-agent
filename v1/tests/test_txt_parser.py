# Sample test input — mimics a real txt file without real data


sample_text = """
Jan 1
coffee 30
groceries 250
chicken 280

Jan 3
gym 500
bus ticket 45
lunch 120

Jan 5
medicine 200
netflix 650
"""

from agent.txt_parser import parse_txt_with_ai  # Adjust the import path as needed


def test_parser():
    print("🧪 Running parser test...\n")
    results = parse_txt_with_ai(sample_text)

    # Check 1: Did we get a list back?
    assert isinstance(results, list), "❌ Result should be a list"
    print(f"✅ Got {len(results)} expenses parsed")

    # Check 2: Did we get all expenses?
    assert len(results) >= 6, f"❌ Too few expenses parsed, got {len(results)}"
    print(f"✅ Got {len(results)} expenses parsed")

    # Check 3: Do all items have required fields?
    required_fields = ['date', 'description', 'amount', 'category', 'payment_method']
    for i, expense in enumerate(results):
        for field in required_fields:
            assert field in expense, f"❌ Expense {i} missing field: {field}"
    print("✅ All expenses have required fields")

    # Check 4: Are amounts numbers?
    for expense in results:
        assert isinstance(expense['amount'], (int, float)), f"❌ Amount is not a number: {expense['amount']}"
    print("✅ All amounts are numbers")

    # Check 5: Print what AI returned so you can visually inspect
    print("\n📋 Parsed Results:")
    for expense in results:
        print(f"  {expense['date']} | {expense['description']:<20} | ₹{expense['amount']:<8} | {expense['category']}")

if __name__ == "__main__":
    test_parser()