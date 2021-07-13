# Task 3 - Characters in Range
def my_range(string_1: str, string_2: str):
    my_ascii_list = []
    ascii_dec_start = int(ord(string_1))
    ascii_dec_end = int(ord(string_2))

    for i in range(ascii_dec_start + 1, ascii_dec_end):
        my_ascii_list.append(chr(i))

    return my_ascii_list


str_character_1 = input()
str_character_2 = input()
print(" " . join(my_range(str_character_1, str_character_2)))
