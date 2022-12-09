import unittest
from app_layer.equipment import Equipment


class MyTestCase(unittest.TestCase):
    def setUp(self):
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
                "lightning": 0,
                "ice": 0,
                "dragon": 0
            },
            "skills": {
                "Quick_Sheath": 1,
                "Partbreaker": 2
            }
        }

        self.equip = Equipment(test_equip_dict)
        self.empty_equip = Equipment()

    def test_init_dict(self):
        self.assertEqual(self.equip.name, "Sword_thing")
        self.assertEqual(self.equip.type, "weapon")
        self.assertEqual(self.equip.defense, 10)
        self.assertEqual(self.equip.jewel_slots, [2, 1, 0])

    def test_init_empty(self):
        self.assertEqual(self.empty_equip.name, "")
        self.assertEqual(self.empty_equip.type, "")
        self.assertEqual(self.empty_equip.defense, 0)
        self.assertEqual(self.empty_equip.jewel_slots, [0, 0, 0])


if __name__ == '__main__':
    unittest.main()
