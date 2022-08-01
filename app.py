from flask import Flask, request, jsonify, abort, render_template
from flask_restful import Api, Resource
from marshmallow import Schema, fields
from SmartCar.GmApiUtils.GmApiService import GmApiService
from SmartCar import app
from SmartCar.error import SmartCarApiException


@app.route('/vehicles/<int:id>', methods=['GET'])
def vehicle_info(id):
    app.logger.info('Getting Vehicle Info')
    service = GmApiService(id)
    response = service.get_vehicle_info()
    return jsonify(response)


@app.route('/vehicles/<int:id>/engine', methods=['POST'])
def vehicle_engine(id):
    if request.data:
        app.logger.info('Starting/Stopping Engine')
        service = GmApiService(id)
        json_body = request.get_json()
        response = service.start_stop_engine(json_body)
        return response
    raise SmartCarApiException(message='Empty Request')


@app.route('/vehicles/<int:id>/doors', methods=['GET'])
def vehicle_door_info(id):
    app.logger.info('Getting Door Info')
    service = GmApiService(id)
    response = service.get_door_info()
    return jsonify(response)


if __name__ == "__main__":
    app.run(debug=True)