# Task 5. Palindrome Integers Function
def palindrome_integers(my_list):
    my_validations_list = []

    for i in range(0, len(my_list)):
        if my_list[i] == my_list[i][::-1]:
            my_validations_list.append("True")
        else:
            my_validations_list.append("False")
    return my_validations_list


integers_list = []
integers_list = input().split(", ")

print("\n".join(palindrome_integers(integers_list)))
