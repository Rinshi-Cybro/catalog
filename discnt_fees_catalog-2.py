# Product catalog
products = {
    "Product A": 20,
    "Product B": 40,
    "Product C": 50
}

# Discount rules
discount_rules = {
    "flat_10_discount": 200,
    "bulk_5_discount": 10,
    "bulk_10_discount": 20,
    "tiered_50_discount": 30
}

# Input quantity and gift wrap information for each product
quantities = {}
gift_wraps = {}
for product in products:
    quantity = int(input(f"Enter the quantity of {product}: "))
    quantities[product] = quantity
    gift_wrap = input(f"Is {product} wrapped as a gift? (yes/no): ")
    gift_wraps[product] = gift_wrap.lower() == "yes"

# Calculate subtotal
subtotal = 0
for product in products:
    subtotal += products[product] * quantities[product]

# Apply discounts
applicable_discounts = {}
for rule in discount_rules:
    if subtotal >= discount_rules[rule]:
        applicable_discounts[rule] = discount_rules[rule]

# Calculate discount amount
discount_amount = 0
discount_name = ""
if applicable_discounts:
    max_discount = max(applicable_discounts.values())
    discount_name = [rule for rule, amount in applicable_discounts.items() if amount == max_discount][0]
    discount_amount = max_discount

# Calculate shipping fee and gift wrap fee
shipping_fee = 5 * (sum(quantities.values()) // 10)
gift_wrap_fee = sum(gift_wraps.values())

# Apply tiered discount rule
if discount_name == "tiered_50_discount":
    for product in products:
        if quantities[product] > 15:
            discount_amount += (quantities[product] - 15) * (products[product] * 0.5)

# Calculate total amount
total = subtotal - discount_amount + shipping_fee + gift_wrap_fee

# Output details
for product in products:
    product_total = products[product] * quantities[product]
    print(f"{product}: Quantity: {quantities[product]}, Total: ${product_total}")

print(f"\nSubtotal: ${subtotal}")
print(f"Discount Applied: {discount_name}, Discount Amount: ${discount_amount}")
print(f"Shipping Fee: ${shipping_fee}")
print(f"Gift Wrap Fee: ${gift_wrap_fee}")
print(f"Total: ${total}")