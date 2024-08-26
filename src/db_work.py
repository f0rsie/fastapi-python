import psycopg2
import os

# TODO: DAO - sql raw
class DbWork:
    def connect_to_db(self):
        try:
            connection = psycopg2.connect(
                dbname=os.environ["POSTGRES_DB"],
                host=os.environ["DB_HOST"],
                user=os.environ["POSTGRES_USER"],
                password=os.environ["POSTGRES_PASSWORD"],
                port=os.environ["DB_PORT"],
            )
            return connection
        except Exception as ex:
            return None

    def add(self, data):
        connection = self.connect_to_db()

        if connection is not None:
            cursor = connection.cursor()
            cursor.execute(
                'INSERT INTO "fastapi"."Pings"("Url", "IsAvailable", "Ping", "Time") VALUES (%s, %s, %s, %s)',
                (data.url, data.is_available, data.ping_value, data.logtime),
            )
            connection.commit()

   #CRUD! на сущность Result