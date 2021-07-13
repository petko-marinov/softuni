# Task 2 - Add and Subtract
def add_and_subtract(my_list_1):

    def sum_numbers(my_list_2):
        output2 = my_list_2[0] + my_list_2[1]
        return output2

    def subtract(my_list_3):
        output3 = sum_numbers(my_list_3) - my_list_3[2]
        return output3

    output1 = subtract(my_list_1)
    return output1


my_list = []
for i in range(0, 3):
    int_parameters = int(input())
    my_list.append(int_parameters)

print(add_and_subtract(my_list))
