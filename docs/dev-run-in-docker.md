
* build image
```shell
docker build -t registry.cn-heyuan.aliyuncs.com/ruanbo/ai-core-api:v0 -f docker/Dockerfile .
```

* run with docker compose, database and api service
```shell
docker compose -f docker/docker-compose.yml up postgres_dev ai_core_api_dev
```

* only run database
```shell
docker compose -f docker/docker-compose.yml up postgres_dev
```


```text
{
    "code": 201,
    "message": "invalid user",
    "data": null
}
nextjs project use fetch() function to request data, and get this response from web server. How to add a middleware, so when the code is not 0, toast shows the message.
```
