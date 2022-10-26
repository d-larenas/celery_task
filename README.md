# Python + Celery + Docker

<h3 align="left"></h3>
<p align="left"> <a href="https://www.docker.com/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/docker/docker-original-wordmark.svg" alt="docker" width="40" height="40"/> </a> <a href="https://www.linux.org/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/linux/linux-original.svg" alt="linux" width="40" height="40"/> </a> <a href="https://www.python.org" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="40" height="40"/> </a> <a href="https://redis.io" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/redis/redis-original-wordmark.svg" alt="redis" width="40" height="40"/> </a> </p>

Application for scheduled tasks with celery.

## Description

Dervices to check website status, adding log in json file as well as alert sent to email

## Installation

Add env.example variable file.

```
  .envs -> path
  └── .local ->file
     
```

## docker 

```
    docker-compose -f local.yml build

    docker-compose -f local.yml up

```

## celery extra

```
    celery -A celery_service worker -l INFO

    celery -A celery_service beat -l INFO

```
