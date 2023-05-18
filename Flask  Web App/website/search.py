from flask import Blueprint, render_template, request

search = Blueprint('search',__name__)

@search.route('/search',methods=['POST'])
def searchalgs():
    if request.method=="POST":
        algname = request.form['q']
        if algname == 'CN':
            return render_template("countingnucleotides.html")
        elif algname == 'GC':
            return render_template('gccontent.html')
        elif algname == 'CSM':
            return render_template('consensus.html')
        elif algname == 'RNAP': 
            return render_template('rnatoprotein.html')
        elif algname == 'HD':
            return render_template('hamming.html')
        elif algname == 'FI':
            return render_template('fibonacci.html')
        else:
            return render_template('algorithms.html')
    return render_template('home.html')