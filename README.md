# Flask_Auth_App
This repository contains the code of a Supehero based website with authentication

## Prerequisites
- virtualenv

### Install VirtualEnv
```bash
  sudo pip install virtualenv
```

Here's the structure of our project

```bash
.
├── app.py
├── requirements.txt
├── static
│   ├── css
│   │   └── main.css
│   └── images
│       ├── 1158056.jpg
│       └── 703e02b53cb97fa45cef8b156e4b0e4a.jpg
├── templates
    ├── homepage.html
    └── results.html
```

We clone the repo, then activate virtual env and install requirements.txt

```bash
  virtualenv my_env
  source my_env/bin/activate

  pip install -r requirements.txt
```

Next step is writing our environment variables in our `.env` file.

We are storing keys gotten from our SuperHero API in our `.env` file.

```bash
  FLASK_APP=app.py
  FLASK_ENV=development
  API_ACCESS_KEY=<Superhero_Access_Key>
  SECRET_KEY=<Anything really> # Allows you to set sessions
```

## Starting the App

While the virtual evironment is activated, we enter this on our terminal

```bash
  flask run
```
