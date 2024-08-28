from typing import Any
import psycopg2
import os
from db.db_base import DbBase
from db.models.model_base import ModelBase


class DbPg(DbBase):
    conenction = None

    def __init__(self):
        try:
            self.conenct()

        except Exception as ex:
            print(ex)

    def conenct(self):
        try:
            connection = psycopg2.connect(
                dbname=os.environ["POSTGRES_DB"],
                host=os.environ["DB_HOST"],
                user=os.environ["POSTGRES_USER"],
                password=os.environ["POSTGRES_PASSWORD"],
                port=os.environ["DB_PORT"],
            )
            self.connection = connection

        except Exception as ex:
            print(ex)

    def get_all(self, table_name: str) -> list[ModelBase]:
        result: list[ModelBase] = []
        try:
            if self.connection is None:
                self.conenct()

            query_str: str = f"""SELECT * FROM "fastapi"."{table_name}"""

            cursor = self.connection.cursor()
            cursor.execute(query_str)

            records = cursor.fetchone()
            print(records)
            self.connection.commit()
            cursor.close()

        except Exception as ex:
            print(ex)

        finally:
            return result

    def get_by_id(self, table_name: str, id: int) -> list[Any]:
        result: list[Any] = []
        try:
            if self.connection is None:
                self.conenct()

            query_str: str = f"""SELECT * FROM "fastapi"."{table_name}" 
                                WHERE "id"={id}"""

            cursor = self.connection.cursor()
            cursor.execute(query_str)

            result = cursor.fetchall()

            self.connection.commit()
            cursor.close()

        except Exception as ex:
            print(ex)

        finally:
            return result

    def delete_by_id(self, table_name: str, id: int) -> bool:
        result: bool = False
        try:
            if self.connection is None:
                self.conenct()

            query_str: str = f"""DELETE FROM "fastapi"."{table_name}" 
                                WHERE "id"={id}"""

            cursor = self.connection.cursor()
            cursor.execute(query_str)

            self.connection.commit()
            cursor.close()

            result = True

        except Exception as ex:
            print(ex)

        finally:
            return result

    def delete_by_sql_params(self, table_name: str, sql_params: str) -> bool:
        result: bool = False
        try:
            if self.connection is None:
                self.conenct()

            query_str: str = f"""DELETE FROM "fastapi"."{table_name}" 
                                WHERE {sql_params}"""

            cursor = self.connection.cursor()
            cursor.execute(query_str)

            self.connection.commit()
            cursor.close()

            result = True

        except Exception as ex:
            print(ex)

        finally:
            return result

    def add_to(self, table_name: str, table: ModelBase) -> bool:
        result: bool = False
        try:
            if self.connection is None:
                self.conenct()

            query_str: str = f"""INSERT INTO "fastapi"."{table_name}"({", ".join(map(str, tuple(table.get_fields())))}) 
                                VALUES {tuple(table.get_values())}"""

            cursor = self.connection.cursor()
            cursor.execute(query_str)

            self.connection.commit()
            cursor.close()

            result = True

        except Exception as ex:
            print(ex)

        finally:
            return result
