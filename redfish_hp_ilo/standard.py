class Standard:
    def reset_server(self):
        managers_uri = self.REDFISH_OBJ.root.obj["Systems"]["@odata.id"]
        managers_response = self.REDFISH_OBJ.get(managers_uri)
        managers_members_uri = next(iter(managers_response.obj["Members"]))["@odata.id"]
        managers_members_response = self.REDFISH_OBJ.get(managers_members_uri)
        path = managers_members_response.obj["Actions"]["#ComputerSystem.Reset"][
            "target"
        ]
        body = dict()
        resettype = ["ForceRestart", "GracefulRestart"]
        body["Action"] = "ComputerSystem.Reset"
        for reset in resettype:
            if reset.lower() == "forcerestart":
                body["ResetType"] = "ForceRestart"
                response = self.REDFISH_OB.post(path, body)
            elif reset.lower() == "gracefulrestart":
                body["ResetType"] = "GracefulRestart"
                response = self.REDFISH_OBJ.post(path, body)
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

    def software_firmware_inventory(self, select="firmware"):
        result = []
        update_service_uri = self.REDFISH_OBJ.root.obj["UpdateService"]["@odata.id"]
        update_service_resp = self.REDFISH_OBJ.get(update_service_uri)
        if "software" in select.lower():
            inventory_uri = update_service_resp.obj["SoftwareInventory"]["@odata.id"]
        elif "firmware" in select.lower():
            inventory_uri = update_service_resp.obj["FirmwareInventory"]["@odata.id"]
        else:
            return self.response.render(response, "Invalid selection provided")
        members = self.REDFISH_OBJ.get(inventory_uri).obj["Members"]
        if not members:
            return self.response.render(response, "Inventory emptyd")
        else:
            for inventory_item in members:
                response = self.REDFISH_OBJ.get(inventory_item["@odata.id"])
                result.append(
                    {
                        "name": response.dict.get("Name"),
                        "description": response.dict.get("Description"),
                    }
                )
            return self.response.render(response, result)

    def reboot_server(self):
        systems_uri = self.REDFISH_OBJ.root.obj["Systems"]["@odata.id"]
        systems_response = self.REDFISH_OBJ.get(systems_uri)
        systems_uri = next(iter(systems_response.obj["Members"]))["@odata.id"]
        systems_response = self.REDFISH_OBJ.get(systems_uri)
        system_reboot_uri = systems_response.obj["Actions"]["#ComputerSystem.Reset"][
            "target"
        ]
        body = dict()
        resettype = ["ForceRestart", "GracefulRestart"]
        body["Action"] = "ComputerSystem.Reset"
        for reset in resettype:
            if reset.lower() == "forcerestart":
                body["ResetType"] = "ForceRestart"
                response = self.REDFISH_OBJ.post(system_reboot_uri, body)
            elif reset.lower() == "gracefulrestart":
                body["ResetType"] = "GracefulRestart"
                response = self.REDFISH_OBJ.post(system_reboot_uri, body)
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

    def get_bios_setting(self):
        systems_uri = self.REDFISH_OBJ.root.obj["Systems"]["@odata.id"]
        systems_response = self.REDFISH_OBJ.get(systems_uri)
        systems_members_uri = next(iter(systems_response.obj["Members"]))["@odata.id"]
        systems_members_response = self.REDFISH_OBJ.get(systems_members_uri)
        bios_uri = systems_members_response.obj["Bios"]["@odata.id"]
        bios_data = self.REDFISH_OBJ.get(bios_uri)
        return self.response.render(systems_members_response, bios_data.dict)
