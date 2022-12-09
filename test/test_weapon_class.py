import unittest
from app_layer.weapon import Weapon


class MyTestCase(unittest.TestCase):
    def setUp(self):
        test_equip_dict = {
            "name": "Sword_thing",
            "rarity": 6,
            "type": "weapon",
            "raw_base": 180,
            "sharpness": 5,
            "affinity": 20,
            "jewelSlots": [2, 1, 0],
            "defense": 10,
            "element": {
                "type": "blast",
                "value": 24
            },
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

        self.weap_dict = Weapon(test_equip_dict)
        self.empty_weap = Weapon()

    def test_init_dict(self):
        self.assertEqual(self.weap_dict.raw, 180)
        self.assertEqual(self.weap_dict.sharpness, 5)
        self.assertEqual(self.weap_dict.affinity, 20)
        self.assertEqual(self.weap_dict.element, {
            "type": "blast",
            "value": 24
        })

    def test_init_empty(self):
        self.assertEqual(self.empty_weap.raw, 0)
        self.assertEqual(self.empty_weap.sharpness, 0)
        self.assertEqual(self.empty_weap.affinity, 0)
        self.assertEqual(self.empty_weap.element, {
            "type": "",
            "value": 0
        })


if __name__ == '__main__':
    unittest.main()
