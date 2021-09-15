# Task 2  - Stacked Queries
lines = int(input())
command = []
ss = []
output = ''

while lines > 0:
    command = input().split(" ")
    if command[0] == "1":
        ss.append(int(command[1]))

    elif command[0] == "2" and len(ss) > 0:
        ss.pop()

    elif command[0] == "3" and len(ss) > 0:
        print(max(ss))

    elif command[0] == "4" and len(ss) > 0:
        print(min(ss))

    lines -= 1

while ss:
    if len(ss) == 1:
        output += str(ss.pop())
    else:
        output += str(ss.pop()) + ", "

print(output)





