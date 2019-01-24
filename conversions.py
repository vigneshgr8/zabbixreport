import json
from hurry import filesize
import zabbixgetdata

gotoutput = json.loads(zabbixgetdata.test)
hrconvvalue = filesize.iec(gotoutput['value_max'])
