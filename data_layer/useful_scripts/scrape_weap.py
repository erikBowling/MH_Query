import bs4.element
import requests
import json
from bs4 import BeautifulSoup


def main():
    all_weap_urls = ["Great+Swords", "Sword+&+Shields", "Dual+Blades+List", "Long+Swords", "Hammers", "Lances",
                     "Hunting+Horns", "Gunlances", "Switch+Axes", "Charge+Blades", "Insect+Glaives", "Bows",
                     "Light+Bowguns", "Heavy+Bowguns"]

    local_files = ["great_swords", "sword_and_shields", "dual_blades", "long_swords", "hammers", "lances",
                   "hunting_horns", "gunlances", "switch_axes", "charge_blades", "insect_glaives", "bows",
                   "light_bowguns", "heavy_bowguns"]

    # Main loop. Runs through each page

    for i, url in enumerate(all_weap_urls):
        temp_url = f"https://monsterhunterrise.wiki.fextralife.com/{url}"
        res = requests.get(temp_url)
        doc = BeautifulSoup(res.text, "html.parser")
        table = doc.find("tbody")
        rows = table.find_all("tr")
        items = []

        if i < 6:
            items = standard_weapon_scrape(rows)
        elif i == 6:
            items = hunting_horn_scrape(rows)
        elif i == 7:
            items = gunlance_scrape(rows)
        elif i == 8 or i == 9:
            items = switch_or_charge_scrape(rows)
        elif i == 10:
            items = insect_glaive_scrape(rows)
        elif i == 11:
            items = bow_scrape(rows)
        elif i > 11:
            items = gun_scrape(rows)

        with open(f"../raw_data/{local_files[i]}.json", "w") as file:
            file.write("{\n\t\"items\": [\n")
            for wep in items:
                file.write("\t\t" + json.dumps(wep) + ',\n')

            file.write("\t]\n}")


def standard_weapon_scrape(rows: bs4.element.ResultSet):
    items = []
    for row in rows:
        item = {
            "name": "",
            "raw": 0,
            "element": [],
            "affinity": 0,
            "defense": 0,
            "rarity": 0,
            "rampage_skills": [],
            "crafting_list": {}
        }
        cells = row.find_all("td")
        for i, cell in enumerate(cells):

            if i == 0:
                item["name"] = cell.find("a").text
            elif i == 1:
                item['raw'] = get_raw(cell)
            elif i == 2:
                item['element'] = get_element(cell)
            elif i == 3:
                item["affinity"] = int(cell.string.replace('%', '').replace("'", ""))
            elif i == 4:
                item['defense'] = get_defense(cell)
            elif i == 5:
                item['rarity'] = get_rarity(cell)
            elif i == 6:
                item['rampage_skills'] = get_rampage_skills(cell)
            elif i == 7:
                item['crafting_list'] = get_crafting_list(cell)

        items.append(item)

    return items


def hunting_horn_scrape(rows: bs4.element.ResultSet):
    items = []
    for row in rows:
        item = {
            "name": "",
            "raw": 0,
            "element": [],
            "affinity": 0,
            "defense": 0,
            "melodies": [],
            "rarity": 0,
            "rampage_skills": [],
            "crafting_list": {}
        }
        cells = row.find_all("td")
        for i, cell in enumerate(cells):

            if i == 0:
                item["name"] = cell.find("a").text
            elif i == 1:
                item['raw'] = get_raw(cell)
            elif i == 2:
                item['element'] = get_element(cell)
            elif i == 3:
                item["affinity"] = int(cell.string.replace('%', '').replace("'", ""))
            elif i == 4:
                item['defense'] = get_defense(cell)
            elif i == 5:
                for child in cell.children:
                    if type(child) == bs4.element.NavigableString:
                        item['melodies'].append(child.text.replace('\xa0', ''))
            elif i == 6:
                item['rarity'] = get_rarity(cell)
            elif i == 7:
                item['rampage_skills'] = get_rampage_skills(cell)
            elif i == 8:
                item['crafting_list'] = get_crafting_list(cell)

        items.append(item)

    return items


def gunlance_scrape(rows: bs4.element.ResultSet):
    items = []
    for row in rows:
        item = {
            "name": "",
            "raw": 0,
            "element": [],
            "affinity": 0,
            "defense": 0,
            "shelling": {
                "type": "",
                "level": 0
            },
            "rarity": 0,
            "rampage_skills": [],
            "crafting_list": {}
        }
        cells = row.find_all("td")
        for i, cell in enumerate(cells):

            if i == 0:
                item["name"] = cell.find("a").text
            elif i == 1:
                item['raw'] = get_raw(cell)
            elif i == 2:
                item['element'] = get_element(cell)
            elif i == 3:
                item["affinity"] = int(cell.string.replace('%', '').replace("'", ""))
            elif i == 4:
                item['defense'] = get_defense(cell)
            elif i == 5:
                item['shelling']['type'] = cell.text.replace('\u00a0', '')
            elif i == 6:
                try:
                    item['shelling']['level'] = int(cell.text[-1])
                except ValueError:
                    item['shelling']['level'] = None
            elif i == 7:
                item['rarity'] = get_rarity(cell)
            elif i == 8:
                item['rampage_skills'] = get_rampage_skills(cell)
            elif i == 9:
                item['crafting_list'] = get_crafting_list(cell)

        items.append(item)

    return items


def switch_or_charge_scrape(rows: bs4.element.ResultSet):
    items = []
    for row in rows:
        item = {
            "name": "",
            "raw": 0,
            "element": [],
            "affinity": 0,
            "defense": 0,
            "phial": "",
            "rarity": 0,
            "rampage_skills": [],
            "crafting_list": {}
        }
        cells = row.find_all("td")
        for i, cell in enumerate(cells):

            if i == 0:
                item["name"] = cell.find("a").text
            elif i == 1:
                item['raw'] = get_raw(cell)
            elif i == 2:
                item['element'] = get_element(cell)
            elif i == 3:
                item["affinity"] = int(cell.string.replace('%', '').replace("'", ""))
            elif i == 4:
                for child in cell.children:
                    if type(child) == bs4.element.NavigableString:
                        item["phial"] = child.text
                        break
                else:
                    item["phial"] = cell.text
            elif i == 5:
                item['defense'] = get_defense(cell)
            elif i == 6:
                item['rarity'] = get_rarity(cell)
            elif i == 7:
                item['rampage_skills'] = get_rampage_skills(cell)
            elif i == 8:
                item['crafting_list'] = get_crafting_list(cell)

        items.append(item)

    return items


def insect_glaive_scrape(rows: bs4.element.ResultSet):
    items = []
    for row in rows:
        item = {
            "name": "",
            "raw": 0,
            "element": [],
            "affinity": 0,
            "defense": 0,
            "kinsect_level": 0,
            "rarity": 0,
            "rampage_skills": [],
            "crafting_list": {}
        }
        cells = row.find_all("td")
        for i, cell in enumerate(cells):

            if i == 0:
                item["name"] = cell.find("a").text
            elif i == 1:
                item['raw'] = get_raw(cell)
            elif i == 2:
                item['element'] = get_element(cell)
            elif i == 3:
                item["affinity"] = int(cell.string.replace('%', '').replace("'", ""))
            elif i == 4:
                item["kinsect_level"] = int(cell.text.replace("\u00a0", '')[-1])
            elif i == 5:
                item['defense'] = get_defense(cell)
            elif i == 6:
                item['rarity'] = get_rarity(cell)
            elif i == 7:
                item['rampage_skills'] = get_rampage_skills(cell)
            elif i == 8:
                item['crafting_list'] = get_crafting_list(cell)

        items.append(item)

    return items


def bow_scrape(rows: bs4.element.ResultSet):
    items = []
    for row in rows:
        item = {
            "name": "",
            "raw": 0,
            "element": [],
            "affinity": 0,
            "arcshot": "",
            "charge_shots": {
                1: "",
                2: "",
                3: "",
                4: ""
            },
            "defense": 0,
            "rarity": 0,
            "rampage_skills": [],
            "coatings": [],
            "crafting_list": {}
        }
        cells = row.find_all("td")
        for i, cell in enumerate(cells):

            if i == 0:
                item["name"] = cell.find("a").text
            elif i == 1:
                item['raw'] = get_raw(cell)
            elif i == 2:
                item['element'] = get_element(cell)
            elif i == 3:
                item["affinity"] = int(cell.string.replace('%', '').replace("'", ""))
            elif i == 4:
                item["arcshot"] = cell.text
            elif 5 <= i <= 8:
                val = cell.text.replace('\u00a0', '')
                if val == '--':
                    item["charge_shots"][i-4] = None
                else:
                    item["charge_shots"][i-4] = val
            elif i == 9:
                item['defense'] = get_defense(cell)
            elif i == 10:
                item['rarity'] = get_rarity(cell)
            elif i == 11:
                item['rampage_skills'] = get_rampage_skills(cell)
            elif i == 12:
                for child in cell.children:
                    if type(child) == bs4.element.NavigableString:
                        item["coatings"].append(child.text)
            elif i == 13:
                item['crafting_list'] = get_crafting_list(cell)

        items.append(item)

    return items


def gun_scrape(rows: bs4.element.ResultSet):
    items = []
    for row in rows:
        item = {
            "name": "",
            "raw": 0,
            "affinity": 0,
            "deviation": "",
            "recoil": "",
            "reload": "",
            "cluster_bomb_type": "",
            "special_ammo": "",
            "defense": 0,
            "rarity": 0,
            "rampage_skills": [],
            "crafting_list": {}
        }
        cells = row.find_all("td")
        for i, cell in enumerate(cells):

            if i == 0:
                item["name"] = cell.find("a").text
            elif i == 1:
                item['raw'] = get_raw(cell)
            elif i == 2:
                item["affinity"] = int(cell.string.replace('%', '').replace("'", ""))
            elif i == 3:
                item["deviation"] = cell.text
            elif i == 4:
                item["recoil"] = cell.text
            elif i == 5:
                item["reload"] = cell.text
            elif i == 6:
                item["cluster_bomb_type"] = cell.text
            elif i == 7:
                item["special_ammo"] = cell.text
            elif i == 8:
                item['defense'] = get_defense(cell)
            elif i == 9:
                item['rarity'] = get_rarity(cell)
            elif i == 10:
                item['rampage_skills'] = get_rampage_skills(cell)
            elif i == 11:
                item['crafting_list'] = get_crafting_list(cell)

        items.append(item)

    return items


def get_raw(cell: bs4.element.Tag):
    try:
        return int(cell.string)
    except TypeError:
        return None
    except ValueError:
        return None


def get_element(cell: bs4.element.Tag):
    if cell.find('a') is not None:
        try:
            return [cell.find('a').text.replace('\u00a0', ''),
                    int(''.join(char for char in cell.text if char.isdigit()))]
        except ValueError:
            return None
    else:
        return None


def get_defense(cell: bs4.element.Tag):
    try:
        return int(cell.string)
    except ValueError:
        return 0


def get_rarity(cell: bs4.element.Tag):
    try:
        return int(cell.string[-2:])
    except ValueError:
        return None
    except TypeError:
        return None


def get_rampage_skills(cell: bs4.element.Tag):
    ul = cell.find_all("li")
    rampage_skills = []
    for li in ul:
        if li.find("a") is not None:
            rampage_skills.append(li.find("a").string)
        else:
            rampage_skills.append(li.string)

    return rampage_skills


def get_crafting_list(cell: bs4.element.Tag):
    ul = cell.find_all("li")
    item = {}
    for j, li in enumerate(ul):
        if li.find('a') is not None:
            try:
                item[f"{li.find('a').string}"] = int(
                    ''.join(char for char in li.text[-3:] if char.isdigit()))
            except ValueError:
                item[f"{li.find('a').string}"] = 0
        else:
            # Zenny
            if li.find('img') is not None:
                try:
                    item["Zenny"] = int(li.text.replace("'", ""))
                except ValueError:
                    item["Zenny"] = None

            # Monster Points
            else:
                item["Points"] = li.string.replace('\u00a0', '')

    return item


if __name__ == "__main__":
    main()
