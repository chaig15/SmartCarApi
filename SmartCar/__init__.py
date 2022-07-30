from flask import Flask, jsonify
from SmartCar.error import SmartCarApiException

app = Flask(__name__)


@app.errorhandler(SmartCarApiException)
def handle_bad_request(e):
    return jsonify(e.create()), e.status_code
