# Task 2 - A miner task
command = ''
command_odd = ''
command_even = 0
lopper = 0
my_resources = {}

while command != "stop":
    command = input()
    lopper += 1

    if lopper % 2 == 0:
        command_even = int(command)
        my_resources[command_odd] += command_even

    elif command != "stop":
        command_odd = str(command)
        if command_odd in my_resources.keys():
            pass
        else:
            my_resources[command_odd] = 0

for key, value in my_resources.items():
    print(f'{key} -> {value}')
