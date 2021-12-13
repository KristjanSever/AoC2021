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
for fold in fo:
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


dots = [['.' for _ in range(paperY+1)] for _ in range(paperX+1)]
distinctPoints = {}
for point in points:
    distinctPoints[str(point[0])+','+str(point[1])] = point
    dots[point[0]][point[1]] = '#'


for i, _ in enumerate(dots[0]):
    row = ''
    for j, _ in enumerate(dots):
        row += dots[j][i]
    print(row)
        
        

