from flask import Flask, render_template
from datetime import datetime

app = Flask("hello")
posts = [
    {
        "title": "meu primeiro post",
        "body": "este e meu primeiro post do blog",
        "author": "andre R",
        "created" : datetime(2022, 8 ,17)
    },
    {
        "title": "meu segundo post",
        "body": "este e meu segundo post do blog",
        "author": "andre RC",
        "created" : datetime(2022, 8 ,17)
    },
    {
        "title": "meu terceiro post",
        "body": "este e meu terceiro post do blog",
        "author": "andre RX",
        "created" : datetime(2022, 8 ,17)
    }
]

@app.route("/")
def index():
    return render_template("index.html", posts=posts)