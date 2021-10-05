# Task 7 - Robotics
import datetime
from collections import deque

robotics = deque()
sorted_robotics = deque()
production_line = deque()
command = ''
is_empty_command = False

# get robots and processing time
for robot in input().split(';'):
    robot_name = []
    for i in robot.split('-'):
        robot_name.append(i)
    robot_name[1] = int(robot_name[1])
    robotics.append(robot_name)

# get start processing time
start_time_list = [int(x) for x in input().split(':')]
start_time = datetime.datetime(100, 1, 1, start_time_list[0], start_time_list[1], start_time_list[2])
last_time = start_time

for robot in robotics:
    robot.append(start_time)

while True:
    if not is_empty_command and command != 'End':
        command = input()
        if command != 'End':
            production_line.append(command)
    else:
        is_empty_command = True
        if not production_line:
            break

    start_time += datetime.timedelta(seconds=1)

    if robotics[0][2] != last_time:
        sorted_robotics = sorted(robotics, key=lambda x: x[1])
        robotics = deque(sorted_robotics)

    if start_time >= robotics[0][2] and len(production_line) > 0:
        # print(start_time.time())
        robotics[0][2] = start_time + datetime.timedelta(seconds=int(robotics[0][1]))
        print(f'{robotics[0][0]} - {production_line.popleft()} [{start_time.time()}]')
        robotics.append(robotics.popleft())
    else:
        production_line.append(production_line.popleft())

