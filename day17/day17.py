
def inBounds(probe, xBounds, yBounds):
    return probe[0] >= xBounds[0] and probe[0] <= xBounds[1] and probe[1] >= yBounds[0] and probe[1] <= yBounds[1]
def missed(probe, xBounds,yBounds):
    if probe[0] > xBounds[1] or probe[1] < yBounds[0]:
        return True
    return False
def addSpeed(s,direction):
    return [s[0] + direction[0], s[1] + direction[1]]
def getXRange(xBounds):
    n = 1
    while (n *(n+1))/2 < xBounds[0]:
        n+=1
    lowX = n
    n = 1
    highX = 0
    highX = xBounds[1]
    return [lowX, highX]
def getYRange(yBounds):
    highY = - yBounds[0]
    lowY = yBounds[0]
    return [lowY, highY]


    
f = open('input.txt','r')
source = f.read().split('target area: ')[1]
#source = 'target area: x=20..30, y=-10..-5'
x,y = source.split(',')
xBounds = x.split('x=')[1].split('..')
xBounds = [int(xBounds[0]),int(xBounds[1])]
yBounds = y.split('y=')[1].split('..')
yBounds = [int(yBounds[0]),int(yBounds[1])]

#target area: x=150..171, y=-129..-70
S = [0,0]
probe = S
maxHeight = -1
xRange = getXRange(xBounds)
yRange = getYRange(yBounds)
print('xRan', xRange,'yRan', yRange)
print(xBounds, yBounds)
direc = [0,0]
distinct = 0
for tmpX in range(xRange[0], xRange[1]+1):
    for tmpY in range(yRange[0], yRange[1]+1):
        direction = [tmpX,tmpY]
        curH = 0
        probe = S
        while True:
            probe = addSpeed(probe,direction)
            if probe[1] > curH:
                curH = probe[1]
            if inBounds(probe,xBounds,yBounds):
                if curH >= maxHeight:
                    maxHeight = curH
                    direc[0],direc[1] = tmpX,tmpY
                distinct +=1
                break
            if missed(probe,xBounds, yBounds):
                break
            if direction[0] > 0:
                direction[0] -= 1
            elif direction[0] < 0:
                direction[0] += 1
                
            direction[1] -= 1
            
print(distinct)
print(maxHeight)
