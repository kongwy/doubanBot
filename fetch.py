import json
from urllib.request import urlopen
from urllib.parse import quote

def getBook(kw):
    response = urlopen('https://api.douban.com/v2/book/search?count=5&q=' + quote(kw)).read().decode('utf-8')
    responseJson = json.loads(response)
    return responseJson['books']

def getMovie(kw):
    response = urlopen('https://api.douban.com/v2/movie/search?count=5&q=' + quote(kw)).read().decode('utf-8')
    responseJson = json.loads(response)
    return responseJson['subjects']

def inTheater():
    response = urlopen('http://api.douban.com/v2/movie/in_theaters').read().decode('utf-8')
    responseJson = json.loads(response)
    return responseJson['subjects']