from flask import Flask, jsonify

app = Flask(__name__)


@app.get("/health")
def health():
    return jsonify({"status": "healthy"}), 200


@app.get("/products")
def products():
    return jsonify([
        {"id": 1, "name": "Keyboard"},
        {"id": 2, "name": "Mouse"}
    ]), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
