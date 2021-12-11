f = open('input.txt','r')

s = 0
for line in f:
    digs = line.rstrip().split(' | ')[1].split(' ')
    for d in digs:
        print(d)
        #1,2 4,4 7,3 8,7
        if len(d) == 2 or len(d) == 4 or len(d) == 3 or len(d) == 7:
            s += 1

print(s)
