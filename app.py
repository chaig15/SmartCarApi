from flask import request, jsonify
from SmartCar.GmApiUtils.GmApiService import GmApiService
from SmartCar import app
from SmartCar.error import SmartCarApiException


@app.route('/vehicles/<int:id>', methods=['GET'])
def vehicle_info(id):
    """
    endpoint for vehicle info
    :param id: vehicle_id
    :return: json_response
    """
    app.logger.info(f'Getting Vehicle Info for vehicle id: {id}')
    service = GmApiService(id)
    response = service.get_vehicle_info()
    return jsonify(response)


@app.route('/vehicles/<int:id>/engine', methods=['POST'])
def vehicle_engine(id):
    """
    endpoint for start/stop vehicle info, which takes json_body in request
    :param id: vehicle_id
    :return: json_response
    """
    if request.data:
        app.logger.info(f'Starting/Stopping Engine for vehicle_id: {id}')
        service = GmApiService(id)
        json_body = request.get_json()
        response = service.start_stop_engine(json_body)
        return response
    raise SmartCarApiException(message='Empty Request')


@app.route('/vehicles/<int:id>/doors', methods=['GET'])
def vehicle_door_info(id):
    """
    endpoint for vehicle door info
    :param id: vehicle_id
    :return: json_response
    """
    app.logger.info(f'Getting Door Info for vehicle_id: {id}')
    service = GmApiService(id)
    response = service.get_door_info()
    return jsonify(response)


@app.route('/vehicles/<int:id>/fuel', methods=['GET'])
def vehicle_fuel_info(id):
    """
    endpoint for vehicle fuel info
    :param id: vehicle_id
    :return: json_response
    """
    app.logger.info(f'Getting Fuel Info for vehicle_id: {id}')
    service = GmApiService(id)
    response = service.get_fuel_info()
    return jsonify(response)


@app.route('/vehicles/<int:id>/fuel', methods=['GET'])
def vehicle_battery_info(id):
    """
    endpoint for vehicle battery info
    :param id: vehicle_id
    :return: json_response
    """
    app.logger.info(f'Getting Battery Info for vehicle_id: {id}')
    service = GmApiService(id)
    response = service.get_battery_info()
    return jsonify(response)


if __name__ == "__main__":
    app.run()