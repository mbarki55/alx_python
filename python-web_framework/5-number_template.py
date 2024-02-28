'''
script starts a Flask web application
'''
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello():
    """
    This function returns a simple string 'Hello HBNB!' when the root
    URL ('/') is accessed.
    
    """
    return 'Hello HBNB!'

@app.route('/hbnb', strict_slashes=False)
def text1():
    return 'HBNB'

@app.route('/c/<text>', strict_slashes=False)
def text2(text):
    underscore = text.replace('_', ' ')
    return f'C {underscore}'

@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def text3(text):
    underscore = text.replace('_', ' ')
    return f'Python {underscore}'

@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    return f"{n} is a number"

@app.route('/number_template/<int:n>', strict_slashes=False)
def display_nInt (n):
    return render_template("5-number.html", number = n)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

''' working ^_^ ''' 