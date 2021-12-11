f = open("input.txt", "r")
first = True
count=0

Data= [];

for line in f:
    Data.append(int(line))
    
            
for i in range(3,len(Data)):
    if Data[i] + Data[i-1] + Data[i-2] > Data[i-1] + Data[i-2] + Data[i-3]:
        count = count + 1
print(count)
