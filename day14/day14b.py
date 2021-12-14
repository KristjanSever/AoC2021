import math
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

dictOfPairs = {}
for i in range(0, len(source) - 1):
        el1,el2 = source[i],source[i+1]
        if el1+el2 in dictOfPairs.keys():  
            dictOfPairs[el1+el2] += 1
        else:
            dictOfPairs[el1+el2] = 1

for step in range(0, 40):
    newDict = {}
    for pair in orders:
        if pair[0] in dictOfPairs.keys():
            tmp = [c for c in pair[0]]
            new1, new2 = tmp[0] + pair[1], pair[1] + tmp[1]

            if new1 in newDict.keys():  
                newDict[new1] += dictOfPairs[pair[0]]
            else:
                newDict[new1] = dictOfPairs[pair[0]]
            if new2 in newDict.keys():  
                newDict[new2] += dictOfPairs[pair[0]]
            else:
                newDict[new2] = dictOfPairs[pair[0]]
            del dictOfPairs[pair[0]]
                 
    dictOfPairs = newDict  

print(dictOfPairs)

chars = {}
for key in dictOfPairs:
    tmp = [c for c in key]
    if tmp[0] in chars:
        chars[tmp[0]] += dictOfPairs[key]
    else:
        chars[tmp[0]] = dictOfPairs[key]
    if tmp[1] in chars:
        chars[tmp[1]] += dictOfPairs[key]
    else:
        chars[tmp[1]] = dictOfPairs[key]
        
v=list(chars.values())
k=list(chars.keys())
maximum = math.ceil(chars[k[v.index(max(v))]] / 2)
minimum = math.ceil(chars[k[v.index(min(v))]] / 2)
print(maximum-minimum)
