FROM ubuntu:latest

# FROM python:3.11-alpine3.17

RUN apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get upgrade -yq && \
    apt-get install -y python3 python3-pip && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .

RUN pip3 install --no-cache-dir -r requirements.txt

# RUN apk add libcrypto3=3.1.1-r1 libssl3=3.1.1-r1 --repository=https://dl-cdn.alpinelinux.org/alpine/edge/main --no-cache

COPY . .

EXPOSE 5000

CMD ["python3", "app.py"]