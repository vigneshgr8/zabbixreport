# All the variable requirements and conversion are done here

# import time to convert date to unix time
import time

# import datetime to get date
import datetime


today = datetime.date.today()
unix_today = time.mktime(datetime.datetime.strptime(str(today), "%Y-%m-%d").timetuple())
yesterday = datetime.date.today() - datetime.timedelta(days=1)
unix_yesterday = time.mktime(datetime.datetime.strptime(str(yesterday), "%Y-%m-%d").timetuple())

application = "['CPU']"
host = "['Zabbix Server']"