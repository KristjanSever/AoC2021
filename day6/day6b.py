f = open('input.txt','r')

l = [int(x) for x in f.read().split(',')]
left = dict()
for el in l:
    if el in left:
        left[el] += 1
    else:
        left[el] = 1

for day in range(256):
    new = dict()
    for key in left:
        if key == 0:
            new[6] = left[key]
            new[8] = left[key]
            
        else:
            if key - 1 in new:   
                new[key - 1] += left[key]
            else:
                new[key - 1] = left[key]
    left = new
    
s = 0
for key in left:
    s += left[key]
print(s)
