FROM python:3.8-slim-buster

COPY ./requirements.txt  /jiten_terria_master/requirements.txt

RUN pip install --no-cache-dir -r /jiten_terria_master/requirements.txt

COPY . /jiten_terria_master /

WORKDIR /jiten_terria_master/

#CMD [ "python", "-m" , "flask", "run", "--host=0.0.0.0"]
