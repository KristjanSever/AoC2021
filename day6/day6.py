f = open('input.txt','r')

l = [int(x) for x in f.read().split(',')]

for i in range(80):
    for idx in range(0, len(l)):
        if l[idx] > 0:
            l[idx] -= 1
        else:
            l.append(8)
            l[idx] = 6


print(len(l))
