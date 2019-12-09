from dictogram import Dictogram
from markov import Markov
from flask import Flask, render_template, request, redirect, url_for


markov = Markov()
markov.build_markov('src.txt')

app = Flask(__name__)


@app.route('/')
def index():
    """Return homepage."""
    sample = markov.sample_markov()
    print(sample)
    return render_template('index.html', sample=sample)




 




