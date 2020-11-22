FROM python:3.6-alpine

COPY ./requirements.txt /tmp/

RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev
RUN pip install --upgrade pip
RUN pip install -r /tmp/requirements.txt

COPY ./app /app/main.py
