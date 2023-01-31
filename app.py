from flask import Flask

app = Flask(__name__)

def index():
    return 'Index Page'

@app.route("/hello")
def hello():
    return "hello_world"