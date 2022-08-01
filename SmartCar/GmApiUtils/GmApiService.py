import requests
from SmartCar.error import SmartCarApiException
base_url = 'http://gmapi.azurewebsites.net/'


class GmApiService:

    def __init__(self, id):
        """
        creates GmApiService class based on given car id
        :param id: vehicle ID
        """
        self.id = id

        self.request_body = {
            "id": self.id,
            "responseType": "JSON"
        }

        self.headers = {
            'Content-Type': 'application/json'
        }

    def __call_endpoint(self, endpoint: str, request_type: str, **kwargs):
        """
        private helper function to make request to GM API with some default request bodies and headers when needed
        :param endpoint: endpoint for url
        :param request_type: REST type
        :param kwargs: any other params we want to send to the request module
        :return: json response on status 200
        :raises: SmartCarApiException with message and status
        """
        url = base_url+endpoint
        try:
            r = requests.request(request_type, url, headers=self.headers, **kwargs)
            return r
        except Exception as e:
            raise e

    def start_stop_engine(self, json_body: dict):
        """
        calls actionEngineService endpoint after modifying json_body request
        :param json_body: json request body
        :return: cleaned json_response from GMAPI
        """
        try:
            value = json_body['action']
            if value == 'START':
                json_body = {
                    'command': 'START_VEHICLE'
                }
            elif value == 'STOP':
                json_body = {
                    'command': 'STOP_VEHICLE'
                }
            else:
                raise Exception()
            self.request_body.update(json_body)
            r = self.__call_endpoint(endpoint='actionEngineService', request_type='POST', json=self.request_body)
            response_json = r.json()
            if r.ok and response_json.get('status') == '200':
                # process response json on success
                if response_json.get('actionResult').get('status') == 'EXECUTED':
                    status = 'success'
                else:
                    status = 'error'
                return ({
                    'action': status
                })
            else:
                raise SmartCarApiException(message=response_json.get('reason'), status_code=response_json.get('status'))
        except Exception as e:
            if isinstance(e, SmartCarApiException):
                raise e
            raise SmartCarApiException(message='INVALID API BODY:', payload=json_body)

    def get_vehicle_info(self):
        """
        calls VehicleInfoService from GM and cleans response
        :return: json response on success
        """
        try:
            r = self.__call_endpoint('getVehicleInfoService', request_type='POST', json=self.request_body)
            response_json = r.json()
            if r.ok and response_json.get('status') == '200':
                # extract needed info and return cleaned json
                vin = response_json['data']['vin']['value']
                color = response_json['data']['color']['value']
                drive_train = response_json['data']['driveTrain']['value']
                if response_json['data']['fourDoorSedan']['value'] == 'True':
                    door_count = 4
                elif response_json['data']['twoDoorCoup']['value'] == 'True':
                    door_count = 2
                else:
                    door_count = 'unknown'
                return ({
                    'vin:': vin,
                    "color": color,
                    "doorCount": door_count,
                    "driveTrain": drive_train
                })
            else:
                raise SmartCarApiException(message=response_json.get('reason'), status_code=response_json.get('status'))
        except Exception as e:
            if isinstance(e, SmartCarApiException):
                raise e
            raise SmartCarApiException()

    def get_door_info(self):
        """
        calls SecurityStatusService
        :return: json response with door status
        """
        try:
            r = self.__call_endpoint('getSecurityStatusService', request_type='POST', json=self.request_body)
            response_json = r.json()
            if r.ok and response_json.get('status') == '200':
                # extract door values and return json
                door_values = response_json['data']['doors']['values']
                to_return = []
                for value in door_values:
                    location = value['location']['value']
                    locked = bool(value['locked']['value'])
                    to_return.append({
                        'location': location,
                        'locked': locked
                    })
                return to_return
            else:
                raise SmartCarApiException(message=response_json.get('reason'), status_code=response_json.get('status'))
        except Exception as e:
            if isinstance(e, SmartCarApiException):
                raise e
            raise SmartCarApiException()

    def get_fuel_info(self):
        """
        calls EnergyService
        :return: json response with fuel status
        """
        try:
            r = self.__call_endpoint('getSecurityStatusService', request_type='POST', json=self.request_body)
            response_json = r.json()
            if r.ok and response_json.get('status') == '200':
                door_values = response_json['data']['doors']['values']
                to_return = []
                for value in door_values:
                    location = value['location']['value']
                    locked = bool(value['locked']['value'])
                    to_return.append({
                        'location': location,
                        'locked': locked
                    })
                return to_return
            else:
                raise SmartCarApiException(message=response_json.get('reason'), status_code=response_json.get('status'))
        except Exception as e:
            if isinstance(e, SmartCarApiException):
                raise e
            raise SmartCarApiException()

    def get_battery_info(self):
        """
        calls SecurityStatusService
        :return: json response with battery level
        """
        try:
            r = self.__call_endpoint('getSecurityStatusService', request_type='POST', json=self.request_body)
            response_json = r.json()
            if r.ok and response_json.get('status') == '200':
                door_values = response_json['data']['doors']['values']
                to_return = []
                for value in door_values:
                    location = value['location']['value']
                    locked = bool(value['locked']['value'])
                    to_return.append({
                        'location': location,
                        'locked': locked
                    })
                return to_return
            else:
                raise SmartCarApiException(message=response_json.get('reason'), status_code=response_json.get('status'))
        except Exception as e:
            if isinstance(e, SmartCarApiException):
                raise e
            raise SmartCarApiException()




