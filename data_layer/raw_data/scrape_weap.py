import requests
from bs4 import BeautifulSoup

def main():
    url = "https://monsterhunterrise.wiki.fextralife.com/Dual+Blades+List"
    res = requests.get(url)

    doc = BeautifulSoup(res.text, "html.parser")
    
    table = doc.find("tbody") # Body of the table

    rows = table.find_all("tr")

    items = []
    
    for row in rows:
        item = []
        cells = row.find_all("td")
        for i, cell in enumerate(cells):

            if i == 0:
                item.append(cell.find("a").text)

            elif i == 1 or i == 3 or i == 4 or i == 5:
                item.append(cell.string)

            elif i == 2:
                if cell.find('a') is not None:
                    item.append([cell.find('a').text, ''.join(char for char in cell.text if char.isdigit())])
                else:
                    item.append(cell.string)

            
            elif i == 6:
                ul = cell.find_all("li")
                rampage_skills = []
                for li in ul:
                    if li.find("a") is not None:
                        rampage_skills.append(li.find("a").string)
                    else:
                        rampage_skills.append(li.string)

                item.append(rampage_skills)

            elif i == 7:
                crafting_list = []
                ul = cell.find_all("li")

                for j, li in enumerate(ul):
                    if li.find('a') is not None:
                        crafting_list.append(li.find('a').string)
                    else:
                        if j == 0:
                            crafting_list.append(''.join(char for char in li.text if char.isdigit()))
                        else:
                            crafting_list.append(li.text)

                item.append(crafting_list)

        items.append(item)

    with open("./dual_blades.txt", "w") as file:
        for lis in items:
            file.write(f"{lis}\n")



if __name__ == "__main__":
    main()