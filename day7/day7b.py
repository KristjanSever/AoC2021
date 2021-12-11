from collections import Counter
f = open('input.txt','r')

source = [int(x) for x in f.read().split(',')]
minimum = min(source)
maximum = max(source)
setSource = Counter(source)
print(minimum, ' minimum,' , maximum, ' maximum')

curMin = maximum * maximum * maximum * maximum
for depth in range(minimum, maximum):
    tmpSum = 0 
    for key in setSource:
        dif = abs(key - depth)
        firstN = (dif*(dif+1))/2
        tmpSum += firstN * setSource[key]
    
    if tmpSum < curMin:
        curMin = tmpSum
print(curMin)

