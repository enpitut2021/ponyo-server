# ponyo-server

滅びの呪文

> docker-compose down --rmi all --volumes --remove-orphans

読み出し:

> curl localhost:9002/task/read
> curl localhost:9002/episode?user_id=example-user-id-1
> curl localhost:9002/episode

登録：

> curl -X POST -H "Content-Type: application/json" -H "Origin:http://localhost:9002" -d '{"name":"hogeタスク","user_id":"example-user-id","deadline":""}' localhost:9002/task

curl -X POST -H "Content-Type: application/json" -H "Origin:http://localhost:9002" -d '{"desc":"私は財布を落としました","user_id":"example-user-id-3"}' localhost:9002/episode