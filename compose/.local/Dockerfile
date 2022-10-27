ARG PYTHON_VERSION=3.9-slim-buster
FROM python as python-build-stage
ARG BUILD_ENVIRONMENT=base

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

COPY ./start /start
RUN sed -i 's/\r$//g' /start
RUN chmod +x /start

COPY . app

RUN echo $PYTHONPATH


