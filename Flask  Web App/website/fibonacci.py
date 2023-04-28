from flask import Blueprint

fibonacci = Blueprint('fibonacci', __name__)

@fibonacci.route('/fib')
def home():
    return "<h1>testing</h1>"