from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'bioinformatics'

    from .views import views
    from .auth import account
    from .dropdown import lists
    from .button import homebut
    from .search import search

    #import algorithms
    from .algorithms import fib
    from .algorithms import cnucleotides
    from .algorithms import gc
    from .algorithms import consensus
    from .algorithms import hamming
    from .algorithms import rnatoprotein
    from .algorithms import motif
 

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(account, url_prefix='/')
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
    return app
