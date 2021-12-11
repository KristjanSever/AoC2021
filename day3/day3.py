f = open("input.txt", "r")
epsilon = ''
gamma = ''
dolzina = -1
source = f.read()
length = source.find('\n')
lines = len(source[::length])
source = source.replace('\n', '')
lines = len(source[::length])
for k in range(0,length):
    print(source[k:len(source):length].count('1') + source[k:len(source):length].count('0'), lines/2)
    if source[k:len(source):length].count('1') > lines / 2:
        gamma+='1'
        epsilon+='0'
    else:
        gamma+='0'
        epsilon+='1'
print(epsilon, gamma)
print(int(epsilon,2)*int(gamma,2))
