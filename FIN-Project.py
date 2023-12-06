def generate_table(num_items, base):
    print(f"{'Item':<12}| {'Base':<15}")
    print('-' * 30)

    if num_items > 0:
        base_increment = base / num_items
    else:
        base_increment = 0


    for i in range(num_items, -1, -1):
        item = f"Score {i}"
        print(f"{item:<12}|  {base:<15,.2f}")

        # Decrement the base value by the calculated increment
        base -= base_increment

items = int(input("Enter the number of items: "))
base = float(input("Enter the base value: "))

generate_table(items, base)
