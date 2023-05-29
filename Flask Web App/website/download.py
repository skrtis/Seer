from flask import Flask, send_file, request, redirect, send_from_directory
from flask import Blueprint, render_template, session
import os, os.path

#naming name_conversion_download
plain_fasta_download = Blueprint('plain_fasta_download',__name__)
fasta_plain_download = Blueprint('fasta_plain_download',__name__)
fasta_embl_download = Blueprint('fasta_embl_download',__name__)
embl_fasta_download = Blueprint('embl_fasta_download',__name__)
extra_download = Blueprint('extra_download',__name__)

# function naming: nameconversiondownload
@plain_fasta_download.route('/plainfasta')
def downloadplainfasta(): 
    file_path = request.args.get('file')
    return send_file(file_path, mimetype='text/plain', as_attachment=True, download_name= 'plaintofasta.txt')

@fasta_plain_download.route('/fastaplain')
def downloadfastaplain():
    file_path = request.args.get('file')
    return send_file(file_path,mimetype='text/plain', as_attachment= True, download_name='fastatoplain.txt' )

@fasta_embl_download.route('/fastaembl')
def downloadfastaembl():
    file_path = request.args.get('file')
    return send_file(file_path,mimetype='text/plain', as_attachment= True, download_name='fastatoembl.txt' )

@embl_fasta_download.route('/emblfasta')
def downloademblfasta():
    file_path = request.args.get('file')
    return send_file(file_path,mimetype='text/plain', as_attachment= True, download_name='embltofasta.txt' )
