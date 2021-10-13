# coding: utf-8
from flask import Flask, request, render_template, redirect, jsonify, make_response

from flask_cors import CORS

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
CORS(app)


@app.route("/dest", methods=['GET'])
def get_sample():
    # jsonオブジェクトを取得

    return make_response(jsonify({
        "task_id": "example-photo-link",
        "name": "hogehoge",
        "id": "uuid",
    }), 200)


@app.route("/post_spot", methods=['POST'])
def new_spot():
    # jsonオブジェクトを取得
    # json_obj = request.json

    # ここでスポット登録

    return make_response(jsonify({"status": "success"}), 200)


@app.route("/test", methods=['POST', 'GET'])
def test():
    return make_response(jsonify({"status": "success"}), 200)


if __name__ == "__main__":
    app.run()
