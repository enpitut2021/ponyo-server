# coding: utf-8
from flask import Flask, request, jsonify, make_response
import psycopg2
import urllib.parse
from flask_cors import CORS
import uuid
import os
import tweepy
import schedule
from time import sleep
from datetime import datetime

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


def get_alluser():
    connection = getConn()
    user_id = []
    try:
        query = """select id from accounts"""
        cursor = connection.cursor()
        cursor.execute(query)
        results = cursor.fetchall()
        for item in results:
            user_id.append(item[0])
    except(Exception, psycopg2.Error) as error:
        print(error)
    finally:
        if connection:
            cursor.close()
            connection.close()
    return user_id


def get_episode(user_id):
    connection = getConn()
    response = ""
    try:
        query = "select description from episodes where user_id=\'{}\'".format(
            user_id)
        cursor = connection.cursor()
        cursor.execute(query)
        results = cursor.fetchall()
        for item in results:
            print(item)
            response = item[0]
    except(Exception, psycopg2.Error) as error:
        print(error)
    finally:
        if connection:
            cursor.close()
            connection.close()
    return response


def calc_progress(user_id="example-user-id"):
    connection = getConn()
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
    finally:
        if connection:
            cursor.close()
            connection.close()
    for task in response:
        t1 = datetime.now()
        task_time = task["deadline"]
        if task_time.timestamp() < t1.timestamp() and task["is_done"] is False:
            api.update_status("投稿ID: " +
                              str(uuid.uuid4()) +
                              "\n" +
                              "恥ずかしいお話:" +
                              get_episode(user_id) +
                              "\n" +
                              "タスク:" +
                              task["desc"])


def batch_process():
    ids = get_alluser()
    print("処理ユーザー数: ", len(ids))
    count = 0
    for id in ids:
        count = count + 1
        print("Progress: ", 100 * ((1.0 * count) / len(ids)), "%")
        print("User: " + id)
        calc_progress(id)


schedule.every(1).minutes.do(batch_process)


def execute_batch():
    batch_process()
    while True:
        schedule.run_pending()
        sleep(1)


if __name__ == "__main__":
    batch_process()
    while True:
        schedule.run_pending()
        sleep(1)
