import urllib
import re

url = 'https://www.minbank.ru/'
resp = urllib.request.urlopen(url)
respData = resp.read()

currencies = re.findall(r'course-no-changed">([0-9]+.[0-9]+)', str(respData))

file = open('output.txt', 'w')
file.write('Minbank.ru\n')
file.write('USD (покупка/продажа): {}/{}\n'.format(currencies[0], currencies[1]))
file.write('EUR (покупка/продажа): {}/{}\n'.format(currencies[2], currencies[3]))

file.close()