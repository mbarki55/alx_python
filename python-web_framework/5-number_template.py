from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_hbnb():
    """Route to greet the user with "Hello HBNB!"."""
    return 'Hello HBNB!'

@app.route('/hbnb')
def hbnb():
    """Route to display "HBNB"."""
    return 'HBNB'

@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """Route to display "C" followed by the provided text."""
    return 'C ' + text.replace('_', ' ')

@app.route('/python/', defaults={'text': 'is cool'})
@app.route('/python/<text>', strict_slashes=False)
def python_text(text):
    """Route to display "Python" followed by the provided text."""
    return 'Python ' + text.replace('_', ' ')

@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """Route to display "n is a number" if n is an integer."""
    if isinstance(n, int):
        return f'{n} is a number'
    else:
        return 'Not Found', 404

@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """Route to display an HTML page with "Number: n" if n is an integer."""
    if isinstance(n, int):
        return f'<html><body><h1>Number: {n}</h1></body></html>'
    else:
        return 'Not Found', 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
