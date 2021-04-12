FROM python:3.8-slim-buster

WORKDIR /gettingStarted

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONBUFFERED 1

RUN pip install --upgrade pip
# COPY ./requirements.txt /gettingStarted/requirements.txt
# COPY ./wait-for-it.sh /gettingStarted/wait-for-it.sh
COPY . /gettingStarted
RUN chmod +x /gettingStarted/wait-for-it.sh
RUN pip install -r requirements.txt
COPY ./__pycache__ /gettingStarted/__pycache__
COPY ./.pytest_cache /gettingStarted/__pycache__