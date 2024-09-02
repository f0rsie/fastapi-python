from typing import Any
import psycopg2
import os
from db.db_base import DbBase
from exceptions.handlers import db_handler


class DbPg(DbBase):

    connection: Any

    @db_handler
    def __init__(self):
        self.conenct()

    @db_handler
    def conenct(self):
        self.connection = psycopg2.connect(
            dbname=os.environ["POSTGRES_DB"],
            host=os.environ["DB_HOST"],
            user=os.environ["POSTGRES_USER"],
            password=os.environ["POSTGRES_PASSWORD"],
            port=os.environ["DB_PORT"],
        )

    @db_handler
    def get_all(self, table) -> list[Any]:
        if self.connection is None:
            self.conenct()

        query_str: str = f"""SELECT * FROM "fastapi"."{table}"""

        cursor = self.connection.cursor()
        cursor.execute(query_str)

        result = cursor.fetchall()

        self.connection.commit()
        cursor.close()

        return result

    @db_handler
    def get_by_id(self, table, id: int) -> Any:
        if self.connection is None:
            self.conenct()

        query_str: str = f"""SELECT * FROM "fastapi"."{table}" WHERE "id"={id}"""

        cursor = self.connection.cursor()
        cursor.execute(query_str)

        result = cursor.fetchone()

        self.connection.commit()
        cursor.close()

        return result

    @db_handler
    def delete_by_id(self, table, id: int) -> bool:
        result: bool = False
        if self.connection is None:
            self.conenct()

        query_str: str = f"""DELETE FROM "fastapi"."{table}" 
                            WHERE "id"={id}"""

        cursor = self.connection.cursor()
        cursor.execute(query_str)

        self.connection.commit()
        cursor.close()

        result = True

        return result

    @db_handler
    def add_to(self, table, data) -> bool:
        result: bool = False
        if self.connection is None:
            self.conenct()

        query_str: str = f"""INSERT INTO "fastapi"."{table}"({", ".join(map(str, tuple(table.get_fields())))}) 
                            VALUES {tuple(table.get_values())}"""

        cursor = self.connection.cursor()
        cursor.execute(query_str)

        self.connection.commit()
        cursor.close()

        result = True

        return result
