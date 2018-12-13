import os
from flask import Flask, redirect, url_for, request, render_template,jsonify
from pymongo import MongoClient

import arrow  # Replacement for datetime, based on moment.js
import acp_times  # Brevet time calculations


import logging


app = Flask(__name__)

client = MongoClient(os.environ['DB_PORT_27017_TCP_ADDR'], 27017)
db = client.tododb

db.tododb.delete_many({})
@app.route("/")
@app.route("/index")
def index():
    app.logger.debug("Main page entry")
    return render_template('calc.html')


@app.route('/todo')
def todo():
    _items = db.tododb.find()
    items = [item for item in _items]

    return render_template('todo.html', items=items)

@app.route('/new', methods=['POST'])
def new():
    openlist = []
    open = request.form.getlist("open")
    for o in open:
        if str(o) != "":
            openlist.append(str(o))

    closelist = []
    close = request.form.getlist("close")
    for c in close:
        if str(c) != "":
            closelist.append(str(c))

    for i in range(len(openlist)):
        time = {
        'otime': openlist[i],
        'ctime': closelist[i]
        }
        db.tododb.insert_one(time)

    _items = db.tododb.find()
    items = [item for item in _items]

    if items != []:
        return redirect(url_for('index'))
    else:
        return redirect(url_for('404.html'))

@app.route("/_calc_times")
def _calc_times():
    """
    Calculates open/close times from miles, using rules
    described at https://rusa.org/octime_alg.html.
    Expects one URL-encoded argument, the number of miles.
    """
    app.logger.debug("Got a JSON request")
    km = request.args.get('km', 999, type=float)
    distance = request.args.get('distance', 999, type=float)
    date = request.args.get('date', 999, type=str)
    time = request.args.get('time', 999, type=str)

    a = arrow.get((date + ' ' + time + ':00'), 'YYYY-MM-DD HH:mm:ss')

    open_time = acp_times.open_time(km, distance, a.isoformat())
    close_time = acp_times.close_time(km, distance, a.isoformat())
    result = {"open": open_time, "close": close_time}
    return jsonify(result=result)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
