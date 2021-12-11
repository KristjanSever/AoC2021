with open("input.txt", 'r') as f:
    lines = [[int(char) for char in line.strip()] for line in f]
print(len(lines))

count = 0
c = 0
for i in range(0,len(lines)):
    for j in range(0,len(lines[0])):
        bottom = True
        c = c+1
        if i != 0:
            bottom = bottom and lines[i-1][j] > lines[i][j]
        if i != len(lines) - 1:
            bottom = bottom and lines[i+1][j] > lines[i][j]
        if j != 0:
            bottom = bottom and lines[i][j-1] > lines[i][j]
        if j != len(lines) - 1:
            bottom = bottom and lines[i][j+1] > lines[i][j]
        if bottom:
            count += 1 + lines[i][j]
print(count)
