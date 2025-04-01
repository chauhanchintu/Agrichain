from collections import Counter

def calculate_total_price(items: str) -> int:
    prices = {'A': 50, 'B': 30, 'C': 20, 'D': 15}
    discounts = {'A': (3, 130), 'B': (2, 45)}
    
    item_counts = Counter(items)
    # print('item_counts',item_counts)
    total = 0
    
    for item, count in item_counts.items():
        # print('itmessss',item,count)
        if item in discounts:
            discount_qty, discount_price = discounts[item]
            # print('discounts[item]',discounts[item])
            total += (count // discount_qty) * discount_price + (count % discount_qty) * prices[item]
            # print('totallllll',total)
        else:
            total += count * prices[item]
    
    return total

if __name__ == "__main__":
    test_cases = [
        "", "A", "AB", "CDBA", "AA", "AAA", "AAAA", "AAAAA", "AAAAAA",
        "AAAB", "AAABB", "AAABBD", "DABABA"
    ]
     #   prices = {'A': 50, 'B': 30, 'C': 20, 'D': 15}
    
    for case in test_cases:
        print(f'Input: "{case}" => Output: {calculate_total_price(case)}')
