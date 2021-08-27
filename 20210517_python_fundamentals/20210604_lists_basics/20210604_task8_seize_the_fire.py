# Task 8 - seize the fire
input_data = (input().split("#"))
int_water = int(input())
list_of_fires = []
type_of_fire = []
extinguished_cells = []
total_effort = 0.00
total_fire = 0

for i in range(0, len(input_data)):
    type_of_fire = input_data[i].split(" = ")
    # type of fire
    type_of_fire[0] = type_of_fire[0]
    # water needed
    type_of_fire[1] = int(type_of_fire[1])

    # str type of fire
    list_of_fires.append(type_of_fire[0])
    # int water needed
    list_of_fires.append(type_of_fire[1])

for i in range(0, len(list_of_fires), 2):

    if int_water >= list_of_fires[i + 1]:

        if list_of_fires[i] == "High":
            if 81 <= list_of_fires[i + 1] <= 125:
                extinguished_cells.append(list_of_fires[i + 1])
                int_water -= list_of_fires[i + 1]
                total_effort += list_of_fires[i + 1] * 0.25
                total_fire += list_of_fires[i + 1]
            else:
                continue

        elif list_of_fires[i] == "Medium":
            if 51 <= list_of_fires[i + 1] <= 80:
                extinguished_cells.append(list_of_fires[i + 1])
                int_water -= list_of_fires[i + 1]
                total_effort += list_of_fires[i + 1] * 0.25
                total_fire += list_of_fires[i + 1]
            else:
                continue

        elif list_of_fires[i] == "Low":
            if 1 <= list_of_fires[i + 1] <= 50:
                extinguished_cells.append(list_of_fires[i + 1])
                int_water -= list_of_fires[i + 1]
                total_effort += list_of_fires[i + 1] * 0.25
                total_fire += list_of_fires[i + 1]
            else:
                continue

print("Cells:")
for el in extinguished_cells:
    print(f" - {el}")
print(f"Effort: {total_effort:.2f}")
print(f"Total Fire: {total_fire}")
