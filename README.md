# ponyo-server

## ビルド方法

**bash build.shを実行**

滅びの呪文

> docker-compose down --rmi all --volumes --remove-orphans

読み出し:

> curl localhost:9002/task/read
> curl localhost:9002/episode?user_id=example-user-id-1
> curl localhost:9002/episode

登録：

> curl -X POST -H "Content-Type: application/json" -H "Origin:http://localhost:9002" -d '{"name":"hogeタスク","user_id":"example-user-id","deadline":"Wed, 12 Jan 2022 18:20:34 GMT +0900","is_done":false}' localhost:9002/task

> curl -X POST -H "Content-Type: application/json" -H "Origin:http://localhost:9002" -d '{"name":"hogeタスク","user_id":"example-user-id","deadline":"2022-01-23T05:36:00.000Z","is_done":false}' localhost:9002/task

2022-01-23T05:36:00.000Z
curl -X POST -H "Content-Type: application/json" -H "Origin:http://localhost:9002" -d '{"desc":"私は財布を落としました","user_id":"example-user-id-3"}' localhost:9002/episode

ユーザー登録:

```
curl -X POST -H "Content-Type: application/json" -H "Origin:http://localhost:9002" -d '{"email":"hoge@example.com","password":"password","name":"hogehoge"}' localhost:9002/signup
```

