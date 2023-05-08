data = open('data.txt','r').read().split('\n')
strand = data[0]
ans =''
n=len(data[1])
for i in range(len(strand)):
    if data[1] == strand[i:i+n]:
        if ans == '':
            ans += str(i+1)
        else: 
            ans += ' '+str(i+1)
print(ans) 