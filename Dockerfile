FROM python:3.12-slim AS base
WORKDIR /app
COPY src/ ./src/

FROM base AS dev
WORKDIR /app
COPY requirements.txt .
COPY requirements-dev.txt .
RUN pip install -r requirements-dev.txt
EXPOSE 8000

FROM python:3.12-alpine AS prod
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY --from=base /app/src /app/src
EXPOSE 8000
CMD [ "python", "src/main.py" ]