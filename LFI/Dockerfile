FROM ubuntu:latest

ENV TZ=Europe/Kiev

RUN \
    apt-get update && \
    apt-get install -y apache2 && \
    apt-get install -y php 

COPY . /home/juan/
