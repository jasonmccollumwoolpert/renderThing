from flask import Flask, request

app = Flask(__name__)

@app.get('/')
def app_get():
    seconds = request.args.get('seconds')
    response = {
        'seconds': seconds
    }
    return response

@app.post('/')
def app_post():
    return 'request received'