from flask import Flask, request, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET'])
def home():
    return jsonify({"status": "BetExAi agent is running."})

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.get_json()
    user_input = data.get('message', '')

    # OVDE IDE TVOJA OBRADA – za sada simuliramo odgovor
    response = {
        "response": f"⚔️ Meč: {user_input}\n🔍 Trenutno obrađujem podatke za tvoju analizu... sačekaj trenutak!"
    }
    return jsonify(response)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
