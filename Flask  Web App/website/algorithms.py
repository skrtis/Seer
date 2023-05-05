from flask import Blueprint, render_template, request

fib = Blueprint('fibonacci', __name__)

@fib.route('/fibonacci', methods=['GET', 'POST'])
def fibonacci():
    if request.method == 'POST':
        n = int(request.form['n'])
        k = int(request.form['k'])
        # Run the Fibonacci algorithm
        # initialize n-1 and n-2
        nm1 = 1
        nm2 = 1
        fin = 0
        # iterate through generations
        for i in range(n-2):
            fin = nm1 + (k*nm2)
            nm2 = nm1
            nm1 = fin
        # Render the template with the output
        return render_template('fibonacci.html', result=fin)
    return render_template('fibonacci.html')
