from datetime import datetime as dt
from flask import Flask, request
import os
import psycopg2

app = Flask(__name__)
conn = psycopg2.connect(os.environ.get('db_conn'))

@app.get('/')
def app_get():
    try:
        seconds = float(request.args.get('seconds'))
    except:
        return 'Numerical argument of seconds is required', 400
    
    value_raw = request.args.get('value')
    value = None
    if value_raw is not None:
        value = str(value_raw)

    cur = conn.cursor()

    if value:
        cur.execute('''
        select
            thing,
            count(thing)
        from
            things
        where
            entrytimestamp >= current_timestamp - interval '%s seconds'
            and thing = %s
        group by thing;
        ''',
            (seconds, value)
        )
    else:
        cur.execute('''
        select
            thing,
            count(thing)
        from
            things
        where
            entrytimestamp >= current_timestamp - interval '%s seconds'
        group by thing;
        ''',
            (seconds,)
        )

    result = cur.fetchall()
    response = {}
    for word in result:
        response[word[0]] = word[1]
    cur.close()
    return response

@app.post('/')
def app_post():
    body = request.json
    if not body:
        return 'Missing request body', 400
    if not isinstance(body, dict) or not 'value' in body:
        return 'Request should be of the format { "value": "myValue" }', 400
    
    value = str(body['value'])
    now = dt.utcnow()

    cur = conn.cursor()
    cur.execute('''
        insert into things (thing, entrytimestamp)
        values
            (%s, %s)
        ''',
        (value, now)
    )
    conn.commit()
    cur.close()

    return { "timestamp": now, "value": value }