FROM python:3.11-slim

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt
#RUN apk add libcrypto3=3.1.1-r1 libssl3=3.1.1-r1 --repository=https://dl-cdn.alpinelinux.org/alpine/edge/main --no-cache

EXPOSE 5000

CMD ["python","main.py"]


