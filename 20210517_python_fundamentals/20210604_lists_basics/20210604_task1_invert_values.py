# Task 1 - Invert values
str_list_of_values = input()

values = []
values = str_list_of_values.split(" ")

for i in range(0, len(values)):
    values[i] = int(values[i]) * -1

print(values)
