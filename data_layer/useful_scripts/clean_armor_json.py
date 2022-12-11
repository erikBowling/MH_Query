import json


def main():
    a_keys = ['resistance', 'skills', 'crafting_list']
    with open('../raw_data/armor.json', 'r') as infile, open('../raw_data/armor_test.json', 'w') as outfile:
        total_json = json.loads(infile.read())
        outfile.write("{\n\t\"armor\": [\n")
        for i, arm in enumerate(total_json['armor']):
            try:
                arm['rarity'] = int(arm['rarity'])
                arm['defense'] = int(arm['defense'])
                for key in a_keys:
                    for item in arm[key]:
                        arm[key][item] = int(arm[key][item].replace(',', ''))

            except ValueError:
                print(f"Error on line {i}: {arm}")

            try:
                old_skills = [s for s in arm['skills']]
                for skill in old_skills:
                    if skill[-1] == "x":
                        arm['skills'][skill[:-2]] = arm['skills'].pop(skill)
            except KeyError:
                print(f"Key error on line {i}: {arm}")

            outfile.write("\t" * 2 + json.dumps(arm) + ",\n")
        outfile.write("]\n}")


if __name__ == "__main__":
    main()
