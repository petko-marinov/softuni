# Task 1  - Reverse numbers
command_list = []
output_list = []
command_list = input().split(" ")

while command_list:
    output_list.append(command_list.pop())

print(" ".join(output_list))
