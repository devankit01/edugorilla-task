FROM python:3.8
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
RUN apt-get update && apt-get install mariadb-server -y
WORKDIR /code
COPY requirements.txt /code/
RUN pip3 install -r requirements.txt
COPY . /code/