import json


class Response:
    def __init__(self) -> None:
        self.success = False
        self.error = False
        self.msg = None
        self.data = None

    def setStatus(self, success=True, error=False, msg=None, data=None):
        if success:
            self.success = True
            self.error = False
        elif error:
            self.error = True
            self.success = False
        self.msg = msg
        self.data = data

    def json(self):
        return json.dumps({
            "success": self.success,
            "error": self.error,
            "msg": self.msg,
            "data": self.data
        }, indent=4)
