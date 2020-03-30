from dictogram import Dictogram
from markov import Markov2nd
from flask import Flask, render_template, request, redirect, url_for


markov = Markov2nd()    
markov.build_markov_2nd('src.txt')

app = Flask(__name__)

@app.route('/')
def index():
    """Return homepage."""
    sample = markov.sample_markov()
    print(sample)
    return render_template('index.html', sample=sample)




 




