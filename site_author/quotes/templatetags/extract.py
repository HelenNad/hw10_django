from django import template

from ..utils import get_mongodb
from bson.objectid import ObjectId
register = template.Library()


def get_author(id_):
    db = get_mongodb()
    author = db.authors.find_one({'_id': ObjectId(id_)})
    return author['fullname']


register.filter('get_author', get_author)


def link_author(id_):
    db = get_mongodb()
    author = db.authors.find_one({'_id': ObjectId(id_)})
    c = str(author['fullname']).replace(" ", "-").replace("'", "").replace("é", "e").replace(".", "-").replace("--", "-")
    if c.endswith("-"):
        x = c.rfind("-")
        y = c[:x]
        return y
    return c


register.filter('author_link', link_author)


def born_author(id_):
    db = get_mongodb()
    author = db.authors.find_one({'_id': ObjectId(id_)})
    return author['born_date']


register.filter('born_date', born_author)
