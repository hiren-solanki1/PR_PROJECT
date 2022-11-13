from flask import Flask, g, render_template, request
from scraper import get_amazon_data
import html
import time

app = Flask(__name__)

@app.route('/')
def ind():
    return render_template('index.html')

@app.route('/data')
def scraper():
    data = {}
    if request.method == "POST":
        data['search'] = request.form['search']
    get_amazon_data(data)
    return render_template('index.html')
    


app.run(debug = True)