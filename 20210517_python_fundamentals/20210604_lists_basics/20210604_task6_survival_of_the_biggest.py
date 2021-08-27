# Task 6 - Survival of the biggest
my_values_list = []
my_values_list = input().split(" ")
count_of_numbers_to_remove = int(input())
my_step = 1
my_output = ''

for i in range(0, len(my_values_list)):
    my_values_list[i] = int(my_values_list[i])
# my_values_list.sort(reverse=True)
#
# for i in range(len(my_values_list)-1, 0, -1):
#     my_values_list.remove(my_values_list[i])
#     if my_step == count_of_numbers_to_remove:
#         break
#     my_step += 1

for i in range(1, count_of_numbers_to_remove + 1):
    my_values_list.remove(min(my_values_list))

for i in range(0, len(my_values_list)):
    if i != len(my_values_list) - 1:
        my_output += str(my_values_list[i]) + ", "
    else:
        my_output += str(my_values_list[i])

print(my_output)
