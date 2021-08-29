# Task 1 - Count chars in string
my_char = input()
my_dict = {}

for i in range(0, len(my_char)):
    if my_char[i] != ' ':
        if my_char[i] in my_dict.keys():
            my_dict[my_char[i]] += 1
        else:
            my_dict[my_char[i]] = 1

for key, value in my_dict.items():
    print(f'{key} -> {value}')
