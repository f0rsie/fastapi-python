FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY src/ ./src/

WORKDIR /app/src

EXPOSE 8000

ENTRYPOINT [ "python", "main.py" ]