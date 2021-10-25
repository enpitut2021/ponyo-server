# ponyo-server

滅びの呪文

> docker-compose down --rmi all --volumes --remove-orphans

読み出し:

> curl localhost:9002/task/read

登録：

> curl -X POST -H "Content-Type: application/json" -H "Origin:http://localhost:9002" -d '{"name":"hogeタスク","user_id":"example-user-id","deadline":""}' localhost:9002/task