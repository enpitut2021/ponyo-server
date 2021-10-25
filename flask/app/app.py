# coding: utf-8
from flask import Flask, request, render_template, redirect, jsonify, make_response
import os
import psycopg2
import urllib.parse
from flask_cors import CORS
import uuid
app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
CORS(app)

# バッドコードな気がしますが...


def getConn():
    urllib.parse.uses_netloc.append("postgres")
    conn = psycopg2.connect(
        database='ponyo',
        user='user',
        password='password',
        host='ponyodb',
        port=5432
    )
    return conn


@app.route("/task/read", methods=['GET'])
def get_task():
    connection = getConn()
    response = []

    try:
        query = """select name,id,deadline from tasks"""
        # ここでスポット登録
        cursor = connection.cursor()
        cursor.execute(query)
        results = cursor.fetchall()
        for item in results:
            print(item)
            task = {"name": item[0], "id": item[1], "deadline": item[2]}
            response.append(task)
    except(Exception, psycopg2.Error) as error:
        print(error)
        return make_response(jsonify({"status": "failed"}), 500)
    finally:
        if connection:
            cursor.close()
            connection.close()
        return make_response(jsonify({"tasks": response}), 200)


@app.route("/task", methods=['POST'])
def new_task():
    connection = getConn()
    cursor = connection.cursor()
    print("hogehoge", flush=True)
    try:
        query = "insert into tasks(id,name,user_id) values(%s,%s,%s)"
        value = (
            str(uuid.uuid4()),
            request.json['name'],
            request.json['user_id'])
        print(value, flush=True)
        # ここでスポット登録
        cursor.execute(query, value)
        connection.commit()
        count = cursor.rowcount
        print(count, "Record inserted successfully into mobile table")
    except(Exception, psycopg2.Error) as error:
        print(error)
        return make_response(jsonify({"status": "failed"}), 500)
    finally:
        if connection:
            cursor.close()
            connection.close()
            return make_response(jsonify({"status": "success"}), 200)


@app.route("/test", methods=['POST', 'GET'])
def test():
    return make_response(jsonify({"status": "success"}), 200)


if __name__ == "__main__":
    app.run()
