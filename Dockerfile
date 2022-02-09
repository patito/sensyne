FROM python:3.9

WORKDIR /app

COPY requirements-dev.txt requirements.txt /app/

RUN pip3 install -r requirements-dev.txt

COPY . /app

