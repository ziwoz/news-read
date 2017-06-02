
import uuid
from src.common.database import Database
import src.models.headlines.constant as HeadlinesConstants

class Headlines(object):
    def __init__(self, name, link, revision=0, read_status = False, _id = None):
        self.name = name
        self.link = link
        self.read_status = read_status
        self._id = uuid.uuid4().hex if _id is None else _id
        self.revision = revision

    def __repr__(self):
        return "<headline:{}>".format(self.name)

    def json(self):
        return {
            "name": self.name,
            "link": self.link,
            "read_status": self.read_status,
            "_id": self._id,
            "revision": self.revision

        }

    @classmethod
    def get_all(cls):
        return [cls(**elem) for elem in Database.find(HeadlinesConstants.COLLECTION, {})]



    def save_to_mongo(self):
        check_already_exist = Database.find_one(HeadlinesConstants.COLLECTION, {"link": self.link})
        if not check_already_exist:
            Database.insert(HeadlinesConstants.COLLECTION, self.json())

    # find_by_id(headline_id).deactivate()

    @classmethod
    def find_by_id(cls, _id):
        return cls(**Database.find_one(HeadlinesConstants.COLLECTION, {'_id':_id}))

    def delete(self):
        Database.remove(HeadlinesConstants.COLLECTION, {'_id': self._id})

    def update(self):
        Database.update(HeadlinesConstants.COLLECTION, {'_id': self._id}, self.json())

    def deactivate(self):
        # print('reached the headlines.py')
        self.read_status = True
        self.update()


    @staticmethod
    def get_highest_revision():
        try:
            return Database.find_highest_one(HeadlinesConstants.COLLECTION, 'revision')['revision']
        except KeyError:
            return 0



    @classmethod
    def find_all_by_rev(cls, rev):
        return [cls(**elem) for elem in Database.find(HeadlinesConstants.COLLECTION, {'revision': {'$lte':rev}})]

    @staticmethod
    def deactivate_all_by_rev(rev):
        headlines = Headlines.find_all_by_rev(rev)
        for headline in headlines:
            headline.deactivate()






