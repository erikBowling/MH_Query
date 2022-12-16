from flask import Flask, redirect, url_for, render_template, request
from data_layer.mongo_bridge import MongoBridge

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():
    mon_bridge = MongoBridge()
    content = None
    if request.method == "POST":
        search = request.form.get("skill")
        content = mon_bridge.get_items_from_skill(search)

    return render_template("index.html", content=content)


if __name__ == "__main__":
    app.run()
