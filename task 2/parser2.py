import requests
from bs4 import BeautifulSoup

HOST = 'https://www.python.org'
URL = 'https://www.python.org/events/python-events/'
HEADERS = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36'
}


def get_html(url, params=None):
    r = requests.get(url, headers=HEADERS, params=params)
    return r


def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    events = []
    for ul in soup.find_all('ul', class_='list-recent-events menu'):
        for li in ul.find_all('li'):
            events.append({
                'title': li.find('h3', class_='event-title').get_text(strip=True),
                'date': li.find('p').get_text(strip=True),
                'link': HOST + li.find('h3', class_='event-title').find('a').get('href')
            })
        print(events)
        return events


def parse():
    html = get_html(URL)
    if html.status_code == 200:
        get_content(html.text)
    else:
        print('Error')


parse()
