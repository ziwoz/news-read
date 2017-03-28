from src.common.database import Database
from src.models.headlines.headlines import Headlines
from src.models.alert.alert import Alert

Database.initialize()

all_news = Alert.get_news_site()
Alert.get_all_headlines(all_news)



