FROM python:3.5.3-alpine3.4
MAINTAINER Brian Buxton <brbuxton@cisco.com>

ENV USER root
ENV HOME /root

RUN pip install --no-cache-dir setuptools wheel
RUN pip install --requirement /app/requirements.txt

ADD . /app
WORKDIR /app
