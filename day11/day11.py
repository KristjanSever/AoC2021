with open("input.txt", 'r') as f:
    lines = [[int(char) for char in line.strip()]for line in f]


def explosion(i,j,lines):
    lines[i][j] = 0
    for n in range(-1,2,1):
        for m in range(-1,2,1):
            if i+n >= 0 and i+n < len(lines):
                if j+m >= 0 and j+m < len(lines[0]):
                    
                        #print(i,j,lines[i+n][j+m])
                        if not lines[i+n][j+m] == 0:
                            lines[i+n][j+m] += 1
                            if lines[i+n][j+m] > 9:
                                explosion(i+n, j+m, lines)
def countExplosions(lines):
    result = 0
    for i, _ in enumerate(lines):
        line = ''
        for j, _ in enumerate(lines[i]):
            if lines[i][j] == 0:
                result+=1
    return result
explosions = 0
def checkDay(lines):
    for i, _ in enumerate(lines):
        line = ''
        for j, _ in enumerate(lines[i]):
            line += str(lines[i][j])
        print(line)

for day in range(0,100):
    for i, _ in enumerate(lines):
        for j, _ in enumerate(lines[i]):
            lines[i][j] += 1


    for i, _ in enumerate(lines):
        for j, _ in enumerate(lines[i]):
            if lines[i][j] > 9:
                explosion(i,j,lines)
    explosions += countExplosions(lines)
    print(explosions)
    print(checkDay(lines))
    
print(explosions)

