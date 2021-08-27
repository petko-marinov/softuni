# Task 4 - Number beggars
my_list = []
my_list = input().split(", ")
beggars = int(input())
sum_1 = 0
output_list = []

for i in range(0, beggars):
    sum_1 = 0
    for j in range(i, len(my_list), beggars):
        # print(my_list[j])
        sum_1 += int(my_list[j])

    output_list.append(sum_1)

print(output_list)
