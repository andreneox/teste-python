from flask import Flask 

app = Flask("blog")

@app.route("/")
def blog ():
    return "Blog NNN"