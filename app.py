import csv
from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/hello")
def hello():
    return jsonify({"status": "hello"})


@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.get_json(silent=True)
    if not data or "order" not in data:
        return jsonify({"status": "error"}), 400
    with open("test_orders.csv", "a", newline="") as f:
        csv.writer(f).writerow([data["order"], data.get("item"), data.get("qty")])
    return jsonify({"status": "ok"})
