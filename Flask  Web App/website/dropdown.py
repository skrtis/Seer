from flask import Flask, Blueprint, render_template
lists = Blueprint('list', __name__)
#list.debug = True

@lists.route('/algs')
def dropdown():
    #choices = ['Conversion', 'Algorithms', 'Literature', 'Sitemap', 'FAQ', 'About']
    return render_template('algorithms.html')


if __name__ == "__main__":
    lists.run()