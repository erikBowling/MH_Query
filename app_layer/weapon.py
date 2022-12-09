from multipledispatch import dispatch
from app_layer.equipment import Equipment


class Weapon(Equipment):

    @dispatch()
    def __init__(self) -> None:
        super().__init__()
        self.__raw: int = 0
        self.__sharpness: int = 0
        self.__affinity: int = 0
        self.__element: dict = {
            "type": "",
            "value": 0
        }

    @dispatch(dict)
    def __init__(self, equip_dict) -> None:
        super().__init__(equip_dict)
        self.__raw: int = equip_dict.get("raw_base")
        self.__sharpness: int = equip_dict.get("sharpness")
        self.__affinity: int = equip_dict.get("affinity")
        self.__element: dict = equip_dict.get("element")

    @property
    def raw(self) -> int:
        return self.__raw

    @property
    def sharpness(self) -> int:
        return self.__sharpness

    @property
    def affinity(self) -> int:
        return self.__affinity

    @property
    def element(self) -> dict:
        return self.__element
