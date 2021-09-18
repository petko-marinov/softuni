# Task 4  - Fashion Boutique
cloths_in_box = [int(x) for x in input().split(" ")]
rack_capacity = int(input())
total_racks = 0
next_rack_capacity = rack_capacity

while cloths_in_box:

    if cloths_in_box[len(cloths_in_box)-1] <= next_rack_capacity:
        next_rack_capacity -= cloths_in_box.pop()

    elif cloths_in_box[len(cloths_in_box)-1] > next_rack_capacity:
        next_rack_capacity = rack_capacity
        total_racks += 1
        next_rack_capacity -= cloths_in_box.pop()

if next_rack_capacity != 16:
    total_racks += 1

print(total_racks)
