import humanize


def jsonconvert(jsoninput):
    max_value = jsoninput['result'][0]['value_max']
    return humanize.naturalsize(max_value, binary=True)
