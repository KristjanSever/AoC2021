class BingoList:
    def __init__(self, rows):
        self.rows = rows
        self.len = len(rows[0])
        self.won = False
        self.remove = False
    def toString(self):
        print(self.rows)
    def check(self, num):
        for r in self.rows:
            if num in r:
                i = r.index(num)
                r[i] = [r[i], 'c']
                try:
                    if all(checked == 'c' for (_, checked) in r):
                        self.won = True
                        return True
                    if all(checked == 'c' for (_, checked) in [el[i%self.len] for el in self.rows]):
                        self.won = True
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

winners = 0
for num in sequence:
    for l in bingoLists:
        l.check(num)
        if l.won and l.remove == False:
            l.remove = True
            winners += 1
            if winners == len(bingoLists):
                s = 0
                for row in l.rows:
                    for el in row:
                        if isinstance(el, str):
                            s += int(el)
                    
                print(int(num) * s)
        
