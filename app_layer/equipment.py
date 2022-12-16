from multipledispatch import dispatch

# Parent class for armor and weapon


class Equipment(object):

    @dispatch()
    def __init__(self) -> None:
        self.__name: str = ""
        # self.__type: str = ""
        self.__rank: str = ""
        self.__rarity: int = 0
        self.__defense: int = 0
        self.__slots: list[int] = []
        self.__crafting_mats: dict = {}

    @dispatch(dict)
    def __init__(self, equip_dict: dict) -> None:
        self.__name: str = equip_dict.get("name")
        # self.__type: str = equip_dict.get("type")
        self.__rank: str = equip_dict.get("rank")
        self.__rarity: int = equip_dict.get("rarity")
        self.__defense: int = equip_dict.get("defense")
        self.__jewel_slots: list[int] = equip_dict.get("slots")
        self.__crafting_mats: dict = equip_dict.get("crafting_materials")

    @property
    def name(self) -> str:
        return self.__name

    # @property
    # def type(self) -> str:
        # return self.__type

    @property
    def rank(self) -> str:
        return self.__rank

    @property
    def defense(self) -> int:
        return self.__defense

    @property
    def jewel_slots(self) -> list[int]:
        return self.__slots
