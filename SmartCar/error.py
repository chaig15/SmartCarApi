from werkzeug.exceptions import BadRequest, HTTPException


class SmartCarApiException(Exception):
    status_code = 400
    message = 'API ERROR'

    def __init__(self, message=None, status_code=None, payload=None):
        super().__init__()
        if message is not None:
            self.message = message
        if status_code is not None:
            self.status_code = status_code
        self.payload = payload

    def create(self):
        response = dict(self.payload or ())
        response['message'] = self.message
        return response



