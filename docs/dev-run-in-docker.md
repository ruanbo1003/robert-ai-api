
## docker image
* build
```shell
docker build --platform=linux/amd64 -t registry.cn-heyuan.aliyuncs.com/ruanbo/ai-core-api:v0 -f docker/Dockerfile .
```
* push
```shell
docker push registry.cn-heyuan.aliyuncs.com/ruanbo/ai-core-api:v0
```


## run in docker
* run with docker compose, database and api service
```shell
docker compose -f docker/docker-compose.yml up postgres_dev ai_core_api_dev
```

* only run database
```shell
docker compose -f docker/docker-compose.yml up postgres_dev
```
