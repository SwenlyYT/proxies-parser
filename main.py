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

r = requests.get(f'https://hidemy.name/ru/proxy-list/?maxtime=100#list', headers=HEADERS)
soup = BS(r.content, 'html.parser')

try:
    f = open('proxies.txt', 'r')
    f_read = f.read()
    f.close()
except:
    open('proxies.txt', 'w').write('')
    f = open('proxies.txt', 'r')
    f_read = f.read()
    f.close()

proxies = soup.find('div', class_='table_block').find('tbody').find_all('tr')

lol = 0

sleep(3)
print('Парсю прокси...')

with open('proxies.txt', 'a') as file:
    for i in proxies:
        proxy = i.find('td').text
        if proxy in f_read: continue
        if lol == 0:
            if f_read == [''] or f_read == [] or f_read == '':
                file.write(proxy)
                lol = 1
        else:
            file.write(f'\n' + proxy)

while True:
    try:
        with open('proxies.txt', 'a') as file:
            site = soup.find('li', class_='next_array').find('a').get('href')

            r = requests.get(f'https://hidemy.name{site}', headers=HEADERS)
            soup = BS(r.content, 'html.parser')

            proxies = soup.find('div', class_='table_block').find('tbody').find_all('tr')

            for i in proxies:
                proxy = i.find('td').text
                if proxy in f_read: continue
                if lol == 0:
                    if f_read == [''] or f_read == [] or f_read == '':
                        file.write(proxy)
                        lol = 1
                else:
                    file.write(f'\n' + proxy)
            

    except Exception as e:
        print(e)
        break

