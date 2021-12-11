f = open("input.txt", "r")
first = True
previous = -1
increased = 0
decreased = 0
count=0
for line in f:
    if first:
        first = False;
        previous = int(line)
    else:
        if int(line) - previous > 0:
            increased = increased + 1
            count = count + 1
        previous = int(line)
            
print(increased)
print(count)
