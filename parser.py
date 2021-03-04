import requests
import bs4

def get_date(name):
    parsed = bs4.BeautifulSoup(requests.get('http://www.ulitka.tv/countdown.html').text, 'html.parser')
    for elem in parsed.find('table', id='genre-table').find_all('tr'):
        for serial in elem.find_all('td'):
            try:
                if name == serial.find('strong').text:
                    return str(serial.find('small')).replace('<small>', '').replace('<br/>', '\n').replace('</small>', '')
            except:
                pass

print(get_date('Цветы'))