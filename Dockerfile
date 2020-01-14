FROM python:alpine3.10
MAINTAINER brandon@simplelc.com

WORKDIR /app/

COPY requirements.txt /app/requirements.txt
RUN ["pip3", "install", "-r", "requirements.txt"]

COPY . /app/

CMD ["python3", "start.py"]
