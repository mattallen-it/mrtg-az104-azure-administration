import os
from flask import Flask, jsonify

app = Flask(__name__)

@app.get("/")
def index():
    return jsonify(
        application="MRTG Lab 23",
        platform="Azure App Service",
        environment=os.getenv("LAB_ENVIRONMENT", "Unset"),
        version="1.0"
    )

@app.get("/health")
def health():
    return jsonify(status="healthy"), 200
