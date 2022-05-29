from urllib import response
from malwrapper import Anime

anime = Anime(45613) #Anime('id) where id is the anime id which can be obtained from myanimelist.net
response = anime.info() # fetching the info function
print(response)