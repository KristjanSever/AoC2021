def trans(line):
    line = [[char,index] for index, char in enumerate(line)]
    return line
def delRight(line,i):
    if i > len(line) - 1:
        return line
    else:
        if line[i-1][0] == '(' and line[i][0] == ')':
            line.pop(i)
            line.pop(i-1)
            return delRight(line,0)
        elif line[i-1][0] == '[' and line[i][0] == ']':
            line.pop(i)
            line.pop(i-1)
            return delRight(line,0)
        elif line[i-1][0] == '{' and line[i][0] == '}':
            line.pop(i)
            line.pop(i-1)
            return delRight(line,0)
        elif line[i-1][0] == '<' and line[i][0] == '>':
            line.pop(i)
            line.pop(i-1)
            return delRight(line,0)
        else:
            return delRight(line,i+1)

with open("input.txt", 'r') as f:
    lines = [line.strip() for line in f]

s = 0
for line in lines:
    l = delRight(trans(line),0)
    print(l)
    for el in l:
        if el[0] == ')':
            s+=3
            break
        if el[0] == ']':
            s+=57
            break
        if el[0]== '}':
            s+=1197
            break
        if el[0] == '>':
            s+=25137
            break
        
print(s)
