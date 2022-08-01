from flask import Flask, jsonify
from SmartCar.error import SmartCarApiException
import logging

app = Flask(__name__)
app.logger.setLevel(logging.INFO)


@app.errorhandler(SmartCarApiException)
def handle_smart_car_exception(e):
    return jsonify(e.create()), e.status_code


@app.errorhandler(Exception)
def handle_generic_exception(e):
    return jsonify(str(e)), 400
