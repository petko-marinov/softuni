# Task 3  - Fast Food
from collections import deque

food = int(input())
orders_str = input().split(" ")
orders = deque()
for i in range(len(orders_str)):
    orders.append(int(orders_str[i]))
output = ''

if orders:
    max_order = max(orders)

while orders:
    first_come = orders[0]
    if first_come > food:
        break
    else:
        food -= first_come
        first_come = orders.popleft()

print(max_order)

if orders:
    print(f"Orders left: {' '.join(map(str, orders))}")
else:
    print("Orders complete")
