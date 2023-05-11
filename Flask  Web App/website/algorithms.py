from flask import Blueprint, render_template, request
import re

##FIBONACCI ALGORITHM
fib = Blueprint('fib', __name__)
cnucleotides = Blueprint('cnucleotides', __name__)
gc = Blueprint('gc', __name__)
consensus = Blueprint('consensus',__name__)
hamming = Blueprint('hamming',__name__)

@fib.route('/fibonacci', methods=['GET', 'POST'])
def fibonacci():
    if request.method == 'POST':
        n = int(request.form['n'])
        k = int(request.form['k'])
        # Run the Fibonacci algorithm
        # initialize n-1 and n-2
        nm1, nm2 = 1,1
        fin = 0
        # iterate through generations
        for i in range(n-2):
            fin = nm1 + (k*nm2)
            nm2 = nm1
            nm1 = fin
        # Render the template with the output
        return render_template('fibonacci.html', result=fin)
    return render_template('fibonacci.html')


@cnucleotides.route('/counting-nucleotides', methods=['GET','POST'])
#Counting DNA Nucleotides
def countingnucleotides():
    if request.method == 'POST':
        strand = request.form['strand']
        m = {}
        for i in strand:
            if i not in m:
                m[i]=0
            if i in m:
                m[i] += 1
        a,c,t,g = str(m['A']),str(m['C']),str(m['G']),str(m['T'])
        return render_template('countingnucleotides.html', a=a,c=c,t=t,g=g)
    return render_template('countingnucleotides.html')

@gc.route('/gccontent', methods=['GET', 'POST'])
def gc_content():
    if request.method == 'POST':
        fasta_file = request.files['fasta_file']
        fasta_data = fasta_file.read().decode('utf8').split('\n')
        d ={}
        cur = '' #use current variable as storage for temp key in dictionary 
        for x in fasta_data:
            if x[0] == '>':
                cur = x
                d[x] = '' #new key
            elif x[0] != '>':
                d[cur] += x
        for key in d:
            x = d[key]
            gc = 0
            for i in x:
                if i == 'G' or i == 'C':
                    gc += 1
            gc = (gc*100)/len(x)
            d[key] = gc
        max_key = max(d, key=d.get) 
        max_key= str(max_key).replace('>','')
        max_val= str(round(max(d.values()), 6))
        return render_template('gccontent.html',max_key=max_key, max_val=max_val)
    return render_template('gccontent.html')

@consensus.route('/consensus',methods=['GET','POST'])
def consensus_profile():
    if request.method == 'POST':
    #read fasta file, store into list instead of dictionary and assemble profile matrix mxn, where m is length of string, n is number of strings
        fasta_file = request.files['fasta_file']
        fasta_data = fasta_file.read().decode('utf8').split('\n')
        #read fasta file
        cur = ''
        matrix=[]
        for x in fasta_data:
            if x[0] == '>':
                matrix.append(cur) #append current to list
                cur=''
            elif x[0]!='>':
                cur+=x
        matrix.append(cur) #append last value
        del matrix[0] #delete blank object at start of list

        consensus = [] #consensus string stored in list
        #formatting actg strings to print matrix
        A = []
        C = []
        G = []
        T = []

        a,c,g,t = 0,0,0,0 #initialize vars
        for x in range(len(matrix[0])):    
            for i in matrix: #count the nucleotides for each index of each object in list
                if i[x] == 'A':
                    a+=1
                elif i[x] == 'C':
                    c+=1
                elif i[x] == 'G':
                    g+=1
                elif i[x] == 'T':
                    t+=1
            A.append(a)
            C.append(c)
            G.append(g)
            T.append(t)
            x = max(a,c,t,g)
            if x == a:
                consensus.append('A')
            elif x == c:
                consensus.append('C')
            elif x == g:
                consensus.append('G')
            elif x == t:
                consensus.append('T') 
            a,c,t,g = 0,0,0,0 #reinitialize vars

        #formatting and printing (iterate through each list)
        fin, fina, finc, fing, fint = '', '', '','',''
        for i in consensus:
            fin += i
        print(fin)

        for i in A:
            fina +=str(i)
            fina +=' '
        fina = 'A: '+fina.rstrip()

        for i in C:
            finc +=str(i)
            finc +=' '
        finc = 'C: '+finc.rstrip()

        for i in G:
            fing +=str(i)
            fing +=' '
        fing = 'G: '+fing.rstrip()

        for i in T:
            fint +=str(i)
            fint +=' '
        fint = 'T: '+fint.rstrip()
        return render_template('consensus.html', fin = fin, fina=fina, finc=finc, fing=fing,fint=fint)
    return render_template('consensus.html')

@hamming.route('/hamming',methods=['GET','POST'])
def hamming_dist():
    if request.method == 'POST':
        f = open('rosalind_hamm.txt','r').read().split('\n')
        c = 0
        for i in range(len(f[1])):
            if f[0][i]!= f[1][i]:
                c += 1
        return render_template('hamming.html', c=c)
    return render_template('hamming.html')