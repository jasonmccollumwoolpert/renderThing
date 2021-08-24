from flask import Flask, request
import psycopg2

app = Flask(__name__)

conn = psycopg2.connect("postgres://renderuser:95YvqCrPPcKt5Rro7oyPJOwvKt8wQlOl@oregon-postgres.render.com/renderdatabase")

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