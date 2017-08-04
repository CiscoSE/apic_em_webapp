FROM python:3.5.3-slim
MAINTAINER Brian Buxton <brbuxton@cisco.com>

EXPOSE 8000

ADD . /app
WORKDIR /app

RUN pip install --no-cache-dir setuptools wheel
RUN pip install -r requirements.txt

CMD ["python", "manage.py", "runserver"]
