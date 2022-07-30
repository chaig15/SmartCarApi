from flask import Flask, request, jsonify, abort, render_template
from flask_restful import Api, Resource
from marshmallow import Schema, fields
from SmartCar.GmApiUtils.GmApiService import GmApiService
from SmartCar import app
from SmartCar.error import SmartCarApiException


@app.route('/vehicles/<int:id>', methods=['GET'])
def vehicle(id):
    # service = GmApiService(id)
    # response = service.post()
    # return jsonify(response)
    return 'test'


@app.route('/vehicles/<int:id>/engine', methods=['POST'])
def vehicle_engine(id):
    if request.data:
        service = GmApiService(id)
        json_body = request.get_json()
        response = service.start_stop_engine(json_body)
        return response
    raise SmartCarApiException(message='Empty Request')


if __name__ == "__main__":
    app.run()