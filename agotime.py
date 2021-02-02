import time
import datetime


# 实例一
"""
threeDayAgo = (datetime.datetime.now() - datetime.timedelta(days=3))

timeStamp = int(time.mktime(threeDayAgo.timetuple()))

otherStyleTime = threeDayAgo.strftime('%Y-%m-%d %H:%M:%S')
print(otherStyleTime)
"""
# 实例二

timeStamp = 155702800
dateArray = datetime.datetime.utcfromtimestamp(timeStamp)
threeDayAgo = dateArray - datetime.timedelta(days=3)

print(threeDayAgo)
