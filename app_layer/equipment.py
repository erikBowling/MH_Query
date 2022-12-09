from multipledispatch import dispatch

# Parent class for armor and weapon


class Equipment(object):

    @dispatch()
    def __init__(self) -> None:
        self.__name: str = ""
        self.__type: str = ""
        self.__defense: int = 0
        self.__jewel_slots: list[int] = [0, 0, 0]

    @dispatch(dict)
    def __init__(self, equip_dict: dict) -> None:
        self.__name: str = equip_dict.get("name")
        self.__type: str = equip_dict.get("type")
        self.__defense: int = equip_dict.get("defense")
        self.__jewel_slots: list[int] = equip_dict.get("jewelSlots")

    @property
    def name(self) -> str:
        return self.__name

    @property
    def type(self) -> str:
        return self.__type

    @property
    def defense(self) -> int:
        return self.__defense

    @property
    def jewel_slots(self) -> list[int]:
        return self.__jewel_slots
