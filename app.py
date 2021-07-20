import os
import requests
import json

from flask import Flask, render_template, request, session, jsonify, redirect, url_for
from dotenv import load_dotenv
from authlib.integrations.flask_client import OAuth
from six.moves.urllib.parse import urlencode

load_dotenv()

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY")

oauth = OAuth(app)

auth0 = oauth.register(
    "auth0",
    client_id=os.environ.get("CLIENT_ID"),
    client_secret=os.environ.get("CLIENT_SECRET"),
    api_base_url=os.environ.get("API_BASE_URL"),
    access_token_url=os.environ.get("API_BASE_URL") + "/oauth/token",
    authorize_url=os.environ.get("API_BASE_URL") + "/authorize",
    client_kwargs={"scope": "openid profile"},
)

# Client Kwargs are specified in order to return user info when successfully logged in


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("homepage.html", user=session.get("jwt_payload"))
    elif request.method == "POST":
        name = request.form.get("supe-name")
        url = (
            "https://superheroapi.com/api/"
            + os.environ.get("API_ACCESS_KEY")
            + "/search/"
            + name
        )

        results = requests.get(url).json()

        session["results"] = results
        return redirect(url_for("results"))


@app.route("/callback")
def handle_callback():
    """This verifies the user's identify when logged in and returns the user data in json."""
    auth0.authorize_access_token()
    resp = auth0.get("userinfo")
    user_info = resp.json()

    # Save User Data to our session
    session["jwt_payload"] = user_info

    # If the user searched for something before logging in, redirect to results
    if session.get("results") is not None:
        return redirect(url_for("results"))

    return redirect(url_for("index"))


@app.get("/results")
def results():
    results = session.get("results")
    user_info = session.get("jwt_payload")

    if user_info is not None:
        if results is not None:
            return render_template("results.html", data=results, user=user_info)

    return redirect("/login")


@app.get("/login")
def login():
    # Auth0 authorizes our callback route and redirects to it's login page
    return auth0.authorize_redirect(redirect_uri=os.environ.get("YOUR_DOMAIN") + "/callback")


@app.get("/logout")
def logout():
    session.clear()
    # Redirect user to logout endpoint
    params = {
        "returnTo": url_for("index", _external=True),
        "client_id": os.environ.get("CLIENT_ID"),
    }
    return redirect(auth0.api_base_url + "/v2/logout?" + urlencode(params))


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
