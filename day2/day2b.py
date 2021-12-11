f = open("inputday2.txt", "r")
forward = 0
depth = 0
aim = 0

for line in f:
    line = line.split(" ")
    command = line[0]
    num = int(line[1])
    if command == 'down':
        aim = aim + num
    if command == 'up':
        aim = aim - num

    if command == 'forward':
        forward = forward + num
        depth = depth + aim * num

print(depth* forward)
