import os
from flask import Flask, jsonify

app = Flask(__name__)
VERSION = "2.0"

@app.get("/")
def index():
    return jsonify(
        application="MRTG Lab 24",
        version=VERSION,
        environment=os.getenv("LAB_ENVIRONMENT", "Unset")
    )

@app.get("/health")
def health():
    return jsonify(status="healthy", version=VERSION), 200
