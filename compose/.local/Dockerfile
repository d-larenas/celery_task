ARG PYTHON_VERSION=3.9-slim-buster
FROM python as python-build-stage
ARG BUILD_ENVIRONMENT=local

ENV TZ=America/Santiago
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

WORKDIR /app
# Requirements are installed here to ensure they will be cached.
COPY ./requirements/ .
# Create Python Dependency and Sub-Dependency Wheels.
RUN pip install -r ${BUILD_ENVIRONMENT}.txt

RUN apt-get update && \
    apt-get install -y locales && \
    sed -i -e 's/# es_ES.UTF-8 UTF-8/es_ES.UTF-8 UTF-8/' /etc/locale.gen && \
    dpkg-reconfigure --frontend=noninteractive locales


COPY celery_start/beat/start /celery_start/beat/start
RUN sed -i 's/\r$//g' /celery_start/beat/start
RUN chmod +x /celery_start/beat/start

COPY compose/.local/entrypoint /entrypoint
RUN sed -i 's/\r$//g' /entrypoint
RUN chmod +x /entrypoint

COPY celery_start/worker/start /celery_start/worker/start
RUN sed -i 's/\r$//g' /celery_start/worker/start
RUN chmod +x /celery_start/worker/start

COPY celery_start/flower/start /celery_start/flower/start
RUN sed -i 's/\r$//g' /celery_start/flower/start
RUN chmod +x /celery_start/flower/start

COPY . app

RUN mkdir -p /celery_service/task_json


RUN mkdir -p /celery_beat_schedule



ENTRYPOINT ["/entrypoint"]


