import humanize


def memoryconv(jsoninput):
    max_value = jsoninput['result'][0]['value_max']
    return humanize.naturalsize(max_value, binary=True)

def dataspeedconv(jsoninput):
    max_value = jsoninput['result'][0]['value_max']
    return humanize.naturalsize(max_value, binary=True) + "/s"