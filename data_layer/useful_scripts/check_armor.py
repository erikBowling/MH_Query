import json


def main():
    with open("../raw_data/armor.json", "r") as file:
        total_json = json.load(file)
        for i, arm in enumerate(total_json):
            if arm["crafting_list"]["Zenny"] == 0:
                print(f"line {i}: {arm['name']} has 0 Zenny")


if __name__ == "__main__":
    main()
