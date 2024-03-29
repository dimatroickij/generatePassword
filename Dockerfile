# pull official base image
FROM python:3.8.1-slim-buster

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip
RUN pip install pip-tools

COPY ./requirements.in /usr/src/app/requirements.in
RUN pip-compile --upgrade
RUN pip-sync

# copy project
COPY . /usr/src/app/