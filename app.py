# ---- YOUR APP STARTS HERE ----
# -- Import section --
from flask import Flask
from flask import render_template
from flask import request
from model import encrypt


# -- Initialization section --
app = Flask(__name__)


# -- Routes section --
@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")

@app.route('/results', methods = ['GET', 'POST'])
def results():
    if request.method=='POST':
        shift = request.form['shift']
        original_message = request.form['message']
        encryption = encrypt(original_message, shift)
        return render_template("result.html", shift = shift, original_message = original_message, encryption = encryption)
    else:
        return "<h2>dique '404 error'...</h2>"
