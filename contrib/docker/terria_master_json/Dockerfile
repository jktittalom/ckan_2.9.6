FROM python:3.8-slim-buster

WORKDIR /jiten_terria_master

COPY jiten_terria_master/requirements.txt requirements.txt
RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .


CMD [ "python", "-m" , "flask", "run", "--host=0.0.0.0"]