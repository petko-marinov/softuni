# Task 2 - Multiples list
factor = int(input())
count = int(input())
my_list = []

for i in range(1, count + 1):
    my_list.append(i * factor)

my_list.sort()
print(my_list)
