# coding: utf-8
from flask import Flask, request, render_template, redirect, jsonify, make_response
import os
import psycopg2
import urllib.parse
from flask_cors import CORS

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
CORS(app)

# バッドコードな気がしますが...

def getConn():
    urllib.parse.uses_netloc.append("postgres")
    url = urllib.parse.urlparse(os.environ["SQL_URL"])
    conn = psycopg2.connect(
        database=url.path[1:],
        user=url.username,
        password=url.password,
        host=url.hostname,
        port=url.port
    )
    return conn


@app.route("/dest", methods=['GET'])
def get_sample():
    # jsonオブジェクトを取得

    return make_response(jsonify({
        "task_id": "example-photo-link",
        "name": "hogehoge",
        "id": "uuid",
    }), 200)


@app.route("/task", methods=['POST'])
def new_spot():
    request = request.json

    # ここでスポット登録

    return make_response(jsonify({"status": "success"}), 200)


@app.route("/test", methods=['POST', 'GET'])
def test():
    return make_response(jsonify({"status": "success"}), 200)


if __name__ == "__main__":
    app.run()
