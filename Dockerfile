# syntax=docker/dockerfile:1

FROM python:3.11-slim-buster

WORKDIR /python-docker

COPY requirements.txt requirements.txt
RUN apt-get update
RUN apt-get -y install gcc python3-dev
RUN apt-get -y install build-essential
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

COPY . .

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]