# Task 1 - Aladdin's Gifts
from collections import deque


def presents(my_value):
    if 100 <= my_value <= 199:
        return "Gemstone"
    elif 200 <= my_value <= 299:
        return "Porcelain Sculpture"
    elif 300 <= my_value <= 399:
        return "Gold"
    elif 400 <= my_value <= 499:
        return "Diamond Jewellery"
    else:
        return None


materials_list = input().split(" ")
magic_level_list = input().split(" ")
present_sum = 0
present_dict = {}

for i in range(0, len(materials_list)):
    materials_list[i] = int(materials_list[i])

for i in range(0, len(magic_level_list)):
    magic_level_list[i] = int(magic_level_list[i])

magic_level_deque = deque(magic_level_list)

while len(materials_list) > 0 and len(magic_level_deque) > 0:
    present_sum = materials_list[-1] + magic_level_deque[0]
    if 100 <= present_sum <= 499:
        present = presents(present_sum)

        if present is not None:
            if present in present_dict:
                present_dict[present] += 1
            else:
                present_dict.update({present: 1})

    elif present_sum < 100:
        if present_sum % 2 == 0:
            present_sum = (materials_list[-1]) * 2 + (magic_level_deque[0] * 3)
        else:
            present_sum = present_sum * 2

        present = presents(present_sum)
        if present is not None:
            if present in present_dict:
                present_dict[present] += 1
            else:
                present_dict.update({present: 1})

    elif present_sum > 499:
        present_sum = present_sum / 2
        present = presents(present_sum)
        if present is not None:
            if present in present_dict:
                present_dict[present] += 1
            else:
                present_dict.update({present: 1})

    materials_list.pop()
    magic_level_deque.popleft()


if ("Gemstone" in present_dict and "Porcelain Sculpture" in present_dict) or \
            ("Gold" in present_dict and "Diamond Jewellery" in present_dict):
    print("The wedding presents are made!")
else:
    print("Aladdin does not have enough wedding presents.")

if len(materials_list) > 0:
    materials_list_str = [str(int) for int in materials_list]
    message = "Materials left: " + ", ".join(materials_list_str)
    print(message)
if len(magic_level_deque) > 0:
    magic_level_deque_str = [str(int) for int in magic_level_deque]
    message = "Magic left: " + ", ".join(magic_level_deque_str)
    print(message)

for key, value in present_dict.items():
    print(f"{key}: {value}")
