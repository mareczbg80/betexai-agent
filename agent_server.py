from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # dozvoljava pozive sa tvoje WP stranice

@app.route('/betexai', methods=['POST'])
def process_request():
    data = request.get_json()
    user_input = data.get("prompt", "").lower()

    # 👉 Ovo je demo logika – možeš kasnije povezati sa pravim API
    if "zvezda" in user_input and "partizan" in user_input:
        return """
⚔️ Zvezda vs Partizan
🔍 Pre-match analiza – Zvezda u formi, Partizan sa slabim učinkom u derbijima
📊 xG: 1.85 vs 1.22, SoG: 6 vs 3
✅ Over 2.5 @ 1.85 – verovatnoća 71%, value zona +14%
📌 Glavni ulaz pre meča – tempo i stil obe ekipe podržavaju over
"""
    else:
        return "⚠️ Nije prepoznat meč – probaj sa 'zvezda vs partizan'"

if __name__ == "__main__":
    app.run(port=5000)
