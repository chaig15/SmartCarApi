base_url = 'http://gmapi.azurewebsites.net/'
import requests
from SmartCar.error import SmartCarApiException

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
            response_json = r.json()
            if r.ok and response_json.get('status') == '200':
                return r.json()
            else:
                raise SmartCarApiException(message=response_json.get('reason'), status_code=response_json.get('status'))
        except Exception as e:
            if isinstance(e, SmartCarApiException):
                raise e
            else:
                raise SmartCarApiException()

    def start_stop_engine(self, json_body: dict):
        """
        calls actionEngineService endpoint after modifying json_body request
        :param json_body: json request body
        :return: cleaned json_response from GMAPI
        """
        value = json_body['ACTION']
        if value == 'START':
            json_body = {
                'command': 'START_VEHICLE'
            }
        elif value == 'STOP':
            json_body = {
                'command': 'STOP_VEHICLE'
            }
        else:
            raise Exception('Invalid Param:', json_body)
        self.request_body.update(json_body)
        response = self.__call_endpoint(endpoint='actionEngineService', request_type='POST', json=self.request_body)
        status = response['actionResult']['status']
        return response


    # def start_stop_engine(self, json_body: dict):
    #
    #     self.request_body.update(var)
    #     response = self.__call_endpoint(endpoint='/actionEngineService', request_type='POST', )
    #     return response


