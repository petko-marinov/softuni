# Task 3 - Deposits Calculator
deposit = int(input())
months = int(input())
interest_rate = float(input())/100
total = deposit + (months * ((deposit * interest_rate)/12))
print(total)
