f = open('rosalind_hamm.txt','r').read().split('\n')
c = 0
for i in range(len(f[1])):
    if f[0][i]!= f[1][i]:
        c += 1
print(c)


