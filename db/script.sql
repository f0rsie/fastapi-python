-- Active: 1724671743141@@127.0.0.1@5432@postgres
CREATE SCHEMA fastapi;

CREATE TABLE "fastapi"."Pings" (
    "Id" SERIAL PRIMARY KEY,
    "Url" VARCHAR(50) NOT NULL,
    "IsAvailable" BOOLEAN NOT NULL,
    "Ping" VARCHAR(50) NOT NULL,
    "Time" VARCHAR(60) NOT NULL
)