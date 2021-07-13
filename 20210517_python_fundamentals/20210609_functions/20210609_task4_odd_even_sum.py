# Task 4. Odd and Even Sum of individual numbers in a given number
def sum_odd_even(my_number):
    my_string = str(my_number)
    sum_of_even_digits = 0
    sum_of_odd_digits = 0

    for i in range(0, len(my_string)):
        my_int = int(my_string[i])
        if my_int % 2 == 0:
            sum_of_even_digits += my_int
        else:
            sum_of_odd_digits += my_int

    return f"Odd sum = {sum_of_odd_digits}, Even sum = {sum_of_even_digits}"


number = int(input())
print(sum_odd_even(number))
