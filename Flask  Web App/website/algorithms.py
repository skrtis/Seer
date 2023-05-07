from flask import Blueprint, render_template, request
import re

##FIBONACCI ALGORITHM
fib = Blueprint('fib', __name__)
cnucleotides = Blueprint('cnucleotides', __name__)
gc = Blueprint('gc', __name__)

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