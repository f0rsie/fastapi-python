FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt
RUN apt-get update && apt-get install -y iputils-ping

COPY src/* ./src/

WORKDIR /app/src

EXPOSE 8000

ENTRYPOINT [ "python", "main.py" ]