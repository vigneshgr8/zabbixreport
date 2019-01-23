from pyzabbix.api import ZabbixAPI

#variables
user_name = 'Admin'
password_zab = '12345678'
zab_url = 'http://192.168.2.226/zabbix'

zapi = ZabbixAPI(url=zab_url, user=user_name, password=password_zab)

zapi.do_request('trend.get',
{
    "output": [
            "itemid",
            "clock",
            "num",
            "value_min",
            "value_avg",
            "value_max",
})