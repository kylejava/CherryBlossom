#main code for cherry blossom
import requests
import json
import os
import urllib
from search import findGenre , findTags

def main():
    user_ani = input("Enter Anime title ")
    print()
    user_ani_genre = []
    user_ani_tags = []

    user_ani_genre = findGenre(user_ani)
    user_ani_tags = findTags(user_ani)

    print("Anime title: " + user_ani)
    print("Genres: ")
    for i in range( 0 , len(user_ani_genre)):
        print(user_ani_genre[i])
    print()
    print("Tags:")
    for i in range( 0 , len(user_ani_tags)):
        print(user_ani_tags[i]['name'] + " " + "Rank: " + str(user_ani_tags[i]['rank']) + "/100")









main()
