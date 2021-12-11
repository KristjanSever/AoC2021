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
scores = []
for line in lines:
    l = delRight(trans(line),0)
    clean = True
    for el in l:
        if el[0] == ')':
            clean = False
            break
        if el[0] == ']':
            clean = False
            break
        if el[0]== '}':
            clean = False
            break
        if el[0] == '>':
            clean = False
            break
    if clean:
        score = 0
        sol = ''
        for el in l:
            if el[0] == '(':
                sol = ')' + sol
            if el[0] == '[':
                sol = ']' + sol
            if el[0]== '{':
                sol = '}' + sol
            if el[0] == '<':
                sol = '>' + sol
        for char in sol:
            if char == ')':
                score = score * 5 + 1
            elif char == ']':
                score = score * 5 + 2
            elif char == '}':
                score = score * 5 + 3
            elif char == '>':
                score = score * 5 + 4
        scores.append(score)

scores.sort()

print(scores[int(len(scores)/2)])
