

import requests
from bs4 import BeautifulSoup
from src.common.database import Database
from src.models.news.news import News
from src.models.headlines.headlines import Headlines

Database.initialize()


class Alert(object):

    @staticmethod
    def load_news(url, tag_name, query, query2, relave_link, revision):
        request = requests.get(url)
        content = request.content
        soup = BeautifulSoup(content, "html.parser")
        element = soup.find(tag_name, query)
        each_elem = element.find_all(query2)
        for elem in each_elem:
            verify = elem.find('a')
            if verify:
                href = elem.find('a').get("href")
                # if not url in href:
                if not 'http' in href:
                    href = relave_link+href
                headline = elem.text.strip()
                Headlines(headline, href, revision).save_to_mongo()

    @staticmethod
    def get_news_site():
        return News.get_all()

    @staticmethod
    def get_all_headlines(all_news, revision):
        for elem in all_news:
            Alert.load_news(url=elem.url, tag_name=elem.tag_name, query=elem.query, query2=elem.query2, relave_link=elem.relative_link, revision=revision)


