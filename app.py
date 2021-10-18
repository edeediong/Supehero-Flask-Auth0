import os
from flask import Flask, render_template, request, session, jsonify, redirect, url_for
from dotenv import load_dotenv
import requests
import json

load_dotenv()

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY')

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "GET":
        return render_template('homepage.html')
    elif request.method == "POST":
        name = request.form.get('supe-name')
        url = 'https://akabab.github.io/superhero-api/api/all.json'

        results = requests.get(url).json()

        supe_details = []
        for x in results:
            if (name.lower() in x['name'].lower()):
                supe_details.append(x)

        session['results'] = supe_details
        
        return redirect(url_for('results'))

@app.route('/results', methods=['GET'])
def results():
    results = session.get('results')
    return render_template('results.html', data=results)


if __name__ == '__main__':
    app.run(debug=True)
