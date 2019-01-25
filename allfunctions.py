# All functions are specified in this module

# Module imports
import humanize    # For making data human-readable


def memoryconv(jsoninput):
    max_value = jsoninput['result'][0]['value_max']
    return humanize.naturalsize(max_value, binary=True)


def dataspeedconv(jsoninput):
    max_value = jsoninput['result'][0]['value_max']
    return humanize.naturalsize(max_value, binary=True) + "/s"
