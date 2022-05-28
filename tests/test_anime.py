from pytest import fixture
from malwrapper import Anime
import vcr

@fixture
def anime_keys():
    """Responsible for returning the test data"""
    return ['data']

@vcr.use_cassette('tests/vcr_cassettes/anime-info.yml')

def test_anime(anime_keys):
    """Tests an API call to get an Anime's info"""

    anime_instance = Anime(50265)
    response = anime_instance.info()
    print(response)

    assert isinstance(response, dict)
    assert response['data']['mal_id'] == 50265, "The mal_id should be in the response"
    assert set(anime_keys).issubset(response.keys()), "All keys should be in the response"