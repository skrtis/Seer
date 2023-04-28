from flask import Blueprint

account = Blueprint('account', __name__)

@account.route('/login')
def login():
    return '<p>Login</p>'

@account.route('/logout')
def logout():
    return '<p>Logout</p>'

@account.route('/signup')
def sign_up():
    return '<p>Sign Up</p>'


