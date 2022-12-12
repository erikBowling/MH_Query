import json

local_files = ["great_swords", "sword_and_shields", "dual_blades", "long_swords", "hammers", "lances",
                   "hunting_horns", "gunlances", "switch_axes", "charge_blades", "insect_glaives", "bows",
                   "light_bowguns", "heavy_bowguns"]


def main():
    for url in local_files:
        with open(f"../raw_data/{url}.json", "r") as file, open("./weapon_error_log.txt", "a") as outfile:
            total_json = json.load(file)
            outfile.write(f"{url}\n")
            for i, weap in enumerate(total_json):
                if weap['raw'] is None:
                    outfile.write(f"\tLine ({i + 2}) Name: {weap['name']} -- Raw is None\n")

                if "element" in weap:
                    if weap["element"] is not None:
                        if len(weap["element"]) == 0:
                            outfile.write(f"\tLine ({i + 2}) Name: {weap['name']} -- Element is empty\n")

                if weap["rarity"] is None:
                    outfile.write(f"\tLine ({i + 2}) Name: {weap['name']} -- Rarity is none and Rank is Unknown\n")

                for item in weap["crafting_list"]:
                    if item == "Zenny":
                        if weap["crafting_list"][item] is None:
                            outfile.write(f"\tLine ({i + 2}) Name: {weap['name']} -- Zenny is none\n")
                    else:
                        if weap["crafting_list"][item] == 0:
                            outfile.write(f"\tLine ({i + 2}) Name: {weap['name']} -- Crafting_List, {item} is 0\n")

                if "shelling" in weap:
                    if weap["shelling"]["level"] is None:
                        outfile.write(f"\tLine ({i + 2}) Name: {weap['name']} -- Shelling level is none\n")


if __name__ == "__main__":
    main()
