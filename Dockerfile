FROM python:3.5.3-slim
MAINTAINER Brian Buxton <brbuxton@cisco.com>

COPY . /app
WORKDIR /app

RUN pip install --no-cache-dir setuptools wheel
RUN pip install -r requirements.txt
