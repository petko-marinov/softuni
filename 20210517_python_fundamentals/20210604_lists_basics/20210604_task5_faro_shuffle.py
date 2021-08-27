# Task 5 - Faro Shuffle
cards_list = []
cards_list = input().split(" ")
number_of_shuffles = int(input())
shuffles_list = []

for j in range(1, number_of_shuffles + 1):

    shuffles_list = []

    for i in range(0, int(len(cards_list) / 2)):

        shuffles_list.append(cards_list[i])
        shuffles_list.append(cards_list[i + int(len(cards_list) / 2)])

    cards_list = []
    cards_list = shuffles_list

print(shuffles_list)
