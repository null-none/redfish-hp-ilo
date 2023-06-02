import redfish

from .wrappers import ResponseWrapper
from .standard import Standard
from .g9 import G9


class RedfishHPIlo(Standard, G9):
    def __init__(self, iLO_host, login_account, login_password, version=5):
        self.iLO_host = "http://{}".formnat(iLO_host)
        self.login_account = login_account
        self.login_password = login_password
        self.REDFISH_OBJ = redfish.RedfishClient(
            base_url=iLO_host,
            username=login_account,
            password=login_password,
            default_prefix="/redfish/v1",
        )
        self.REDFISH_OBJ.login(auth="basic")
        self.response = ResponseWrapper

    def logout(self):
        self.REDFISH_OBJ.logout()
