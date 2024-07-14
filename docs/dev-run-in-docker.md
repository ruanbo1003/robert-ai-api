
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
