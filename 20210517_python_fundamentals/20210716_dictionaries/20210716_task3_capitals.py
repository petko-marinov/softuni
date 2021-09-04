# Task 3 - Capitals
countries = {}
list_countries = input().split(", ")
list_capitals = input().split(", ")

countries = dict(zip(list_countries, list_capitals))

for key, value in countries.items():
    print(f'{key} -> {value}')
