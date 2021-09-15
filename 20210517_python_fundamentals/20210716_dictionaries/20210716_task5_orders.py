# Task 5 - Orders
command = []
my_products = {}
i = 0
is_available_product = False

while "buy" not in command:
    command = input().split(" ")
    i += 1

    for key in my_products.keys():
        if command[0] == my_products[key]["Product"] and "buy" not in command:
            my_products[key]["Price"] = float(command[1])
            my_products[key]["Quantity"] += int(command[2])
            is_available_product = True
            i = key + 1

    if not is_available_product and "buy" not in command:
        my_products[i] = {}
        my_products[i]["Product"] = command[0]
        my_products[i]["Price"] = float(command[1])
        my_products[i]["Quantity"] = int(command[2])

for key, value in my_products.items():
    total_price = my_products[key]["Price"]*my_products[key]["Quantity"]
    print(f'{my_products[key]["Product"]} -> {total_price:.2f}')
