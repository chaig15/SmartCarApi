class SmartCarApiException(Exception):
    """
    Exception Wrapper for SmartCarApiExceptions
    """
    status_code = 400
    message = 'INTERNAL API ERROR'

    def __init__(self, message=None, status_code=None, payload=None):
        super().__init__()
        if message is not None:
            self.message = message
        if status_code is not None:
            self.status_code = status_code
        self.payload = payload

    def create(self):
        response = dict()
        response['payload'] = self.payload
        response['message'] = self.message
        response['status_code'] = self.status_code
        return response



