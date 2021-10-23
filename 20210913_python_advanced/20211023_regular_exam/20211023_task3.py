# Task 3

def shopping_list(budget, **kwargs):
    if budget >= 100:
        product_in_basket = []
        total_price = 0
        message_list = []
        products_in_basket = 0
        message = ""

        for key, value in kwargs.items():
            total_price = value[0] * value[1]
            if total_price <= budget and products_in_basket < 5:
                budget -= total_price
                products_in_basket += 1
                temp_message = f"You bought {key} for {total_price:.2f} leva."
                message_list.append(temp_message)
                message = "\n". join(message_list)
        return message
    else:
        message = "You do not have enough budget."
        return message


print(shopping_list(100,
                    ))

print(shopping_list(20,
                    jeans=(19.99, 1),
                    ))

print(shopping_list(104,
                    cola=(1.20, 2),
                    candies=(0.25, 15),
                    bread=(1.80, 1),
                    pie=(10.50, 5),
                    tomatoes=(4.20, 1),
                    milk=(2.50, 2),
                    juice=(2, 3),
                    eggs=(3, 1),
                    ))


