print("\n=== Shopping Receipt ===")

while True:
    item_name = input("Item name: ").strip()
    if item_name:
        break
    print("Please try again.")

while True:
    try:
        item_price = float(input("Item price: "))
        if item_price > 0:
            break
        else:
            print("Please try again.")
    except ValueError:
        print("Invalid price.")
        
while True:
    try:
        Quantity = int(input('Quantity :'))
        if Quantity > 0:
            break
        else:
             print("Please try again.")
    except ValueError:
        print("Invalid Quantity")
        
total = item_price * Quantity

print("\n=== Shopping Receipt ===")
print(f"Item     : {item_name}")
print(f"Price    : {item_price:.2f} Bath")
print(f"Quantity : {Quantity}")
print(f"Total    : {total:.2f} Bath")