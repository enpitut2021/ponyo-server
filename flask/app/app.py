# coding: utf-8
from flask import Flask, request, jsonify, make_response
import psycopg2
import urllib.parse
from flask_cors import CORS
import uuid
import os
import tweepy
import batch
import datetime
app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
CORS(app)

consumer_key = os.environ["CONSUMER_KEY"]
consumer_secret = os.environ["CONSUMER_SECRET"]
access_token = os.environ["ACCESS_TOKEN"]
access_token_secret = os.environ["ACCESS_TOKEN_SECRET"]

# Twitterオブジェクトの生成
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

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
    user_id = request.args.get('user_id', 'example-user-id')
    response = []
    try:
        query = "select name,id,deadline,description,is_done from tasks where user_id=\'{}\'".format(
            user_id)
        cursor = connection.cursor()
        cursor.execute(query)
        results = cursor.fetchall()
        for item in results:
            print(item)
            task = {
                "name": item[0],
                "id": item[1],
                "deadline": item[2],
                "desc": item[3],
                "is_done": item[4]}
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
    jsonObj = request.get_json()
    cursor = connection.cursor()
    task_id = ""
    task_state = False
    name = ""
    desc = ""
    tdatetime = "Wed, 12 Jan 2022 08:20:34 GMT"
    if 'name' in request.json:
        name = request.json['name']

    if 'desc' in request.json:
        desc = request.json['desc']

    if 'deadline' in request.json:
        try:
            tdatetime = datetime.datetime.strptime(
                request.json['deadline'], '%a, %d %b %Y %H:%M:%S %Z%z')
        except Exception as e:
            print(e)
            pass

    if jsonObj.get("id") is None:
        task_id = str(uuid.uuid4())
    else:
        task_id = jsonObj.get("id")

    if 'is_done' in request.json:
        task_state = jsonObj.get("is_done")

    try:
        query = "insert into tasks(id,name,description,user_id,deadline) values(%s,%s,%s,%s,%s) on conflict on constraint task_pkey do update set is_done=%s, updated_at=%s"
        value = (
            task_id,
            name,
            desc,
            request.json['user_id'],
            tdatetime,
            task_state,
            datetime.datetime.now(datetime.timezone.utc)
        )
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
            return make_response(
                jsonify({"status": "success", "task_id": task_id}), 200)


@app.route("/episode", methods=['POST', 'GET'])
def episode():
    connection = getConn()
    # 読み出し
    if request.method == 'GET':
        user_id = request.args.get('user_id', 'example-user-id')
        response = []
        try:
            query = "select description from episodes where user_id=\'{}\'".format(
                user_id)
            cursor = connection.cursor()
            cursor.execute(query)
            results = cursor.fetchall()
            for item in results:
                task = {"desc": item[0], "user_id": user_id}
                response.append(task)
        except(Exception, psycopg2.Error) as error:
            print(error)
            return make_response(jsonify({"status": "failed"}), 500)
        finally:
            if connection:
                cursor.close()
                connection.close()
            # api.update_status(response)
            return make_response(jsonify({"episodes": response}), 200)
    # 登録
    elif request.method == 'POST':
        connection = getConn()
        cursor = connection.cursor()
        try:
            query = "insert into episodes(id,description,user_id) values(%s,%s,%s)"
            value = (
                str(uuid.uuid4()),
                request.json['desc'],
                request.json['user_id'])
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


@app.route("/test/tweet", methods=['GET'])
def test_tweet():
    connection = getConn()
    # 読み出し
    if request.method == 'GET':
        user_id = request.args.get('user_id', 'example-user-id')
        response = []
        try:
            query = "select description from episodes where user_id=\'{}\'".format(
                user_id)
            cursor = connection.cursor()
            cursor.execute(query)
            results = cursor.fetchall()
            for item in results:
                task = {"desc": item[0], "user_id": user_id}
                response.append(task)
        except(Exception, psycopg2.Error) as error:
            print(error)
            return make_response(jsonify({"status": "failed"}), 500)
        finally:
            if connection:
                cursor.close()
                connection.close()
            api.update_status(response[len(response) - 1].get("desc"))
            return make_response(jsonify({"episodes": response}), 200)


@app.route("/signup", methods=['POST'])
def sign_up():
    connection = getConn()
    cursor = connection.cursor()
    try:
        query = "insert into accounts(id,email,password,name) values(%s,%s,%s,%s)"
        value = (
            str(uuid.uuid4()),
            request.json['email'],
            request.json['password'],
            request.json['name'])
        cursor.execute(query, value)
        connection.commit()
    except(Exception, psycopg2.Error, psycopg2.OperationalError, psycopg2.DatabaseError, psycopg2.DataError, psycopg2.ProgrammingError) as error:
        print(error)
        return make_response(jsonify({"message": "failed"}), 500)
    finally:
        if connection:
            cursor.close()
            connection.close()
            return make_response(jsonify({"status": "success"}), 200)


@app.route("/signin", methods=['POST'])
def login():
    connection = getConn()
    # 読み出し
    if request.method == 'POST':
        email = request.json['email']
        response = []
        try:
            query = "select * from accounts where email=\'{}\'".format(email)
            cursor = connection.cursor()
            cursor.execute(query)
            results = cursor.fetchall()
            for item in results:
                task = {"id": item[0]}
                response.append(task)
        except(Exception, psycopg2.Error) as error:
            print(error)
            return make_response(jsonify({"status": "failed"}), 500)
        finally:
            if connection:
                cursor.close()
                connection.close()
            if len(response) != 0:
                return make_response(jsonify(response[0]), 200)
            else:
                return make_response(jsonify({"status": "failed"}), 500)


@app.route("/test", methods=['POST', 'GET'])
def test():
    connection = getConn()
    cursor = connection.cursor()
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


if __name__ == "__main__":
    batch.execute_batch()
    app.run()
