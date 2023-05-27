#EMBL format keeps annotations with the gene data
import math
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
    #information collection
    des = []
    print('CREATING NEWFILE...')
    DEnums=int(input("# of Description lines needed: "))
    for x in range(DEnums):
        des.append(input("Enter Description: "))
    acc=input("Accession number: ") #find accession number

    #Collecting sequence information: Sequence # BP; # A; # C; # G; # T; # other;
    m = {'A':0,'C':0,'G':0,'T':0} #nucleotide dictionary
    for i in d[key]:
        if i in m:
            m[i] += 1

    tenslist = []
    x,y=0,10

    for i in range(math.floor(len(d[key])/10)):
        tenslist.append(d[key][x:y])
        x += 10
        y += 10
    tenslist.append(d[key][y-10:])


    #printing the file
    print('ID '+key[1:]) #ID first line
    print('XX')
    print("AC "+acc)
    print("XX")
    for i in range(len(des)):
        print("DE "+des[i])
    print("XX")

    #number of each:
    A = str(m['A'])
    C = str(m['C'])
    T = str(m['T'])
    G = str(m['G']) 

    print('SQ '+"Sequence "+str(len(d[key]))+" BP; "+A+" A; "+C+' C; '+G+' G; '+T+" T;")

    cur = 0
    length = 0
    print('   ',end='')
    for i in tenslist:
        length +=len(i)
        cur +=1
        print(i.lower() + ' ',end='')
        if cur%6 == 0 and cur != len(tenslist):
            print(' '+str(length))
            print('   ',end='')
        elif cur%6==0 and cur == len(tenslist):
            print(' '+str(length),end='')
            length = 0
    print("\n//")