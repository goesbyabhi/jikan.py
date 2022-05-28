import os, requests, json

with open("token.json") as f:
    data = json.load(f)

MAL_API_KEY = data.get("access_token")

class APIKEYMissingError(Exception):
    pass

if MAL_API_KEY is None:
    raise APIKEYMissingError(
        "Needs an API Key. See"
        "https://myanimelist.net/apiconfig/references/authorization"
        "for how to retrive access tokens from"
        "MyAnimeList"
    )

session = requests.Session()
session.params = {}
session.params['api_key'] = MAL_API_KEY
from .anime import Anime