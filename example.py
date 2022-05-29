from malwrapper import Anime

#Example to find an anime using the id
anime = Anime(id=45613) #Anime('id') where id is the anime id which can be obtained from myanimelist.net
response = anime.info() # fetching the info function
print(response)

#Example to find an anime using keywords
anime = Anime(name='Naruto')
response = anime.search()
print(response)