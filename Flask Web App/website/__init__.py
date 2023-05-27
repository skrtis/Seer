from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'bioinformatics'

    from .views import views
    from .mainmenu import lists
    from .button import homebut
    from .search import search
    from .download import plain_fasta_download

    #import algorithms
    from .algorithms import fib
    from .algorithms import cnucleotides
    from .algorithms import gc
    from .algorithms import consensus
    from .algorithms import hamming
    from .algorithms import rnatoprotein
    from .algorithms import motif
    from .conversion import plain_fasta
 
 

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

    #implement file conversion
    app.register_blueprint(plain_fasta, url_prefix='/conversion')
    
    #implement file conversion dowload links
    app.register_blueprint(plain_fasta_download, url_prefix='/download')

    return app
