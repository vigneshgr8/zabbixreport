# credentials and logging in

# Import the ZabbixAPI module
from pyzabbix.api import ZabbixAPI

user_name = 'Admin'
password_zab = 'zabbix'
zab_url = 'http://192.168.2.226/zabbix'

zapi = ZabbixAPI(url=zab_url, user=user_name, password=password_zab)