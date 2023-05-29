from flask import Blueprint, render_template, request, redirect, url_for, session
import re 
import math 
import os

#formatting name_conversion
plain_fasta = Blueprint('plain_fasta',__name__)
fasta_plain= Blueprint('fasta_plain',__name__)
fasta_embl = Blueprint('fasta_embl',__name__)
embl_fasta = Blueprint('embl_fasta',__name__)


#function naming: name_(first letter of conversion)
@plain_fasta.route('/plain-fasta',methods=['GET','POST'])
def plain_f(): 
    if request.method=='POST':
        #x = input("Enter String(s), split multiple strings with semicolon:")
       # y = int(input("Enter preferred line length: "))
        x = request.files['plain_file'].read().decode('utf8')
        y = int(request.form['linelength'])
        n = request.form['sequence_id']

        #Kurtis's file path
        output_file_path = '/Users/kurtisng/Documents/dev/Seer 1.91/Flask Web App/processed-files/plaintofasta.txt' #filetoconversion.txt
        
        #define nathan's file path here:


        if os.path.exists(output_file_path):
            os.remove(output_file_path)

        with open(output_file_path, 'w') as f:
            f.write(">"+n+'\n') #prints FASTA id
            nums = math.floor(len(x)/y)
            for z in range(nums):
                f.write(x[:y]+'\n')
                x = x.replace(x[:y],'')
            if x != '':
                f.write(x)
        
        #download_link =  f'<a href="/download/plainfasta?file={output_file_path}">Download Output File</a>' 

        return redirect(url_for('plain_fasta_download.downloadplainfasta', file=output_file_path))
    return render_template('plain_fasta.html')

@fasta_plain.route('/fasta-plain', methods=['GET','POST'])
def fasta_p():
    if request.method=='POST':
        f = request.files['fasta_file'].read().decode('utf8').split('\n')
        d ={}
        cur = '' #use current variable as storage for temp key in dictionary 
        for x in f:
            if x[0] == '>':
                cur = x
                d[x] = '' #new key
            elif x[0] != '>':
                d[cur] += x
        
        output_file_path = '/Users/kurtisng/Documents/dev/Seer 1.91/Flask Web App/processed-files/fastatoplain.txt' #filetoconversion.txt

        if os.path.exists(output_file_path):
            os.remove(output_file_path)
        with open(output_file_path, 'w') as f:
            for key in d:
                f.write(d[key]+';')
        with open(output_file_path,'+rb') as h:  
            h.seek(-1,2)
            h.truncate()
        return redirect(url_for('fasta_plain_download.downloadfastaplain', file=output_file_path))
    return render_template('fasta_plain.html')

@fasta_embl.route('/fasta-embl', methods=['GET','POST'])
def fasta_e1():
    if request.method=='POST':
        f = request.files['fasta_file'].read().decode('utf8').split('\n')
        d =[]
        cur = '' #use current variable as storage for temp key in dictionary 
        for x in f:
            d.append(x)

        #information collection
        des = []
        #print('CREATING NEWFILE...')
        des.append(request.form['description1'])
        des.append(request.form['description2']) 
        acc=request.form['accession'] #find accession number


        #Collecting sequence information: Sequence # BP; # A; # C; # G; # T; # other;
        m = {'A':0,'C':0,'G':0,'T':0} #nucleotide dictionary
        for i in d[1]:
            if i in m:
                m[i] += 1

        tenslist = []
        x,y=0,10

        for i in range(math.floor(len(d[1])/10)):
            tenslist.append(d[1][x:y])
            x += 10
            y += 10
        tenslist.append(d[1][y-10:])

        #printing the file
        output_file_path = '/Users/kurtisng/Documents/dev/Seer 1.91/Flask Web App/processed-files/fastatoembl.txt' #filetoconversion.txt

        if os.path.exists(output_file_path):
            os.remove(output_file_path)

        with open(output_file_path, 'w') as f:
            f.write('ID '+d[0][1:]+"\n") #ID first line
            f.write('XX\n')
            f.write("AC "+acc+'\n')
            f.write("XX\n")
            for i in range(len(des)):
                f.write("DE "+des[i]+'\n')
            print("XX\n")

            #number of each:
            A = str(m['A'])
            C = str(m['C'])
            T = str(m['T'])
            G = str(m['G']) 

            f.write('SQ '+"Sequence "+str(len(d[1]))+" BP; "+A+" A; "+C+' C; '+G+' G; '+T+" T;\n")

            cur = 0
            length = 0
            f.write('   ')
            for i in tenslist:
                length +=len(i)
                cur +=1
                f.write(i.lower() + ' ')
                if cur%6 == 0 and cur != len(tenslist):
                    f.write(' '+str(length)+"\n")
                    f.write('   ')
                elif cur%6==0 and cur == len(tenslist):
                    f.write(' '+str(length)+"\n")
                    length = 0
            f.write("\n//")
        return redirect(url_for('fasta_embl_download.downloadfastaembl', file=output_file_path))
    return render_template('fasta_embl.html')

@embl_fasta.route('/embl-fasta',methods=['GET','POST'])
def embl_f():
    if request.method == 'POST':
        import re
        f = request.files['embl_file'].read().decode('utf8').split('\n')

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

        output_file_path = '/Users/kurtisng/Documents/dev/Seer 1.91/Flask Web App/processed-files/embltofasta.txt' #filetoconversion.txt

        if os.path.exists(output_file_path):
            os.remove(output_file_path)

        with open(output_file_path,'w') as f:
            f.write(">"+idstr+'\n')
            f.write(''.join(refinedseq))
        
        return redirect(url_for('embl_fasta_download.downloademblfasta', file=output_file_path))
    return render_template('embl_fasta.html') 