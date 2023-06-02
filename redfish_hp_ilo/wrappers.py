class ResponseWrapper:
    def __init__(self):
        pass

    def render(self, response, data):
        if response.status >= 200 and response.status < 300:
            return {"status": "success", "data": data}
        else:
            return {
                "status": "error",
                "message": data,
                "status_code": response.status_code,
            }
