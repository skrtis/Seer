from flask import Flask, Blueprint, render_template
lists = Blueprint('list', __name__)
#list.debug = True

@lists.route('/l')
def dropdown():
    #choices = ['Conversion', 'Algorithms', 'Literature', 'Sitemap', 'FAQ', 'About']
    return '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Dropdown</title>
    </head>
    <body>
        <label for="List">Choose An Action:</label>

        <select id="List" name="choices">
            <option value="conversion">Conversion</option>
            <option value="algorithms">Algorithms</option>
            <option value="literature">Literature</option>
        </select>
    </body>
    </html>
    '''


if __name__ == "__main__":
    lists.run()