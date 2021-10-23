# Task 2 - Ball in the Bucket
board_md = []
command = []
throw_position = [0, 0]
command = [0, 0]
total_points = 0
board_value = ""

for i in range(0, 6):
    board_md.append(input().split(" "))

for throw in range(0, 3):
    string_command = input()
    string_command = string_command.replace("(", "")
    string_command = string_command.replace(")", "")

    command = string_command.split(", ")
    throw_position[0] = (int(command[0]))
    throw_position[1] = (int(command[1]))

    if (throw_position[0] < 0 or throw_position[0] > 5) and (throw_position[1] < 0 or throw_position[1] > 5):
        pass
    else:
        if board_md[throw_position[0]][throw_position[1]] == "B":

            # sum scores in the column
            for i in range(0, 6):
                board_value = board_md[i][throw_position[1]]
                if board_value.isdigit():
                    total_points += int(board_value)

                # remove the bucket
                else:
                    board_md[i][throw_position[1]] = "H"

if 100 <= total_points <= 199:
    prize = "Football"
    print(f"Good job! You scored {total_points} points, and you've won {prize}.")
elif 200 <= total_points <= 299:
    prize = "Teddy Bear"
    print(f"Good job! You scored {total_points} points, and you've won {prize}.")
elif total_points >= 300:
    prize = "Lego Construction Set"
    print(f"Good job! You scored {total_points} points, and you've won {prize}.")
else:
    points = 100 - total_points
    print(f"Sorry! You need {points} points more to win a prize.")