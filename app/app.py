from flask import Flask, jsonify
import time

app = Flask(__name__)

@app.route("/message", methods=["GET"])
def get_message():
    return jsonify({"message": "Zayzoon rocking here!", "timestamp": int(time.time())})

@app.route("/health", methods=["GET"])
def health_check():
    return jsonify({"status": "healthy"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
