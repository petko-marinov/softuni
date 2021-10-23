# Task 2 - Dart

players_list = input().split(", ")
players_scores = [501, 501]
board_md = []
is_game_end = True
command = ""
throw_position = [0, 0]
loop = 0
total_throws = 0

for i in range(0, 7):
    board_md.append(input().split(" "))

while is_game_end:
    throw_output = 0
    temp_score = 0
    command = input().split(", ")
    command[0] = command[0].replace("(", "")
    command[1] = command[1].replace(")", "")
    throw_position[0] = (int(command[0]))
    throw_position[1] = (int(command[1]))

    if loop % 2 == 0:
        player_id = 0
    else:
        player_id = 1
        total_throws += 1

    if throw_position[0] > 6 and throw_position[1] > 6:
        break

    throw_output = board_md[throw_position[0]][throw_position[1]]
    # print(throw_output)

    if throw_output.isdigit():
        players_scores[player_id] -= int(throw_output)
    else:
        if throw_output == "D":
            temp_score = (int(board_md[0][throw_position[1]]) +
                          int(board_md[6][throw_position[1]]) +
                          int(board_md[throw_position[0]][0]) +
                          int(board_md[throw_position[0]][6])
                          ) * 2
            players_scores[player_id] -= temp_score

        elif throw_output == "T":
            temp_score = (int(board_md[0][throw_position[1]]) +
                          int(board_md[6][throw_position[1]]) +
                          int(board_md[throw_position[0]][0]) +
                          int(board_md[throw_position[0]][6])
                          ) * 3
            players_scores[player_id] -= temp_score

        elif throw_output == "B":
            players_scores[player_id] = 0
            total_throws = 1

    if players_scores[0] <= 0 or players_scores[1] <= 0:
        is_game_end = False
    else:
        loop += 1


print(f"{players_list[player_id]} won the game with {total_throws} throws!")



