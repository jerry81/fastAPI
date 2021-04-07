FROM python:3.8-slim-buster

WORKDIR /gettingStarted

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONBUFFERED 1

RUN pip install --upgrade pip
COPY ./requirements.txt /gettingStarted/requirements.txt
RUN pip install -r requirements.txt
COPY . /gettingStarted