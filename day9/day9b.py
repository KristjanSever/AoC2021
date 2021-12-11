def findBasinSize(x,y,lines,checked):
    if lines[x][y] == 9:
        return 0
    else:
        size = 1
        if x != len(lines) - 1 and not checked[x+1][y]:
            checked[x+1][y] = True
            size += findBasinSize(x+1,y,lines,checked)
        if x != 0 and not checked[x-1][y]:
            checked[x-1][y] = True
            size += findBasinSize(x-1,y,lines,checked)
        if y != len(lines[0]) - 1 and not checked[x][y+1]:
            checked[x][y+1] = True
            size += findBasinSize(x,y + 1,lines,checked)
        if y != 0 and not checked[x][y-1]:
            checked[x][y-1] = True
            size += findBasinSize(x,y - 1,lines,checked)
            
        return size

with open("input.txt", 'r') as f:
    lines = [[int(char) for char in line.strip()] for line in f]
checked = [[False for i in range(0,len(lines[0]))] for j in range(0,len(lines))]


largest3 = [0,0,0]
for i in range(0,len(lines)):
    for j in range(0, len(lines[0])):
        size = findBasinSize(i,j,lines,checked) - 1
        if size != 0:
            largest3.sort()
            if size > largest3[0]:
                largest3[0] = size
                
      
print('over', largest3)
print(largest3[0] * largest3[1] * largest3[2] )
        
