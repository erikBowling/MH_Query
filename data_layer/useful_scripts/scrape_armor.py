import requests
import json
from bs4 import BeautifulSoup


def main():
    rank_tables_url = "https://monsterhunterrise.wiki.fextralife.com/Armor+Set+Comparison+Table"
    rank_tables_res = requests.get(rank_tables_url)
    rank_tables_page = BeautifulSoup(rank_tables_res.text, "html.parser")

    tables = rank_tables_page.find_all("tbody")
    ranks = ["Master", "High", "Low"]
    armor = []
    for rank_ind, table in enumerate(tables):
        rows = table.find_all("tr")
        for row in rows:
            first_cell = row.find("td")
            href = first_cell.find("a").get("href")

            set_url = f"https://monsterhunterrise.wiki.fextralife.com{href}"
            set_res = requests.get(set_url)
            set_page = BeautifulSoup(set_res.text, "html.parser")

            set_tables = set_page.find_all("tbody")

            for second_row in set_tables[1].find_all("tr"):
                piece = {
                    "name": "",
                    "rarity": "",
                    "defense": "",
                    "rank": ranks[rank_ind],
                    "slots": [],
                    "resistance": {
                        "fire": 0,
                        "water": 0,
                        "thunder": 0,
                        "ice": 0,
                        "dragon": 0
                    },

                    "skills": {},
                    "crafting_list": {}
                }

                first_cell = second_row.find("td")
                if first_cell.find("a") is None:
                    continue
                href = first_cell.find("a").get("href")

                piece_url = f"https://monsterhunterrise.wiki.fextralife.com/{href}"
                piece_res = requests.get(piece_url)
                piece_page = BeautifulSoup(piece_res.text, "html.parser")

                bonfire = piece_page.find("h3", class_="bonfire")
                print(bonfire.text.split("Craft ")[1])

                crafting_ul = bonfire.find_next_sibling("ul")

                # Crafting list in middle of page

                for li in crafting_ul.find_all('li'):
                    if li.find('a') is not None:
                        temp = li.text.split(" x", 1)
                        if len(temp) == 1:
                            temp = li.text.split("\xa0x", 1)
                        if len(temp) == 1:
                            temp = li.text.split("x", 1)
                        if len(temp) == 1:
                            temp = li.text.split("&nbsp;x", 1)

                        try:
                            piece['crafting_list'][f'{temp[0]}'] = temp[1]
                        except IndexError:
                            piece['crafting_list'][f'{li.text}'] = '0'
                    else:
                        piece['crafting_list']['Zenny'] = li.text

                piece_table = piece_page.find('tbody')
                for i, r in enumerate(piece_table.find_all("tr")):
                    s = ""
                    for child in r.children:
                        s += child.text

                    s = s.strip()

                    if i == 0:
                        piece['name'] = s
                    elif i == 1 or i == 10:
                        continue
                    elif i == 2:
                        piece['rarity'] = s.split("Rarity")[1]
                    elif i == 3:
                        piece['defense'] = s.split("Defense\n")[1]
                    elif i == 4:
                        img_tags = r.find_all("img")
                        for img in img_tags:
                            if img.get(
                                    "src") == "/file/Monster-Hunter-Rise/decoration_level_4_icon_monster_hunter_rise_wiki_guide_24px.png":
                                piece['slots'].append(4)
                            elif img.get(
                                    "src") == "/file/Monster-Hunter-Rise/gem_level_3_icon_monster_hunter_rise_wiki_guide_24px.png":
                                piece['slots'].append(3)
                            elif img.get(
                                    "src") == "/file/Monster-Hunter-Rise/gem_level_2_icon_monster_hunter_rise_wiki_guide_24px.png":
                                piece['slots'].append(2)
                            elif img.get(
                                    "src") == "/file/Monster-Hunter-Rise/gem_level_1_icon_monster_hunter_rise_wiki_guide_24px.png":
                                piece['slots'].append(1)

                    elif i == 5:
                        piece['resistance']['fire'] = s.split("Res.\n")[1]
                    elif i == 6:
                        piece['resistance']['water'] = s.split("Res.\n")[1]
                    elif i == 7:
                        piece['resistance']['thunder'] = s.split("Res.\n")[1]
                    elif i == 8:
                        piece['resistance']['ice'] = s.split("Res.\n")[1]
                    elif i == 9:
                        piece['resistance']['dragon'] = s.split("Res.\n")[1]

                    elif i == 10:
                        continue

                    elif i == 11:
                        while True:
                            if len(s) == 0:
                                break
                            for j, char in enumerate(s):
                                if char.isdigit():
                                    piece['skills'][f'{s[0:j]}'.split('\xa0x')[0]] = s[j]
                                    break
                            s = s[j + 1:]
                armor.append(piece)

    with open('../raw_data/test_armor.json', 'w') as file:
        file.write("[\n")
        for arm in armor:
            file.write("\t\t" + json.dumps(arm) + ',\n')

        file.write("]")


def test():
    test_url = "https://monsterhunterrise.wiki.fextralife.com/Royal+Artillery+Corps"
    test_res = requests.get(test_url)
    test_page = BeautifulSoup(test_res.text, "html.parser")

    set_tables = test_page.find_all("tbody")
    armor = []
    for row in set_tables[1].find_all("tr"):

        first_cell = row.find("td")
        href = first_cell.find("a").get("href")

        piece_url = f"https://monsterhunterrise.wiki.fextralife.com/{href}"
        piece_res = requests.get(piece_url)
        piece_page = BeautifulSoup(piece_res.text, "html.parser")

        bonfire = piece_page.find("h3", class_="bonfire")
        crafting_ul = bonfire.find_next_sibling("ul")

        piece = {
            "name": "",
            "rarity": "",
            "defense": "",
            "slots": [],
            "resistance": {
                "fire": 0,
                "water": 0,
                "thunder": 0,
                "ice": 0,
                "dragon": 0
            },

            "skills": {},
            "crafting_list": {}
        }

        # Crafting list in middle of page

        for li in crafting_ul.find_all('li'):
            if li.find('a') is not None:
                temp = li.text.split(" x", 1)
                if len(temp) == 1:
                    temp = li.text.split("\xa0x", 1)
                if len(temp) == 1:
                    temp = li.text.split("x", 1)
                if len(temp) == 1:
                    temp = li.text.split("&nbsp;x", 1)

                try:
                    piece['crafting_list'][f'{temp[0]}'] = temp[1]
                except IndexError:
                    piece['crafting_list'][f'{li.text}'] = '0'
            else:
                piece['crafting_list']['Zenny'] = li.text

        # Armor Table in top left
        piece_table = piece_page.find('tbody')
        for i, r in enumerate(piece_table.find_all("tr")):
            s = ""
            for child in r.children:
                s += child.text

            s = s.strip()

            if i == 0:
                piece['name'] = s
            elif i == 1 or i == 10:
                continue
            elif i == 2:
                piece['rarity'] = s.split("Rarity ")[1]
            elif i == 3:
                piece['defense'] = s.split("Defense\n")[1]
            elif i == 4:
                img_tags = r.find_all("img")
                for img in img_tags:
                    if img.get(
                            "src") == "/file/Monster-Hunter-Rise/decoration_level_4_icon_monster_hunter_rise_wiki_guide_24px.png":
                        piece['slots'].append(4)
                    elif img.get(
                            "src") == "/file/Monster-Hunter-Rise/gem_level_3_icon_monster_hunter_rise_wiki_guide_24px.png":
                        piece['slots'].append(3)
                    elif img.get(
                            "src") == "/file/Monster-Hunter-Rise/gem_level_2_icon_monster_hunter_rise_wiki_guide_24px.png":
                        piece['slots'].append(2)
                    elif img.get(
                            "src") == "/file/Monster-Hunter-Rise/gem_level_1_icon_monster_hunter_rise_wiki_guide_24px.png":
                        piece['slots'].append(1)

            elif i == 5:
                piece['resistance']['fire'] = s.split("Res.\n")[1]
            elif i == 6:
                piece['resistance']['water'] = s.split("Res.\n")[1]
            elif i == 7:
                piece['resistance']['thunder'] = s.split("Res.\n")[1]
            elif i == 8:
                piece['resistance']['ice'] = s.split("Res.\n")[1]
            elif i == 9:
                piece['resistance']['dragon'] = s.split("Res.\n")[1]

            elif i == 10:
                continue

            elif i == 11:
                while True:
                    if len(s) == 0:
                        break
                    for j, char in enumerate(s):
                        if char.isdigit():
                            piece['skills'][f'{s[0:j]}'.split('\xa0x', 1)[0]] = s[j]
                            break
                    s = s[j + 1:]
        armor.append(piece)
        print(piece)

    with open('../raw_data/armor_test.json', 'w') as file:
        file.write("{\n\t\"armor\": [\n")
        for arm in armor:
            file.write("\t\t" + json.dumps(arm) + ',\n')

        file.write("\t]\n}")


if __name__ == "__main__":
    main()
