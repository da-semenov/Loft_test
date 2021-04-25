import requests
from bs4 import BeautifulSoup
import csv

CSV = 'events.csv'
URL = 'https://www.python.org'
HEADERS = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36'
}


def get_html(url, params=None):
    r = requests.get(url, headers=HEADERS, params=params)
    return r


def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    events = []
    for ul in soup.find_all('div', class_='medium-widget event-widget last'):
        for li in ul.find_all('li'):
            events.append({
                'title': li.find('a').get_text(strip=True),
                'date': li.find('time').get_text(strip=True),
                'link': URL + li.find('a').get('href')
            })
        print(events)
        return events


def save_doc(items, path):
    with open(path, 'w', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(['Мероприятие', 'Дата', 'Ссылка'])
        for item in items:
            writer.writerow([item['title'], item['date'], item['link']])


def parse():
    html = get_html(URL)
    if html.status_code == 200:
        events = []
        for page in range(1,):
            html = get_html(URL)
            events.extend(get_content(html.text))
            save_doc(events, CSV)
    else:
        print('Error')


parse()
