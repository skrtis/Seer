from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'bioinformatics'

    from .views import views
    from .auth import account
    from .algorithms import fib
    from .dropdown import lists

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(account, url_prefix='/')
    app.register_blueprint(fib, url_prefix='/algs')
    app.register_blueprint(lists, url_prefix='/')
    return app
