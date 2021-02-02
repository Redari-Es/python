import re


def Find(string):
    url = re.findall('https?://(?:[-\w.]|(?:%[\da-fA-F{2}]))+', string)
    return url


string = 'Redaries的网址是：https://www.redaries.xyz, Google得网址为：https://www.google.com'
print("urls: ", Find(string))
