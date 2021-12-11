from collections import Counter
from numpy import median

f = open('input.txt','r')

source = [int(x) for x in f.read().split(',')]
minimum = min(source)
maximum = max(source)
setSource = Counter(source)

curMin = maximum * maximum
for depth in range(minimum, maximum):
    tmpSum = 0 
    for key in setSource:
        tmpSum += abs(key - depth)* setSource[key]
    
    if tmpSum < curMin:
        curMin = tmpSum
print(curMin)


##
##tmpSum = 0
##a = median(source)
##for key in setSource:
##        tmpSum += abs(key - a)* setSource[key]
##
