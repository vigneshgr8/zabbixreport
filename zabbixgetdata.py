from pyzabbix.api import ZabbixAPI

#variables
user_name = 'admin'
password_zab = 'password'
zab_url = 'http://localhost/zabbix'

zapi = ZabbixAPI(url=zab_url, user=user_name, password=password_zab)

