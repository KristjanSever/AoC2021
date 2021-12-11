f = open("input.txt", "r")
oxygen = ""
co2 = ""
length = -1
source = f.read()
length = source.find('\n')
source = source.split('\n')
source.remove('')
sourceO, sourceC = source, source


for i in range(0,length):
    zerosO, onesO, zerosC, onesC = [], [], [], []
    cO0, cO1, cC0, cC1 = 0, 0, 0, 0
    
    for el in sourceO:
        if(el[i] == '1'):
            onesO.append(el)
        else:
            zerosO.append(el)

    for el in sourceC:
        if(el[i] == '1'):
            onesC.append(el)
        else:
            zerosC.append(el)

    if len(onesO) >= len(zerosO):
        sourceO = onesO
    else:
        sourceO = zerosO
        
    if len(onesC) < len(zerosC):
        sourceC = onesC
    else:
        sourceC = zerosC
    
    if len(sourceO) == 1:
        oxygen = sourceO[0]
    if len(sourceC) == 1:
        co2 = sourceC[0]
    
print(int(oxygen,2) *  int(co2,2))
