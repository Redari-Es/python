import calendar
yy = int(input('请输入年份：'))
mm = int(input('请输入月份：'))
monthRange = calendar.monthrange(yy, mm)
print(monthRange)
