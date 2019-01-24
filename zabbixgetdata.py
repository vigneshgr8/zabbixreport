from pyzabbix.api import ZabbixAPI

# variable imports
import cred
import variableproc


zapi = ZabbixAPI(url=cred.zab_url, user=cred.user_name, password=cred.password_zab)

test = zapi.do_request(method='trend.get', params={
        "output": [
                "itemid",
                "value_max"
        ],
        "itemids": [
                "23316"
        ],
        "limit": "1",
        "time_from": variableproc.unix_yesterday,
        "time_till": variableproc.unix_today,
})

#print(variablegen.hrvalue)

print(test)
