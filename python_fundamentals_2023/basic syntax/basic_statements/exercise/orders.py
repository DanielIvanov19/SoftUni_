number_of_orders = int(input())
total_price = 0
for _ in range(0, number_of_orders):
    price_per_capsule = float(input())
    days = int(input())
    capsules = int(input())
    if price_per_capsule < 0.01 or price_per_capsule > 100.00:
        continue
    elif days < 1 or days > 31:
        continue
    elif capsules < 1 or capsules > 2000:
        continue
    else:
        price = price_per_capsule * days * capsules
        print(f"The price for the coffee is: ${price:.2f}")
        total_price += price
print(f"Total: ${total_price:.2f}")
#if 0.01 <= price_per_capsule <= 100.00 and 1 <= days <= 31 and 1 <= capsules <= 2000: