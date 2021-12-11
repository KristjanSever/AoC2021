class BingoList:
    def __init__(self, rows):
        self.rows = rows
        self.len = len(rows[0])
    def toString(self):
        print(self.rows)
    def check(self, num):
        for r in self.rows:
            if num in r:
                i = r.index(num)
                r[i] = [r[i], 'c']
                try:
                    if all(checked == 'c' for (_, checked) in r):
                        return True
                    if all(checked == 'c' for (_, checked) in [el[i%self.len] for el in self.rows]):
                        return True
                except:
                  return False
               
                    
    
    
    
f = open('input.txt','r')
source =[]
for line in f:
    source.append(line.strip())
sequence = source[0].split(',')
bingoLists = []
for i in range(1,len(source),6):
    rows = []
    for j in range(1, 6):
        rows.append(source[i+j].split())
    bingoLists.append(BingoList(rows))

found = False
for num in sequence:
    if not found:
        for l in bingoLists:
            if l.check(num):
                #l is winner, calculate neccessary things
                s = 0
                for row in l.rows:
                    for el in row:
                        if isinstance(el, str):
                            s += int(el)
                
                print(int(num) * s)
                found = True
                break
                           
                                                                                                 

