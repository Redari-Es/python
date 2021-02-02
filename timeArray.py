import time

a1 = '2020-5-28 00:40:00'
timeArray = time.strptime(a1, "%Y-%m-%d %H:%M:%S")

timeStamp = int(time.mktime(timeArray))
print(timeStamp)


a2 = '2020-5-28 00:40:00'

timeArray = time.strptime(a2, "%Y-%m-%d %H:%M:%S")
otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)

print(otherStyleTime)
