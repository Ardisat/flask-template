from flask import Flask, jsonify
# from db.db import execute



app = Flask(__name__, static_folder="static")


@app.route('/')
def index():
    html = open("index.html").read()
    return html


@app.route('/function', methods=['POST'])
def function():

    response = execute(f'SELECT * FROM table')

    return jsonify(response)



app.run(debug = True, host = 'localhost', port = 1111)