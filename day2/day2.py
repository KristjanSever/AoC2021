f = open("inputday2.txt", "r")
forward = 0
down = 0
up = 0
for line in f:
    line = line.split(" ")
    command = line[0]
    num = int(line[1])
    if command == 'forward':
        print(str(forward) + 'forward')
        forward = forward + num
    if command == 'up':
        print(str(up) + "up")
        up = up + num
    if command == 'down':
        print(str(down) + "down")
        down = down + num

depth = down - up

print(forward*depth)
