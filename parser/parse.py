import requests
from datetime import datetime
from dotenv import load_dotenv
import os
from config import timezone
import re

load_dotenv('../config/.env')

url: str = os.getenv('URL')
word: str = os.getenv('WORD')
pattern: str = os.getenv('PATTERN')


def get_data():
    def unit_to_utc(unix):
        ts = unix / 1000
        utc = datetime.fromtimestamp(ts, timezone.TIMEZONE)
        return utc.strftime("%d.%m.%Y %H:%M:%S")

    articles = requests.get(url).json()['data']['catalogs'][0]['articles'][12]
    data = {'title': articles['title'], 'date': unit_to_utc(articles['releaseDate'])}

    if word in data['title']:
        with open('exclude.txt', 'a+') as f:
            exceptions = f.readlines()
            if data['date'] in exceptions:
                return "Nothing new, monitoring continues."
            else:
                f.write(data['date'] + "\n")
                token = re.search(pattern, data['title']).group(1)
                return f"{word} ({token})\n{data['date']} in {timezone.TIMEZONE}"
    else:
        return "Nothing new, monitoring continues."
