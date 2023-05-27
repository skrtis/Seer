from flask import Flask, send_file, request
from flask import Blueprint, render_template

#naming name_conversion_download
plain_fasta_download = Blueprint('plain_fasta_download',__name__)

# function naming: nameconversiondownload
@plain_fasta_download.route('/plainfasta')
def downloadplainfasta(): 
    file_path = request.args.get('file')
    return send_file(file_path, mimetype='text/plain', as_attachment=True, download_name= 'plaintofasta.txt')