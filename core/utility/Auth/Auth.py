from core.templates.Response import Response
from app_utils import log


class Auth:
    def jwt_login(self):
        res = Response()
        try:
            # Write jwt authentication logic below
            pass
        except Exception as e:
            log.exception(e)
            res.setStatus(error=True, msg=str(e))
        return res

    def login(self, username, password):
        res = Response()

        global log

        print("AT LOGIN : ", log)
        try:
            # Write login logic to create a new jwt
            pass
        except Exception as e:
            log.exception(e)
            res.setStatus(error=True, msg=str(e))
        return res
