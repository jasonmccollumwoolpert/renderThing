from flask import Flask, request
import psycopg2

app = Flask(__name__)

conn = psycopg2.connect("postgres://renderuser:95YvqCrPPcKt5Rro7oyPJOwvKt8wQlOl@oregon-postgres.render.com/renderdatabase")

@app.get('/')
def app_get():
    seconds = float(request.args.get('seconds'))
    cur = conn.cursor()
    cur.execute('''
    select
        thing,
        count(thing)
    from
        things
    where
        entrytimestamp >= current_timestamp - interval '%d seconds'
    group by thing;
    ''' % seconds)
    result = cur.fetchall()
    response = {}
    for word in result:
        response[word[0]] = word[1]
    return response

@app.post('/')
def app_post():
    return 'request received'