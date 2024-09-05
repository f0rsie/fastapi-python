-- Active: 1724680656125@@db@5432@fastapi
CREATE SCHEMA fastapi;

CREATE TABLE "fastapi"."pings" (
    "id" UUID PRIMARY KEY NOT NULL,
    "url" VARCHAR(50) NOT NULL,
    "is_available" BOOLEAN NOT NULL,
    "ping" VARCHAR(50) NOT NULL
)