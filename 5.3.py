prices = {
    "apple": 2,
    "banana": 2,
    "orange": 1,
    "milk": 1,
    "bread": 1
}

quantities = {
    "apple": 1,
    "banana": 2,
    "orange": 1,
    "milk": 2,
    "bread": 1
}

total_bill = 0.0
bill_details = []

for item, quantity in quantities.items():
    item_cost = prices[item] * quantity
    total_bill += item_cost
    bill_details.append(f"{item.capitalize()}: {quantity} * {prices[item]} = {item_cost}")

bill_details.append(f"\nTotal bill: ₹ {total_bill}")
print("\n".join(bill_details))
print(dir(dict))
# print(type(dict.join))

#OUTPUT
#Apple: 1 * 2 = 2
# Banana: 2 * 2 = 4
# Orange: 1 * 1 = 1
# Milk: 2 * 1 = 2
# Bread: 1 * 1 = 1

# Total bill: ₹ 10.0