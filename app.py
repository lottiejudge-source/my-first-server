from flask import Flask, render_template

app = Flask(__name__)


# a decorator = "When an HTTP request matches this URL and method, run the function immediately below."
@app.get('/')
def home():
    return render_template('index.html')


# @app.post()
