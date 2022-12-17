from bs4 import BeautifulSoup
import requests
import json


def main():
    url = "https://monsterhunterrise.wiki.fextralife.com/Skills"
    res = requests.get(url)
    usable_site = BeautifulSoup(res.text, "html.parser")
    table = usable_site.find("tbody")
    skills = {}
    print(len(table.find_all("tr")))
    for row in table.find_all("tr"):
        skill_name = ""
        skill_max_level = 0
        for i, cell in enumerate(row.find_all("td")):
            if i == 0:
                skill_name = cell.text
            elif i == 2:
                skill_max_level = cell.text[0]

        try:
            skills[skill_name] = int(skill_max_level)
        except ValueError:
            skills[skill_name] = skill_max_level

    with open("../raw_data/skills.json", "w") as outfile:
        outfile.write(json.dumps(skills))


if __name__ == "__main__":
    main()
