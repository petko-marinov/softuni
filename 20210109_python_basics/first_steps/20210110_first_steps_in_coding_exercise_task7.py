# Task 7 - Fruit market
price_strawberry = float(input())

kg_banana = float(input())
kg_orange = float(input())
kg_berry = float(input())
kg_strawberry = float(input())

price_berry = price_strawberry * 0.5
price_orange = price_berry * 0.6
price_banana = price_berry * 0.2

total = (kg_banana * price_banana) + (kg_orange * price_orange) + \
        (kg_berry * price_berry) + (kg_strawberry * price_strawberry)

print(total)
