from flask import Flask
import datetime

app = Flask(__name__)


@app.route("/")
def hello():
    return 'Hello, World! <a href="/status">Status</a>'


@app.route("/status")
def status():
    return {
        'status': 200,
        'Name': 'KoshkinChat',
        'Time': datetime.datetime.now()
    }


app.run()
