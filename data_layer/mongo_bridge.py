import pymongo
from multipledispatch import dispatch
from app_layer.armor import Armor


class MongoBridge:

    @dispatch()
    def __init__(self) -> None:
        self.__client = pymongo.MongoClient("mongodb://localhost:27017/")
        self.__collection = self.__client['Equipment']["Armor"]

    @dispatch(str, str, str)
    def __init__(self, uri: str, db: str, col: str) -> None:
        self.__client = pymongo.MongoClient(uri)
        self.__collection = self.__client[db][col]

    def get_all_items(self) -> list[dict]:
        result: list = []
        items = self.__collection.find()
        for item in items:
            result.append(item)

        return result

    def get_all_armor(self) -> list[Armor]:
        result: list[Armor] = []

        for item in self.__collection.find():
            result.append(Armor(item))

        return result

    def get_items_from_skill(self, search) -> list[Armor]:
        print(search)
        result: list[Armor] = []

        for item in self.__collection.find({f"skills.{search}": {"$exists": True}}):
            result.append(Armor(item))

        print(len(result))
        return result
