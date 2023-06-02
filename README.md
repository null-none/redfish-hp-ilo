# redfish-hp-ilo
Redfish API implementation on HPE servers with iLO RESTful API

#### Install 
```bash
pip install redfish-hp-ilo
```

#### Examples

```python
from redfish_hp_ilo.api import RedfishHPIlo

handler = RedfishHPIlo()
handler.software_firmware_inventory("firmware")
handler.software_firmware_inventory("software")
handler.get_bios_setting()
handler.reboot_server()
handler.reset_server()

handler.reset_server_gen9()
handler.get_bios_setting_gen9()
```
