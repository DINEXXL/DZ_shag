import urllib.request as ur
from bs4 import BeautifulSoup

openurl = ur.build_opener()
response = openurl.open('https://httbin.org/get')
print(response.read())

import requests

response = requests.get('https://coinmarketcap.com')
response = response.text
response_parse = response.split('<span>')
result_list = []
for element in response_parse:
    if element.startswith('$'):
        for result in element.split('</span>'):
            if result.startswith('$') and result[1].isdigit():
                result_list.append(result)

bitcoin_rate = result_list[0]
print(bitcoin_rate)

response = requests.post(
    url='https://httbin.org/get',
    data='Test data',
    headers={'h1': 'Test title'}
)
print(response.text)
print(type(response.text))

response = requests.get('https://coinmarketcap.com')
if response.status_code == 200:
    soup = BeautifulSoup(response.text, features='html.parser')
    soup_list = soup.find_all(
        'a', {'href': '/currencies/bitcoin/#markets'}
    )
    result = soup_list[0].find('span')
    print(result.text)