# Task 8
length = int(input())
width = int(input())
hight = int(input())
used_share = float(input()) * 0.01

volume = (length * width * hight) * 0.001 * (1 - used_share)

print(volume)
