import os
import sys

import requests
from bs4 import BeautifulSoup

_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../'))
sys.path.append(_ROOT)

from bson import ObjectId
from mongodb.bootstrap import bootstrap_mongo

bootstrap_mongo()

from mongodb.globals import db


def main():
    base_url = "https://www.laidudu.org/book/50073/"

    spec = {
        'href': base_url,
    }
    record = db.Book.find_one(spec)
    if record:
        return

    print('start crawling...')
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36'
    }
    response = requests.get(base_url, headers=headers)
    response.encoding = 'utf-8'

    doc = {
        'href': base_url,
        'title': '万古神帝',
        'raw_content': response.text
    }
    record.update(doc)
    record.save()
    print('end crawling...')


if __name__ == '__main__':
    main()
