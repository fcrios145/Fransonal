FROM python:3.7.4-alpine
MAINTAINER FranRios

ENV PYTHONUNBEFFERED 1

RUN apk update \
    && apk add gcc \
    && apk add libpq postgresql-dev \
    && apk add build-base

COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

RUN mkdir /fransonal_project
WORKDIR /fransonal_project
COPY ./fransonal_project /fransonal_project

RUN adduser -D fransonal
USER fransonal
