from multipledispatch import dispatch
from app_layer.equipment import Equipment


class Armor(Equipment):

    @dispatch()
    def __init__(self) -> None:
        super().__init__()
        self.__resistance: dict = {
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
        self.__resistance: dict = equip_dict.get("resistance")
        self.__skills: dict = equip_dict.get("skills")

    @property
    def elemental_def(self) -> dict:
        return self.__resistance

    @property
    def skills(self) -> dict:
        return self.__skills

    def get_skills_list(self) -> list[tuple[str, int]]:
        skills_list: list[tuple[str, int]] = []
        for key in self.__skills:
            skills_list.append((key, self.__skills[key]))

        return skills_list

