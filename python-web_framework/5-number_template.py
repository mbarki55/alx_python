"""A simple Flask web application."""
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello HBNB!'


@app.route('/hbnb',strict_slashes=False)
def hbnb():
    return 'HBNB'

@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    return 'C ' + text.replace('_', ' ')

'''Route to display "Python" followed by the provided text'''

@app.route('/python/', defaults={'text': 'is_cool'})
@app.route('/python/<text>', strict_slashes=False)
def python_text(text):
    return 'Python ' + text.replace('_', ' ')

@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    return f'{n} is a number'


@app.route('/number_template/<int(n)>', strict_slashes=False)
def number_template(n):
    return f'<html><body><h1>Number: {n}</h1></body></html>'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)



    
    