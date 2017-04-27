from src.common.database import Database
from src.models.headlines.headlines import Headlines
from src.models.alert.alert import Alert
import src.models.headlines.constant as HeadlinesConstants

Database.initialize()

# find the last headlines revision number and increase it by one
try:
    # the try except is for the fist time when the DB dont have any revision value
    last_rev = Headlines.get_highest_revision()
except TypeError:
    last_rev = 0
rev = last_rev+1


all_news = Alert.get_news_site()
Alert.get_all_headlines(all_news, rev)
# HeadlinesConstants.revision = 12

# print(last_revision['revision'])


