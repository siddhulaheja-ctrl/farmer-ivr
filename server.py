import os
from flask import Flask, request, jsonify

app = Flask(__name__)

BASE_URL = "https://farmer-ivr-jky0.onrender.com"   # your Render URL, no trailing slash

@app.route("/")
def home():
    return "IVR server is alive"

@app.route("/answer", methods=["GET", "POST"])
def answer():
    return jsonify([
        {
            "action": "talk",
            "text": "Namaste. Your procurement slot is booked for March fifteenth."
        },
        {
            "action": "input",
            "type": ["dtmf"],
            "dtmf": {"maxDigits": 1},
            "eventUrl": [f"{BASE_URL}/keypress"]
        }
    ])

@app.route("/keypress", methods=["POST"])
def keypress():
    data = request.get_json()
    print("RECEIVED:",data)
    digit = data.get("dtmf", {}).get("digits")

    if digit == "1":
        text = "Your bank details are confirmed. Thank you."
    elif digit == "2":
        text = "Your payment is pending and will be credited within forty eight hours."
    else:
        text = "Sorry, I did not understand that."

    return jsonify([{"action": "talk", "text": text}])

@app.route("/event", methods=["POST"])
def event():
    return "", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))