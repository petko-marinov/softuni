# Task 6 - Donation campaign
campaign_duration_days = int(input())
chefs = int(input())
cake_number = int(input())
gofrets_number = int(input())
pancacks_number = int(input())


total_income_cakes = cake_number * 45
total_income_gofrets = gofrets_number * 5.80
total_income_pancacks = pancacks_number * 3.20
total_income_per_day = (total_income_cakes + total_income_gofrets + total_income_pancacks) * chefs
total_income_campaign = total_income_per_day * campaign_duration_days
total_donation = total_income_campaign - total_income_campaign * 1 / 8

print(total_donation)
