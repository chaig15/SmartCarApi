from flask import Flask, jsonify
from SmartCar.error import SmartCarApiException

app = Flask(__name__)


@app.errorhandler(SmartCarApiException)
def handle_smart_car_exception(e):
    return jsonify(e.create()), e.status_code


@app.errorhandler(Exception)
def handle_generic_exception(e):
    return jsonify(str(e)), 400
