class G9:
    def reset_server_gen9(self):
        response = self.REDFISH_OBJ.get("/Systems/1/")
        system_path = response.obj["Actions"]["#ComputerSystem.Reset"]["target"]
        body = dict()
        body["Action"] = "Reset"
        body["ResetType"] = "ForceRestart"
        response = self.REDFISH_OBJ.post(system_path, body)
        if response.status == 400:
            try:
                return self.response.render(
                    response, response.obj["error"]["@Message.ExtendedInfo"]
                )
            except Exception as e:
                return self.response.render(response, str(e))
        elif response.status != 200:
            return self.response.render(
                response,
                "An http response of '{}' was returned.".format(response.status),
            )
        else:
            return self.response.render(response, response.dict)

    def get_bios_setting_gen9(self):
        bios_uri = "/redfish/v1/systems/1/bios"
        response = self.REDFISH_OBJ.get(bios_uri)
        return self.response.render(response, response.dict)
