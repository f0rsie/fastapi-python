from typing import Any
import psycopg2
import os
from db.db_base import DbBase
from db.models.model_base import ModelBase
from exceptions.handlers import db_handler


class DbPg(DbBase):
    conenction = None

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
    def get_all(self, table_name: str) -> list[Any]:
        if self.connection is None:
            self.conenct()

        query_str: str = f"""SELECT * FROM "fastapi"."{table_name}"""

        cursor = self.connection.cursor()
        cursor.execute(query_str)

        result = cursor.fetchall()

        self.connection.commit()
        cursor.close()

        return result

    @db_handler
    def get_by_id(self, table_name: str, id: int) -> Any:
        if self.connection is None:
            self.conenct()

        query_str: str = f"""SELECT * FROM "fastapi"."{table_name}" 
                            WHERE "id"={id}"""

        cursor = self.connection.cursor()
        cursor.execute(query_str)

        result = cursor.fetchone()

        self.connection.commit()
        cursor.close()

        return result

    @db_handler
    def delete_by_id(self, table_name: str, id: int) -> bool:
        result: bool = False
        if self.connection is None:
            self.conenct()

        query_str: str = f"""DELETE FROM "fastapi"."{table_name}" 
                            WHERE "id"={id}"""

        cursor = self.connection.cursor()
        cursor.execute(query_str)

        self.connection.commit()
        cursor.close()

        result = True

        return result

    @db_handler
    def delete_by_sql_params(self, table_name: str, sql_params: str) -> bool:
        result: bool = False
        if self.connection is None:
            self.conenct()

        query_str: str = f"""DELETE FROM "fastapi"."{table_name}" 
                            WHERE {sql_params}"""

        cursor = self.connection.cursor()
        cursor.execute(query_str)

        self.connection.commit()
        cursor.close()

        result = True

        return result

    @db_handler
    def add_to(self, table_name: str, table: ModelBase) -> bool:
        result: bool = False
        if self.connection is None:
            self.conenct()

        query_str: str = f"""INSERT INTO "fastapi"."{table_name}"({", ".join(map(str, tuple(table.get_fields())))}) 
                            VALUES {tuple(table.get_values())}"""

        cursor = self.connection.cursor()
        cursor.execute(query_str)

        self.connection.commit()
        cursor.close()

        result = True

        return result
