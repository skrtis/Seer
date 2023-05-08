t = open('table.txt','r').read().split('\n')
data = open('data.txt','r').read()
#read table, place values into 2D array
ref = [i.split(' ') for i in t]

#read data, place every 3 values into list
n=3 #step is 3
grouped = [data[i:i+n] for i in range(0,len(data),n)] 

fin=''
for x in grouped: #for every 3 letter code
    for i in ref: #for every code stored in 2d array
        if x == i[0] and i[1]!='Stop': #compare if they're the same and if they're not a stop codon
            fin+=i[1] #add the attributed letter from the array to a string
print(fin)
