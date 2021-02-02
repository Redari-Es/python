# 实例一
'''
str = 'redaries'
print(len(str))

'''
# 实例二


def findLen(str):
    counter = 0
    while str[counter:]:
        counter += 1
    return counter


str = 'redaries'
print(findLen(str))
