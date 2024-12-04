import re

f = open('embl.txt',"r")
f = f.read().split('\n')
#store sequence and fasta data and additional information
accession = ''
idstr = ''
definition =[]
seq = []
for i in f: 
    if i[0]=='I' and i[1]=='D':
        idstr = i[2:]
    if i[0]==' ':
        seq.append(i)
    if i[0]=='D' and i[1]=='E':
        definition.append(i)
    if i[0] =='A' and i[1] == 'C':
        accession = i

#iterate and refine the strings list
pattern ='[0-9]'
newseq=[z.replace(' ','') for z in seq]
refinedseq=[re.sub(pattern,'',i).upper() for i in newseq]
print(">"+idstr)
print(''.join(refinedseq))