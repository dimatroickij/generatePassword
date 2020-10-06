import random

from flask import Flask, render_template, request

app = Flask(__name__)

alphabet = 'abcdefghijklmnopqrstuvwxyz'
symbols = """!"#$%&'()*"""


@app.route('/')
def hello_world():
    return render_template("index.html")


@app.route('/generatePassword')
def generatePassword():
    id = request.args.get('inputId')
    b1 = alphabet[random.randint(0, 25)].upper()
    b2 = alphabet[random.randint(0, 25)].upper()
    b3 = str((len(id) ** 2) % 10)
    b4 = str(random.randint(0, 9))
    b5 = symbols[random.randint(0, 9)]
    b6 = alphabet[random.randint(0, 25)]
    alphabet.upper()
    return b1 + b2 + b3 + b4 + b5 + b6


if __name__ == '__main__':
    app.run()
