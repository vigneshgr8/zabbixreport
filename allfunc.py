# All functions are specified in this module

# Module imports
import cred
import variablein
import humanize    # For making data human-readable


def memoryconv(jsoninput):  # Function to convert memory size to human readable
    max_value = jsoninput['result'][0]['value_max']
    return humanize.naturalsize(max_value, binary=True)


def dataspeedconv(jsoninput):  # Function to convert data transfer speed to human readable
    max_value = jsoninput['result'][0]['value_max']
    return humanize.naturalsize(max_value, binary=True) + "/s"


def zapi_request(item):  # Function to obtain data from Zabbix API through JSON request
    request = cred.zapi.do_request(method='trend.get', params={
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
