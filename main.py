#main code for cherry blossom
import requests
import time
import json
import os
import urllib
from search import findGenre , findTags
from recc import result
def main():
    user_ani = raw_input("Enter Anime title ")
    print("")
    user_ani_genre = []
    user_ani_tags = []

    user_ani_genre = findGenre(user_ani)
    user_ani_tags = findTags(user_ani)


#    for i in range(0 , len(user_ani_tags)):
#        if((user_ani_tags[i]['rank']) < 60):
#            user_ani_tags.pop(i)
#
#        else:
#            pass



    print("Anime title: " + user_ani)
    print("Genres: ")
    for i in range( 0 , len(user_ani_genre)):
        print(user_ani_genre[i])
    print("")
    print("Tags:")
    for i in range( 0 , len(user_ani_tags)):
        print(user_ani_tags[i]['name'] + " " + "Rank: " + str(user_ani_tags[i]['rank']) + "/100")

    print("New Anime Reccomendations Loading:")
    new_rec = result(user_ani_genre , user_ani_tags)

    print("")
    print("Animes similar to " + user_ani +" are:")
    print("")
    while(new_rec == user_ani or new_rec == None):

        new_rec = result(user_ani_genre , user_ani_tags)
    print(new_rec)


main()
