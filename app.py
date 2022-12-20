import pymongo.errors
from flask import Flask, redirect, url_for, render_template, request
import json

from data_layer.mongo_bridge import MongoBridge

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    mon_bridge: MongoBridge = MongoBridge()
    skills: dict = {}
    search = None
    with open("./data_layer/raw_data/skills.json") as file:
        skills = json.load(file)

    content = None
    if request.method == "POST":
        search = request.form.get("skill")
        try:
            content = mon_bridge.get_items_from_skill(search)
        except pymongo.errors.ServerSelectionTimeoutError:
            content = "Server not found"

    return render_template("index.html", skills=skills, content=content, prev_search=search)

if __name__ == "__main__":
    app.run()