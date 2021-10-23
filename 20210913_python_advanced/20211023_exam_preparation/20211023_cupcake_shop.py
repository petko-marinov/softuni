# Task 3 - Cupcake_shop


def stock_availability(inventory_list, operation, *args):
    if operation == 'delivery':
        for element in args:
            inventory_list.append(element)
    elif operation == 'sell':
        if len(args) == 0:
            del inventory_list[0]
        elif len(args) > 0:
            command = str(args[0])
            if command.isdigit():
                for i in range(int(command)):
                    del inventory_list[0]
            else:
                for element in args:
                    number_of_products = inventory_list.count(element)
                    for i in range(0, number_of_products):
                        inventory_list.remove(element)

    return inventory_list


# print(stock_availability(["choco", "vanilla", "banana"], "delivery", "caramel", "berry"))
# print(stock_availability(["chocolate", "vanilla", "banana"], "delivery", "cookie", "banana"))
# print(stock_availability(["chocolate", "vanilla", "banana"], "sell"))
# print(stock_availability(["chocolate", "vanilla", "banana"], "sell", 3))
# print(stock_availability(["chocolate", "chocolate", "banana"], "sell", "chocolate"))
# print(stock_availability(["cookie", "chocolate", "banana"], "sell", "chocolate"))
# print(stock_availability(["chocolate", "vanilla", "banana"], "sell", "cookie"))
