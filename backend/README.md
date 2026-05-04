# Party Finder 3 - Backend

Backend part of Party Finder 3, written using django

## Prerequisites

- Python 3.14

## Dev setup

Best practice is to setup a local python venv and install required packages from `requirements.txt` with:

```
$ backend/ > pip install -r requirements.txt
```

You will also need to create a `.env` file (you can copy the `.env.template` file). The most important entry in there for dev purposes is the POSTGRESS_URL key, which will be used to connect to a Postgress database and is required for the app to run properly.
