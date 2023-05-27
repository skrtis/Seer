from flask import Blueprint, render_template, request, redirect, url_for
import re 
import math 
import os

#formatting name_conversion
plain_fasta = Blueprint('plain_fasta',__name__)
fasta_plain= Blueprint('fasta_plain',__name__)

#function naming: name_(first letter of conversion)
@plain_fasta.route('/plain-fasta',methods=['GET','POST'])
def plain_f(): 
    if request.method=='POST':
        #x = input("Enter String(s), split multiple strings with semicolon:")
       # y = int(input("Enter preferred line length: "))
        x = request.files['fasta_file'].read().decode('utf8')
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