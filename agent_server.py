from flask import Flask, request, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

@app.route("/")
def status():
    return jsonify({"status": "BetExAi agent is running."})

@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.get_json()
    message = data.get("message", "").lower()

    if "zvezda" in message and "partizan" in message:
        response = (
            "⚔️ Meč (Zvezda vs Partizan)\n"
            "🔍 Pre-match analiza – Zvezda u formi, Partizan sa slabim učinkom u derbijima\n"
            "📊 xG: 1.85 vs 1.22, SoG: 6 vs 3\n"
            "✅ Over 2.5 @ 1.85 – verovatnoća 71%, value zona +14%\n"
            "📌 Glavni ulaz pre meča – tempo i stil obe ekipe podržavaju over"
        )
    else:
        response = "⚔️ Meč nije pronađen ili još nije analiziran. Pošalji naziv dva tima (npr. Zvezda vs Partizan)."

    return jsonify({"response": response})

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
