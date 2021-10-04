# Task 5 - Truck Tour
from collections import deque

number_of_petrol_pumps = int(input())
queue = deque()

for i in range(number_of_petrol_pumps):
    pump = [int(x) for x in input().split()]
    queue.append(pump)

for attempt in range(number_of_petrol_pumps):

    car_fuel = 0
    completed = True

    for petrol, distance in queue:
        car_fuel += petrol
        if distance > car_fuel:
            completed = False
            break
        car_fuel -= distance

    if completed:
        print(attempt)
        break
    queue.append(queue.popleft())
