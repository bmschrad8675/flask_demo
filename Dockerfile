FROM python:alpine3.10
MAINTAINER brandon@simplelc.com

WORKDIR /app/

COPY requirements.txt /app/requirements.txt
RUN ["pip3", "install", "-r", "requirements.txt"]

COPY . /app/

EXPOSE 5050
CMD ["python3", "run.py"]
