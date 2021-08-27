# Task 3 - Football cards
input_text = input()
list_of_cards_all = input_text.split(" ")
list_of_cards = []

for i in range(0, len(list_of_cards_all)):
    if list_of_cards_all[i] not in list_of_cards:
        list_of_cards.append(list_of_cards_all[i])

# print(list_of_cards)
players_in_team_a = 11
players_in_team_b = 11
card = ""

for i in range(0, len(list_of_cards)):
    card = list_of_cards[i].split("-")
    # print(card)
    if card[0] == "A":
        players_in_team_a -= 1
    elif card[0] == "B":
        players_in_team_b -= 1
    if players_in_team_a < 7 or players_in_team_b < 7:
        break


print(f"Team A - {players_in_team_a}; Team B - {players_in_team_b}")
if players_in_team_a < 7 or players_in_team_b < 7:
    print(f"Game was terminated")
