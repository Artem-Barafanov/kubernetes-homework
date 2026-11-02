from flask import Flask, jsonify
import requests
import os

app = Flask(__name__)

BACKEND_URL = os.getenv(
    "BACKEND_URL",
    "http://backend-service:5000"
)

@app.route("/")
def home():
    response = requests.get(BACKEND_URL, timeout=5)
    response.raise_for_status()
    return jsonify({
        "frontend": "Hello from Kubernetes frontend!",
        "backend_response": response.json()
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
