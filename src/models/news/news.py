import uuid
from src.common.database import Database
import src.models.news.constants as NewsConstants

class News(object):
    def __init__(self, name, url, tag_name, query, query2, relative_link=None, _id=None):
        self.name = name
        self.url = url
        self.tag_name = tag_name
        self.query = query
        self.query2 = query2
        self._id = uuid.uuid4().hex if _id is None else _id
        self.relative_link = "None" if relative_link is None else relative_link

    def __repr__(self):
        return "<News {}>".format(self.name)

    def json(self):
        return{
            "_id": self._id,
            "name": self.name,
            "url": self.url,
            "tag_name": self.tag_name,
            "query": self.query,
            "query2": self.query2
        }

    @classmethod
    def get_by_id(cls, id):
        return cls(**Database.find_one(NewsConstants.COLLECTION, {"_id": id}))

    @classmethod
    def get_all(cls):
        return [cls(**elem) for elem in Database.find(NewsConstants.COLLECTION, {})]
