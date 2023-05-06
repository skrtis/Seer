from flask import Blueprint, render_template, request
import re

##FIBONACCI ALGORITHM
fib = Blueprint('fib', __name__)
cnucleotides = Blueprint('cnucleotides', __name__)
gccontent = Blueprint('gc', __name__)

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

@gccontent.route('/gccontent', methods=['GET', 'POST'])
def gc_content():
    if request.method == 'POST':
        fasta_file = request.files['fasta_file']
        fasta_data = fasta_file.read().decode('utf-8')
        fasta_seqs = re.findall(r'>.+?\n([A-Za-z\n]+)', fasta_data, re.DOTALL)
        d = {}
        for seq in fasta_seqs:
            seq = seq.replace('\n', '')
            gc_content = ((seq.count('G') + seq.count('C')) / len(seq)) * 100
            header = re.search(r'>(.+?)\n', fasta_data).group(1)
            d[header] = gc_content
        max_gc = max(d.items(), key=lambda x: x[1])
        return render_template('gccontent.html', max_gc=max_gc)
    return render_template('gccontent.html')