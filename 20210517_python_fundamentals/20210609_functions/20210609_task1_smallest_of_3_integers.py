# Task 1 - Smallest of Three Numbers
def min_range(int_list):
    result = min(int_list)
    return result


parameter_1 = int(input())
parameter_2 = int(input())
parameter_3 = int(input())

my_list = [parameter_1, parameter_2, parameter_3]

print(min_range(my_list))
