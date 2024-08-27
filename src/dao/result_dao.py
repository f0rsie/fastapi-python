from typing import Any
from dao.dao_base import DaoBase
from db.db_base import DbBase
from db.db_pg import DbPg
from db.models.ping_model import PingModel
from db.models.model_base import ModelBase
from utils import read_file, check_ping, read_file_async

# TODO: make controller for this dao
class ResultDAO(DaoBase):

    def __init__(self, db: DbBase, path_file: str):
        self.db: DbBase = db
        self.path_file: str = path_file #TODO: посмотри работу с файлами на питоне

    def add_data_to_db(self, table: ModelBase) -> ModelBase:
        try:
            result: ModelBase = table

            self.db.add_to("pings", table)

            return result

        except Exception as ex:
            print(ex)

            return table

    def get_all_data_from_db(self) -> list[ModelBase]:
        try:
            result: list[ModelBase] = self.db.get_all("pings")

            return result

        except Exception as ex:
            print(ex)

            return []

    def get_data_by_id(self, parameter: Any) -> list[ModelBase]:
        try:
            dictionary: dict[str, Any] = {"id": parameter}
            result: list[ModelBase] = self.db.get_by("pings", dictionary)

            return result

        except Exception as ex:
            print(ex)

            return []

    def check_pings(self) -> list[PingModel]:
        try:
            url_list: list[str] = read_file(self.path_file)
            urls_pings: list[PingModel] = []

            for url in url_list:
                url_PingModel: PingModel = check_ping(url)
                urls_pings.append(url_PingModel)

            return urls_pings

        except Exception as ex:
            print(ex)

            return []

    def check_and_save(self) -> list[ModelBase]:
        try:
            result: list[ModelBase] = []

            pings: list[PingModel] = self.check_pings()
            for ping in pings:
                self.add_data_to_db(ping)
                result.append(ping)

            return result

        except Exception as ex:
            print(ex)

            return []
