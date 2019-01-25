# Import the ZabbixAPI module
from pyzabbix.api import ZabbixAPI

# variable imports
import cred
import variablein
import allfunctions

zapi = ZabbixAPI(url=cred.zab_url, user=cred.user_name, password=cred.password_zab)


def zapi_request(item):

    request = zapi.do_request(method='trend.get', params={
        'output': [

            'itemid',
            'value_max'
        ],
        'itemids': [
            item
        ],
        'limit': '1',
        'time_from': variablein.unix_yesterday,
        'time_till': variablein.unix_today
    })
    return request

hrvalue = allfunctions.dataspeedconv(zapi_request(23316))
print(hrvalue)

print(zapi_request(23316))
