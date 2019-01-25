# All functions are specified in this module

# Module imports
import cred
import variablein
import humanize    # For making data human-readable


def memoryconv(jsoninput):
    max_value = jsoninput['result'][0]['value_max']
    return humanize.naturalsize(max_value, binary=True)


def dataspeedconv(jsoninput):
    max_value = jsoninput['result'][0]['value_max']
    return humanize.naturalsize(max_value, binary=True) + "/s"


def zapi_request(item):

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
