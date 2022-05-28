from . import session


class Anime(object):
    def __init__(self, id):
        self.id = id

    def info(self):
        path = f'https://api.jikan.moe/v4/anime/{self.id}/full'
        response = session.get(path)
        return response.json()