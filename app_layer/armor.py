from multipledispatch import dispatch
from app_layer.equipment import Equipment


class Armor(Equipment):

    @dispatch()
    def __init__(self) -> None:
        super().__init__()
        self.__elemental_def: dict = {
            "fire": 0,
            "water": 0,
            "lightning": 0,
            "ice": 0,
            "dragon": 0
        }

        self.__skills: dict = {}

    @dispatch(dict)
    def __init__(self, equip_dict: dict) -> None:
        super().__init__(equip_dict)
        self.__elemental_def: list[int] = equip_dict.get("elementalDefense")
        self.__skills: dict = equip_dict.get("skills")

    @property
    def elemental_def(self) -> dict:
        return self.__elemental_def

    @property
    def skills(self) -> dict:
        return self.__skills
