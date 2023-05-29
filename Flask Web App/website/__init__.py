from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'bioinformatics'

    from .views import views
    from .mainmenu import lists
    from .button import homebut
    from .search import search
    from .download import plain_fasta_download
    from .download import fasta_plain_download
    from .download import fasta_embl_download
    from .download import embl_fasta_download


    #import algorithms
    from .algorithms import fib
    from .algorithms import cnucleotides
    from .algorithms import gc
    from .algorithms import consensus
    from .algorithms import hamming
    from .algorithms import rnatoprotein
    from .algorithms import motif
    from .algorithms import transcription
    from .algorithms import complement

    #import all conversions
    from .conversion import plain_fasta
    from .conversion import fasta_plain
    from .conversion import fasta_embl
    from .conversion import embl_fasta
 
 

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(lists, url_prefix='/')
    app.register_blueprint(homebut,url_prefix='/')
    app.register_blueprint(search,url_prefix='/')

    #implement algs
    app.register_blueprint(fib, url_prefix='/algs')
    app.register_blueprint(cnucleotides, url_prefix='/algs') 
    app.register_blueprint(gc, url_prefix='/algs')
    app.register_blueprint(consensus, url_prefix='/algs')
    app.register_blueprint(hamming, url_prefix='/algs')
    app.register_blueprint(rnatoprotein, url_prefix='/algs')
    app.register_blueprint(motif, url_prefix='/algs')
    app.register_blueprint(transcription, url_prefix='/algs')
    app.register_blueprint(complement, url_prefix ='/algs')

    #implement file conversion
    app.register_blueprint(plain_fasta, url_prefix='/conversion')
    app.register_blueprint(fasta_plain, url_prefix='/conversion')
    app.register_blueprint(fasta_embl,url_prefix='/conversion')
    app.register_blueprint(embl_fasta, url_prefix='/conversion')
    
    #implement file conversion dowload links
    app.register_blueprint(plain_fasta_download, url_prefix='/download')
    app.register_blueprint(fasta_plain_download, url_prefix='/download')
    app.register_blueprint(fasta_embl_download, url_prefix='/download')
    app.register_blueprint(embl_fasta_download, url_prefix='/download')


    return app #DO NOT DELETE DO NOT DO NOT DO NOT