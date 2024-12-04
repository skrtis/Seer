f = open('fasta.txt',"r")
f = f.read().split('\n')
d ={}
cur = '' #use current variable as storage for temp key in dictionary 
for x in f:
    if x[0] == '>':
        cur = x
        d[x] = '' #new key
    elif x[0] != '>':
        d[cur] += x

for key in d:
    print(d[key]+';',end='')
