from bs4 import BeautifulSoup as BS
import requests
from time import sleep
import pyfiglet

result = pyfiglet.figlet_format("Proxies Parser")
result1 = pyfiglet.figlet_format("by Swenly")
print(f'{result}\n{result1}')

HEADERS = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:87.0) Gecko/20100101 Firefox/87.0'
}

print()

try:
    f = open('http.txt', 'r')
    h_read = f.read()
    f.close()
except:
    print('Создаю http.txt')
    open('http.txt', 'w').write('')
    f = open('http.txt', 'r')
    h_read = f.read()
    f.close()
    sleep(1)
try:
    f = open('socks4.txt', 'r')
    s4_read = f.read()
    f.close()
except:
    print('Создаю socks4.txt')
    open('socks4.txt', 'w').write('')
    f = open('socks4.txt', 'r')
    s4_read = f.read()
    f.close()
    sleep(1)
try:
    f = open('socks5.txt', 'r')
    s5_read = f.read()
    f.close()
except:
    print('Создаю socks5.txt')
    open('socks5.txt', 'w').write('')
    f = open('socks5.txt', 'r')
    s5_read = f.read()
    f.close()
    sleep(1)

#!Socks4
print()
sleep(1)
print('Парсю socks4...')

with open('socks4.txt', 'a') as file:
    lol = 0
    r = requests.get(f'https://hidemy.name/ru/proxy-list/?type=4#list', headers=HEADERS)
    soup = BS(r.content, 'html.parser')
    proxies = soup.find('div', class_='table_block').find('tbody').find_all('tr')
    for i in proxies:
        _proxy = i.find('td')
        _port = _proxy.find_next('td').text
        _proxy = _proxy.text
        proxy = _proxy + ':' + _port
        if proxy in s4_read: continue
        if lol == 0:
            if s4_read == [''] or s4_read == [] or s4_read == '':
                file.write(proxy)
            lol = 1
        else:
            file.write(f'\n' + proxy)

while True:
    try:
        with open('socks4.txt', 'a') as file:
            site = soup.find('li', class_='next_array').find('a').get('href')

            r = requests.get(f'https://hidemy.name{site}', headers=HEADERS)
            soup = BS(r.content, 'html.parser')

            proxies = soup.find('div', class_='table_block').find('tbody').find_all('tr')

            for i in proxies:
                _proxy = i.find('td')
                _port = _proxy.find_next('td').text
                _proxy = _proxy.text
                proxy = _proxy + ':' + _port
                if proxy in s4_read: continue
                file.write(f'\n' + proxy)

    except Exception as e:
        break

r = requests.get(f'https://github.com/TheSpeedX/PROXY-List/blob/master/socks4.txt', headers=HEADERS)
soup = BS(r.content, 'html.parser')

proxies = soup.find_all('tr')

with open('socks4.txt', 'a') as file:
    for i in proxies:
        proxy = i.text.split('\n')[2]
        if proxy in open('socks4.txt', 'r').read(): continue
        file.write('\n' + proxy)

r = requests.get(f'https://api.openproxylist.xyz/socks4.txt', headers=HEADERS)

proxies = str(r.content).split(f'\n')[0].split(f'\\n')

with open('socks4.txt', 'a') as file:
    for i in proxies:
        if i in open('socks4.txt', 'r').read(): continue
        file.write('\n' + i)

print('Успешно!')

#!Socks5
sleep(1)
print()
print('Парсю socks5...')

with open('socks5.txt', 'a') as file:
    lol = 0
    r = requests.get(f'https://hidemy.name/ru/proxy-list/?type=5#list', headers=HEADERS)
    soup = BS(r.content, 'html.parser')
    proxies = soup.find('div', class_='table_block').find('tbody').find_all('tr')
    for i in proxies:
        _proxy = i.find('td')
        _port = _proxy.find_next('td').text
        _proxy = _proxy.text
        proxy = _proxy + ':' + _port
        if proxy in s5_read: continue
        if lol == 0:
            if s5_read == [''] or s5_read == [] or s5_read == '':
                file.write(proxy)
            lol = 1
        else:
            file.write(f'\n' + proxy)

while True:
    try:
        with open('socks5.txt', 'a') as file:
            site = soup.find('li', class_='next_array').find('a').get('href')

            r = requests.get(f'https://hidemy.name{site}', headers=HEADERS)
            soup = BS(r.content, 'html.parser')

            proxies = soup.find('div', class_='table_block').find('tbody').find_all('tr')

            for i in proxies:
                _proxy = i.find('td')
                _port = _proxy.find_next('td').text
                _proxy = _proxy.text
                proxy = _proxy + ':' + _port
                if proxy in s5_read: continue
                file.write(f'\n' + proxy)

    except Exception as e:
        break

r = requests.get(f'https://www.socks-proxy.net/', headers=HEADERS)
soup = BS(r.content, 'html.parser')

proxies = soup.find('table', class_='table table-striped table-bordered').find('tbody').find_all('tr')

r = requests.get(f'https://github.com/TheSpeedX/PROXY-List/blob/master/socks5.txt', headers=HEADERS)
soup = BS(r.content, 'html.parser')

proxies = soup.find_all('tr')

with open('socks5.txt', 'a') as file:
    for i in proxies:
        proxy = i.text.split('\n')[2]
        if proxy in open('socks5.txt', 'r').read(): continue
        file.write('\n' + proxy)

print('Успешно!')

#! HTTP
sleep(1)
print()
print('Парсю http...')

with open('http.txt', 'a') as file:
    lol = 0
    r = requests.get(f'https://hidemy.name/ru/proxy-list/?maxtime=100#list', headers=HEADERS)
    soup = BS(r.content, 'html.parser')
    proxies = soup.find('div', class_='table_block').find('tbody').find_all('tr')
    for i in proxies:
        _proxy = i.find('td')
        _port = _proxy.find_next('td').text
        _proxy = _proxy.text
        proxy = _proxy + ':' + _port
        if proxy in h_read: continue
        if lol == 0:
            if h_read == [''] or h_read == [] or h_read == '':
                file.write(proxy)
                lol = 1
        else:
            file.write(f'\n' + proxy)
while True:
    try:
        with open('http.txt', 'a') as file:
            site = soup.find('li', class_='next_array').find('a').get('href')

            r = requests.get(f'https://hidemy.name{site}', headers=HEADERS)
            soup = BS(r.content, 'html.parser')

            proxies = soup.find('div', class_='table_block').find('tbody').find_all('tr')

            for i in proxies:
                _proxy = i.find('td')
                _port = _proxy.find_next('td').text
                _proxy = _proxy.text
                proxy = _proxy + ':' + _port
                if proxy in h_read: continue
                file.write(f'\n' + proxy)

    except Exception as e:
        break

r = requests.get(f'https://github.com/TheSpeedX/PROXY-List/blob/master/http.txt', headers=HEADERS)
soup = BS(r.content, 'html.parser')

proxies = soup.find_all('tr')

with open('http.txt', 'a') as file:
    for i in proxies:
        proxy = i.text.split('\n')[2]
        if proxy in open('http.txt', 'r').read(): continue
        file.write('\n' + proxy)

print('Успешно!')

