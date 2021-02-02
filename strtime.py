import time
import datetime

# 实例一
'''
now = int(time.time())

timeArray = time.localtime(now)
otherStyleTime = time.strftime('%Y-%m-%d %H:%M:%S', timeArray)''
print(otherStyleTime)
'''

# 实例二
'''
now = datetime.datetime.now()

otherStyleTime = now.strftime('%Y-%m-%d %H:%M:%S')

print(otherStyleTime)
'''

# 实例三
'''
timeStamp = 1557502800
timeArray = time.localtime(timeStamp)

otherStyleTime = time.strftime('%Y-%m-%d %H:%M:%S', timeArray)
print(otherStyleTime)
'''

# 实例四

timeStamp = 1557502800
dateArray = datetime.datetime.utcfromtimestamp(timeStamp)
otherStyleTime = dateArray.strftime('%Y-%m-%d %H:%M:%S')
print(otherStyleTime)
