import time
import datetime
import json

from hurry import filesize

#import zabbixgetdata

today = datetime.date.today()
unix_today = time.mktime(datetime.datetime.strptime(str(today), "%Y-%m-%d").timetuple())
yesterday = datetime.date.today() - datetime.timedelta(days=1)
unix_yesterday = time.mktime(datetime.datetime.strptime(str(yesterday), "%Y-%m-%d").timetuple())
# print(today)
# print(int(unix_today))
# print (yesterday)
# print(int(unix_yesterday))

#gotoutput = json.loads(zabbixgetdata.test)

#hrvalue = filesize.iec(gotoutput['value_max'])