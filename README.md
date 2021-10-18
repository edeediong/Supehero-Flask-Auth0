# Flask_Auth_App
This repository contains the code of a Supehero based website with authentication

## Prerequisites
- virtualenv
- Superhero [API Access Key](https://superheroapi.com/)

### Install VirtualEnv
```bash
  sudo pip install virtualenv
```

### Get Superhero API Access Key
Head over to the website given above  and generate  your access token.

## Initialize Code

### Clone Branch

We clone the branch **initial** in the repo.

```bash
  git clone -b initial https://github.com/edeediong/Supehero-Flask-Auth0.git
```

Here's the structure of our project after running `tree Supehero-Flask-Auth0`.

```bash
.
├── app.py
├── requirements.txt
├── static
│   ├── css
│   │   └── main.css
│   └── images
│       ├── 1158056.jpg
│       └── 703e02b53cb97fa45cef8b156e4b0e4a.jpg
├── templates
    ├── homepage.html
    └── results.html
```

### Activate Python Environment with Necessary Libraries

Then activate virtual env and install requirements.txt

```bash
  virtualenv my_env
  source my_env/bin/activate

  pip install -r requirements.txt
```

### Attach Environment Variables

Next step is writing our environment variables in our `.env` file.

We are storing keys gotten from our SuperHero API in our `.env` file.

```bash
  FLASK_APP=app.py
  FLASK_ENV=development
  API_ACCESS_KEY=<Superhero_Access_Key>
  SECRET_KEY=<Anything really> # Allows you to set sessions
```

## Starting the App

While the virtual evironment is activated, we enter this on local terminal

```bash
  flask run
```