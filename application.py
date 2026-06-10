from flask import Flask, jsonify
from flask_cors import CORS
import mysql.connector
import os

app = Flask(__name__)
CORS(app)

DB_HOST = os.getenv("DB_HOST", "db")
DB_USER = os.getenv("DB_USER", "root")
DB_PASSWORD = os.getenv("DB_PASSWORD", "root")
DB_NAME = os.getenv("DB_NAME", "carwebdb")

@app.route("/health")
def health():
    return jsonify({"status": "backend running"})

@app.route("/cars")
def cars():
    return jsonify([
        {"id": 1, "name": "Hyundai i20", "price": "8.5 Lakhs"},
        {"id": 2, "name": "Tata Nexon", "price": "10 Lakhs"},
        {"id": 3, "name": "Maruti Baleno", "price": "8 Lakhs"}
    ])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
