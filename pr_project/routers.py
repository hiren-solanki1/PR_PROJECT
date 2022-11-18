from flask import Flask, g, render_template, request ,make_response

from scraper import get_amazon_data
import html
import time

app = Flask(__name__)

@app.route('/')
def ind():
    return render_template('index.html')

@app.route('/data', methods=['GET', 'POST'])
def scraper():
    # data = {}
    if request.method == "POST":
        url_  = request.form.get('search')

        df = get_amazon_data(url_)

        print(df)
        resp = make_response(df.to_csv())
        resp.headers["Content-Disposition"] = "attachment; filename=PRProject.csv"
        resp.headers["Content-Type"] = "text/csv"
        return resp
    # get_amazon_data(data)
    # return render_template('index.html')
    

if __name__ == "__main__":
    app.run(debug = False,host='0.0.0.0')
