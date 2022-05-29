from . import session


class Anime(object):
    def __init__(self, name=None, id=None):
        self.id = id
        self.name = name

    def info(self):
        path = f'https://api.jikan.moe/v4/anime/{self.id}/full'
        response = session.get(path)
        return response.json()

    def search(self):
        path = f'https://api.jikan.moe/v4/anime?q={self.name}'
        search_result = session.get(path)
        return search_result.json()