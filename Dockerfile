# FROM ubuntu:20.04

FROM python:3.11-alpine3.17

WORKDIR /app

COPY requirements.txt .

RUN apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get upgrade -yq && \
    apt-get install -y --no-install-recommends python3=3.11.0 python3-pip=21.3.1 && \
    rm -rf /var/lib/apt/lists/* && \
    pip3 install --no-cache-dir -r requirements.txt


# RUN apk add libcrypto3=3.1.1-r1 libssl3=3.1.1-r1 --repository=https://dl-cdn.alpinelinux.org/alpine/edge/main --no-cache

COPY . .

EXPOSE 5000

CMD ["python3", "app.py"]
