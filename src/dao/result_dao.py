from typing import Any
from dao.dao_base import DaoBase
from db.db_base import DbBase
from db.db_pg import DbPg
from db.models.ping_model import PingModel
from db.models.model_base import ModelBase
from utils import read_file, check_ping, async_read_file, async_check_ping


# TODO: make controller for this dao
class ResultDAO(DaoBase):

    def __init__(self, db: DbBase, path_file: str):
        self.db: DbBase = db
        self.path_file: str = path_file  # TODO: посмотри работу с файлами на питоне

    def add_data_to_db(self, table: ModelBase) -> bool:
        result: bool = False
        try:
            result = self.db.add_to("pings", table)

        except Exception as ex:
            print(ex)

        finally:
            return result

    def get_all_data_from_db(self, table_name: str) -> list[ModelBase]:
        result: list[ModelBase] = []
        try:
            result = self.db.get_all(table_name)

        except Exception as ex:
            print(ex)

        finally:
            return result

    def delete_by_id(self, table_name: str, id: int) -> bool:
        result: bool = False
        try:
            result = self.db.delete_by_id(table_name, id)

        except Exception as ex:
            print(ex)

        finally:
            return result

    def delete_by_sql_params(self, table_name: str, sql_params: str) -> bool:
        result: bool = False
        try:
            result = self.db.delete_by_sql_params(table_name, sql_params)

        except Exception as ex:
            print(ex)

        finally:
            return result

    def get_data_by_id(self, table_name: str, id: int) -> list[ModelBase]:
        result: list[ModelBase] = []
        try:
            result = self.db.get_by_id(table_name, id)

        except Exception as ex:
            print(ex)

        finally:
            return result

    def check_pings(self) -> list[PingModel]:
        result: list[PingModel] = []
        try:
            url_list: list[str] = read_file(self.path_file)

            for url in url_list:
                url_PingModel: PingModel = check_ping(url)
                result.append(url_PingModel)

        except Exception as ex:
            print(ex)

        finally:
            return result

    def check_and_save(self) -> list[ModelBase]:
        result: list[ModelBase] = []
        try:
            pings: list[PingModel] = self.check_pings()
            for ping in pings:
                self.add_data_to_db(ping)
                result.append(ping)

        except Exception as ex:
            print(ex)

        finally:
            return result

    async def async_check_pings(self) -> list[PingModel]:
        result: list[PingModel] = []
        try:
            url_list: list[str] = await async_read_file(self.path_file)

            for url in url_list:
                url_PingModel: PingModel = await async_check_ping(url)
                result.append(url_PingModel)

        except Exception as ex:
            print(ex)

        finally:
            return result

    async def async_check_and_save(self) -> list[ModelBase]:
        result: list[ModelBase] = []
        try:
            pings: list[PingModel] = await self.async_check_pings()
            for ping in pings:
                self.add_data_to_db(ping)
                result.append(ping)

        except Exception as ex:
            print(ex)

        finally:
            return result
