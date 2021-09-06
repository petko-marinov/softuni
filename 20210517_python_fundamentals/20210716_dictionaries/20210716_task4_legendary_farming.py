# Task 4 - Legendary farming
my_dict = {}
is_obtained = False
key_obtained = ''
key_obtained_name = ''

while is_obtained == False:
    command = []
    command = input().split(" ")
    # print(command)

    for i in range(1, len(command), 2):
        if command[i].lower() not in my_dict.keys():
            my_dict[command[i].lower()] = 0 + int(command[i-1])
        else:
            my_dict[command[i].lower()] += int(command[i-1])

        if my_dict[command[i].lower()] >= 250 and command[i].lower() == "shards":
            is_obtained = True
            key_obtained = "Shadowmourne"
            my_dict[command[i].lower()] -= 250
            key_obtained_name = "shards"
            break
        elif my_dict[command[i].lower()] >= 250 and command[i].lower() == "fragments":
            is_obtained = True
            key_obtained = "Valanyr"
            my_dict[command[i].lower()] -= 250
            key_obtained_name = "fragments"
            break
        elif my_dict[command[i].lower()] >= 250 and command[i].lower() == "motes":
            is_obtained = True
            key_obtained = "Dragonwrath"
            my_dict[command[i].lower()] -= 250
            key_obtained_name = "motes"
            break
    # print(my_dict)

# you did it - sorting by value desc and key asc
sorted_dict = dict(sorted(my_dict.items(), key=lambda x: (-x[1], x[0])))

print(f'{key_obtained} obtained!')
for key, value in sorted_dict.items():
    if key == "shards" or key == "fragments" or key == "motes":
        # legendary_dict[key] = value
        print(f'{key}: {value}')

# you did it - sorting by value desc and key asc
sorted_dict = dict(sorted(my_dict.items(), key=lambda x: x[0]))
for key, value in sorted_dict.items():
    if key != key_obtained_name:
        # junk_dict[key] = value
        print(f'{key}: {value}')
