import unittest
from app_layer.armor import Armor


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        test_equip_dict: dict = {
            "name": "Sword_thing",
            "rarity": 6,
            "type": "weapon",
            "raw_base": 180,
            "sharpness": 5,
            "affinity": 20,
            "jewelSlots": [2, 1, 0],
            "defense": 10,
            "elementalDefense": {
                "fire": -5,
                "water": 3,
                "lightning": 5,
                "ice": -1,
                "dragon": 2
            },
            "skills": {
                "Quick_Sheath": 1,
                "Partbreaker": 2
            }
        }

        self.arm = Armor(test_equip_dict)
        self.empty_arm = Armor()

    def test_init_dict(self):
        self.assertEqual(self.arm.elemental_def, {
            "fire": -5,
            "water": 3,
            "lightning": 5,
            "ice": -1,
            "dragon": 2
        })

        self.assertEqual(self.arm.skills, {
            "Quick_Sheath": 1,
            "Partbreaker": 2
        })

    def test_init_empty(self):
        self.assertEqual(self.empty_arm.elemental_def, {
            "fire": 0,
            "water": 0,
            "lightning": 0,
            "ice": 0,
            "dragon": 0
        })

        self.assertEqual(self.empty_arm.skills, {})

    def test_skills_list(self):
        self.assertEqual([("Quick_Sheath",  1), ("Partbreaker", 2)], self.arm.get_skills_list())


if __name__ == '__main__':
    unittest.main()
