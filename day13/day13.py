f = open('input.txt', 'r')

points = []
fo = []
folds = False
for line in f:
    if line == '\n':
        folds = True
        continue
    if folds:
        fo.append(line.rstrip().split('fold along ')[1])
    else:
        point = line.rstrip().split(',')
        points.append([int(point[0]),int(point[1])])

print(fo)
print(points)
paperX = float('inf') 
paperY = float('inf') 
for index, fold in enumerate(fo):
    if index == 0:
        tmp = fold.split('=')
        direction = 0 if tmp[0] == 'x' else 1
        size = int(tmp[1])
        if direction == 1 and size < paperY:
            print('papersizeY', size)    
            paperY = size - 1
        elif direction == 0 and size < paperX:
            print('papersizeX', size)   
            paperX = size - 1
                    
        for point in points:
            if point[direction] > size:
                fromFold = point[direction] - size
                point[direction] = size - fromFold
                print('point removed')
distinctPoints = {}
for point in points:
    distinctPoints[str(point[0])+','+str(point[1])] = point
print(len(distinctPoints))
print(paperX, paperY)
print((paperX + 1)* (paperY+1) - len(distinctPoints))
