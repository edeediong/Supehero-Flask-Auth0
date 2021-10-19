import os
from flask import Flask, render_template, request, session, jsonify, redirect, url_for
from dotenv import load_dotenv
import requests
import json
from authlib.integrations.flask_client import OAuth
from six.moves.urllib.parse import urlencode

load_dotenv()

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY')

oauth = OAuth(app)

auth0 = oauth.register(
    'auth0', 
    client_id=os.environ.get('CLIENT_ID'), 
    client_secret=os.environ.get('CLIENT_SECRET'),
    api_base_url=os.environ.get('API_BASE_URL'),
    access_token_url=os.environ.get('API_BASE_URL') + '/oauth/token',
    authorize_url=os.environ.get('API_BASE_URL') + '/authorize',
    client_kwargs={
        'scope': 'openid profile'
    }
)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "GET":
        return render_template('homepage.html', user=session.get('jwt_payload'))
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

@app.route('/callback')
def handle_callback():
    auth0.authorize_access_token()
    resp = auth0.get('userinfo')
    user_info = resp.json()

    print(resp)
    session['jwt_payload'] = user_info

    if session.get('results') is not None:
        return redirect(url_for('results'))

    return redirect(url_for('index'))

@app.route('/results', methods=['GET'])
def results():
    results = session.get('results')
    user_info = session.get('jwt_payload')

    if user_info is not None:
        if results is not None:
            return render_template('results.html', data=results, user=user_info)
         
    return redirect('/login')

@app.route('/login', methods=['GET'])
def login():
    return auth0.authorize_redirect(redirect_uri='http://localhost:5000/callback')

@app.route('/logout', methods=['GET'])
def logout():
    session.clear()
    # Redirect user to logout endpoint
    params = {'returnTo': url_for('index', _external=True), 'client_id': os.environ.get('CLIENT_ID')}
    return redirect(auth0.api_base_url + '/v2/logout?' + urlencode(params))

if __name__ == '__main__':
    app.run(debug=True)