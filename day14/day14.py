f = open('input.txt','r')
source=[]
orders=[]
for index, line in enumerate(f):
    if index == 0:
        source = [c for c in line.rstrip()]
    elif index == 1:
        continue
    else:
        order = line.rstrip().split(' -> ')
        orders.append(order)

for step in range(0,10):
    temp = source
    inserted = False
    for i in range(len(source) - 2, -1, -1):
        el1,el2 = source[i],source[i+1]
        for pair in orders:
            ord1,ord2 = [c for c in pair[0]]
            if el1 == ord1 and el2 == ord2:
                inserted = True
                source = source[:i+1] + [pair[1]] + source[i+1:]
        

#must be a way to do this simpler, but its near bed time haha    
res = dict((x,source.count(x)) for x in set(source))
v=list(res.values())
k=list(res.keys())
maximum = res[k[v.index(max(v))]]
minimum = res[k[v.index(min(v))]]

print(maximum-minimum)
