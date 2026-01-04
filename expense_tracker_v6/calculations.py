def total_price(data):
    if not data:
        return None
    total = 0
    for each in data:
        total += each["amount"]
    return total


def average_price(data):
    if not data:
        return None
    total = total_price(data)
    count = len(data)
    average = total / count
    return average

def get_low_high_price(data):
    if not data:
        return None

    low_price  = float('inf')
    high_price = float('-inf')
    max_product = ""
    min_product = ""

    for each in data:
        if each["amount"] < low_price:
            low_price = each["amount"]
            min_product = each["product"]

        if each["amount"] > high_price:
            high_price = each["amount"]
            max_product = each["product"]

    return max_product, min_product,high_price,low_price

def price_per_category(data):
    if data :
        category_price = {}
        for each in data:
            if each["category"] not in category_price:
                category_price[each["category"]] = each["amount"]
            else:
                category_price[each["category"]] += each["amount"]
        return category_price
    return {}

def high_lowest_price_per_category(data):
    if data :
        category_price = price_per_category(data)
        max_category_price = max(category_price , key=category_price.get)
        min_category_price = min(category_price , key=category_price.get)
        return max_category_price, min_category_price,category_price[max_category_price],category_price[min_category_price]
    return None, None,None,None


