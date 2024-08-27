from typing import Any
import psycopg2
import os
from db.db_base import DbBase
from db.models.model_base import ModelBase


class DbPg(DbBase):
    connection = None

    def check_connection(self) -> Any | None:
        try:
            if self.connection is not None:
                return self.connection
            else:
                return None

        except Exception as ex:
            print(ex)

            return None

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

            return connection

        except Exception as ex:
            print(ex)

            return None

    def get_all(self, table_name: str) -> list[ModelBase]:
        connection = self.conenct()

        if connection is not None:
            try:
                result: list[ModelBase] = []

                cursor = connection.cursor()
                cursor.execute('SELECT * FROM "fastapi"."%s"', table_name)

                records = cursor.fetchone()
                print(records)
                connection.commit()
                cursor.close()

                return result

            except Exception as ex:
                print(ex)

                return []

            finally:
                connection.close()
        else:
            raise Exception
        
    def get_by(self, table_name: str, parameters: dict[str, Any]) -> list[Any] | None:
        connection = self.conenct()

        if connection is not None:
            try:
                result: list[Any] = []
                
                parameters_query: str = ''

                print(parameters)

                for par in parameters.keys():
                    parameters_query += ' AND '.join(list([f"{par}={parameters.get(par)}"]))
                    print(par)

                query_str: str = f"""SELECT * FROM "fastapi"."{table_name}" 
                                    WHERE {parameters_query}"""
                
                cursor = connection.cursor()
                cursor.execute(query_str)

                result = cursor.fetchall()

                connection.commit()
                cursor.close()

                return result

            except Exception as ex:
                print(ex)

                return []

    def add_to(self, table_name: str, table: ModelBase) -> ModelBase:
        connection = self.conenct()

        if connection is not None:
            try:
                result: ModelBase = table

                query_str: str = f"""INSERT INTO "fastapi"."{table_name}"({", ".join(map(str, tuple(table.get_fields())))}) 
                                    VALUES {tuple(table.get_values())}"""

                cursor = connection.cursor()
                cursor.execute(query_str)

                connection.commit()
                cursor.close()

                return result

            except Exception as ex:
                print(ex)

                return table

            finally:
                connection.close()
        else:
            raise Exception
