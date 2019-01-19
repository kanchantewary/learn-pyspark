#FROM ubuntu:latest

FROM python:alpine3.7

MAINTAINER 'kanchan.tewary@gmail.com'

#RUN apt-get update -y && apt-get install -y python-pip python-dev

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip3 install -r requirements.txt

COPY . /app

#ENTRYPOINT ["python"]

EXPOSE 5000

CMD python3 ./app.py
