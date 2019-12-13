#main code for cherry blossom
import requests
import time
import json
import os
import urllib
from search import findGenre , findTags
from recc import result
def find():
    user_ani = "Naruto"
    print("")
    user_ani_genre = []
    user_ani_tags = []

    user_ani_genre = findGenre(user_ani)
    user_ani_tags = findTags(user_ani)

    print("Anime title: " + user_ani)
    print("Genres: ")
    for i in range( 0 , len(user_ani_genre)):
        print(user_ani_genre[i])
    print("")
    print("Tags:")
    for i in range( 0 , len(user_ani_tags)):
        print(user_ani_tags[i]['name'] + " " + "Rank: " + str(user_ani_tags[i]['rank']) + "/100")

    print("New Anime Reccomendations Loading:")
    new_rec = (result(user_ani_genre , user_ani_tags, user_ani))

    print("")
    print("Animes similar to " + user_ani +" are:")
    print("")

    for i in range(0 , len(new_rec['tags']['name'])):
        print("Name: " + new_rec['tags']['name'][i] + " Rank: " + str(new_rec['tags']['rank'][i]) +"/100")




find()
