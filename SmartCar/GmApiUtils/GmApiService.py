base_url = 'http://gmapi.azurewebsites.net/'
import requests


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
        :return:
        """
        url = base_url+endpoint
        try:
            print(self.headers)
            r = requests.request(request_type, url, headers=self.headers, **kwargs)
            if r.ok:
                print('test')
                print(r.status_code)
                return r.json()
            else:
                raise Exception()
        except Exception as e:
            print(e)
            raise e

    def start_stop_engine(self, json_body: dict):
        """
        calls actionEngineService endpoint with given json_body
        :param json_body:
        :return:
        """
        try:
            value = json_body['ACTION']
            self.request_body.update(json_body)
            print(self.request_body)
            response = self.__call_endpoint(endpoint='/actionEngineService', request_type='POST', json=self.request_body)
            print(response)
            return response
        except Exception as e:
            raise Exception("The key 'ACTION' must be present with a value of: 'START' or 'STOP'")


    # def start_stop_engine(self, json_body: dict):
    #
    #     self.request_body.update(var)
    #     response = self.__call_endpoint(endpoint='/actionEngineService', request_type='POST', )
    #     return response


