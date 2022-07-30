from flask import Flask, request, jsonify, abort, render_template
from flask_restful import Api, Resource
from marshmallow import Schema, fields
from SmartCar.GmApiUtils.GmApiService import GmApiService
from SmartCar import app
from SmartCar.error import SmartCarApiException


@app.route('/vehicles/<int:id>', methods=['GET'])
def vehicle(id):
    service = GmApiService(id)
    response = service.post()
    return jsonify(response)


@app.route('/vehicles/<int:id>/engine', methods=['POST'])
def vehicle_engine(id):
    service = GmApiService(id)
    json_body = request.get_json()
    if json_body is None:
        abort(400)
    try:
        result = service.start_stop_engine(json_body)
        return jsonify(result)
    except Exception as e:
        print(e)
        raise SmartCarApiException(e)


app.run()
