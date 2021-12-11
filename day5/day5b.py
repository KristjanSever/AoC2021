f = open('input.txt','r')
l = {}
for line in f:
    line = line.replace('\n', '').split(' -> ')
    x1,y1 = map(int, line[0].split(','))
    x2,y2 = map(int, line[1].split(','))
    directionX = x2 - x1
    directionY = y2 - y1

    steps = max(abs(directionX), abs(directionY)) + 1

    dirX = directionX / (steps - 1)
    dirY = directionY / (steps - 1)
    
    curX, curY = x1, y1
    for i in range (0, steps):
        k = str(curX)+','+str(curY)
        if k in l:
            l[k] = l[k] + 1
        else:
            l[k] = 1
        curX += dirX
        curY += dirY

print(sum(value >= 2 for value in l.values()))

