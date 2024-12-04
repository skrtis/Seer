from flask import Blueprint, render_template, request
import re

#all blueprints defined
fib = Blueprint('fib', __name__)
cnucleotides = Blueprint('cnucleotides', __name__)
gc = Blueprint('gc', __name__)
consensus = Blueprint('consensus',__name__)
hamming = Blueprint('hamming',__name__)
rnatoprotein = Blueprint('rnatoprotein', __name__)
motif = Blueprint('motif', __name__)
transcription = Blueprint('transcription',__name__)
complement = Blueprint('complement',__name__)


@transcription.route('/transcription',methods=['GET','POST'])
def DNAtranscribe():
    if request.method=='POST':
        strand  = request.form['strand']
        strand = strand.replace('T','U')
        return render_template('transcription.html', result = strand )
    return render_template('transcription.html')


@complement.route('/complement',methods=['GET','POST'])
def revcomp():
    if request.method == 'POST':
        strand = request.form['strand']
        strand = strand.replace('A','B').replace('T','A').replace('C','D').replace('G','C').replace('B','T').replace('D','G')
        #All the original As are now Bs #All the original Cs are now Ds
        strand = strand[::-1] #reverses the strand
        return render_template('complement.html', result = strand)
    return render_template('complement.html')

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
        m = {'A':0,'C':0,'G':0,'T':0}  #nucleotide dictionary
        for i in strand:
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
        f = request.files['ham_text'].read().decode('utf8').split('\n')
        c = 0
        for i in range(len(f[1])):
            if f[0][i]!= f[1][i]:
                c += 1
        return render_template('hamming.html', c=c)
    return render_template('hamming.html')

@rnatoprotein.route('/rna-to-protein',methods=['GET','POST'])
def rtp_converter():
    if request.method == 'POST':
        data = request.files['rna'].read().decode('utf8')
        t = ['UUU F', 'CUU L', 'AUU I', 'GUU V', 'UUC F', 'CUC L', 'AUC I', 'GUC V', 'UUA L', 
             'CUA L', 'AUA I', 'GUA V', 'UUG L', 'CUG L', 'AUG M', 'GUG V', 'UCU S', 'CCU P', 
             'ACU T', 'GCU A', 'UCC S', 'CCC P', 'ACC T', 'GCC A', 'UCA S', 'CCA P', 'ACA T', 
             'GCA A', 'UCG S', 'CCG P', 'ACG T', 'GCG A', 'UAU Y', 'CAU H', 'AAU N', 'GAU D', 
             'UAC Y', 'CAC H', 'AAC N', 'GAC D', 'UAA Stop', 'CAA Q', 'AAA K', 'GAA E', 'UAG Stop', 
             'CAG Q', 'AAG K', 'GAG E', 'UGU C', 'CGU R', 'AGU S', 'GGU G', 'UGC C', 'CGC R', 'AGC S', 
             'GGC G', 'UGA Stop', 'CGA R', 'AGA R', 'GGA G', 'UGG W', 'CGG R', 'AGG R', 'GGG G']
        ref = [i.split(' ') for i in t]
        n=3
        grouped = [data[i:i+n] for i in range(0,len(data),n)]
        fin=''
        for x in grouped:
            for i in ref:
                if x == i[0] and i[1]!='Stop':
                    fin+=i[1]
        return render_template('rnatoprotein.html', fin=fin)
    return render_template('rnatoprotein.html')

@motif.route('/motif',methods=['GET','POST'])
def substring_finder():
    if request.method == 'POST':
        data = request.files['motif_text'].read().decode("utf8").split('\n')
        strand = data[0]
        ans =''
        n=len(data[1])
        for i in range(len(strand)):
            if data[1] == strand[i:i+n]:
                if ans == '':
                    ans += str(i+1)
                else: 
                    ans += ' '+str(i+1)
        return render_template('motif.html', ans=ans)
    return render_template('motif.html')
