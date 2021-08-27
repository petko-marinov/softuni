# Task 7 - Easter gifts
gifts_list = input().split(" ")
received_commands = ''
next_received_command = 0
next_received_gift = 0
received_index = 0

while received_commands != "No Money":
    received_commands = input()
    next_received_command = ''
    next_received_gift = ''
    received_index = 0

    if "OutOfStock" in received_commands:
        next_received_command = received_commands.split(" ")[0]
        next_received_gift = received_commands.split(" ")[1]

        for j in range(0, len(gifts_list)):
            if gifts_list[j] == next_received_gift:
                gifts_list[j] = "None"

    elif "Required" in received_commands:
        next_received_command = received_commands.split(" ")[0]
        next_received_gift = received_commands.split(" ")[1]
        received_index = int(received_commands.split(" ")[2])

        if 0 <= received_index <= len(gifts_list) - 1:
            gifts_list[received_index] = next_received_gift

    elif "JustInCase" in received_commands:
        next_received_command = received_commands.split(" ")[0]
        next_received_gift = received_commands.split(" ")[1]
        gifts_list[-1] = next_received_gift

while "None" in gifts_list:
    gifts_list.remove("None")

print(" ".join(gifts_list))
