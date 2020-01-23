import requests
import time
import json
import os
import urllib
import random

from query import *


def verify(user_ani):
    variables = {
        'search':user_ani
    }
    response = requests.post(url, json={'query': queryForVerifying, 'variables': variables})
    data = response.json()
    return(data)



def findGenre(user_ani):
    variables = {
        'search':user_ani
    }
    response = requests.post(url, json={'query': queryForFindingGenre, 'variables': variables})
    data = response.json()
    return(data['data']['Media']['genres'])

def findTags(user_ani):
    variables = {
        'search':user_ani
    }
    ani_tags = []
    response = requests.post(url, json={'query': queryForFindingTag, 'variables': variables})
    data = response.json()
    tags = (data['data']['Media']['tags'])

    for i in range(0 , len(tags)):
        if(int(tags[i]['rank']) < 60):
            pass
        else:
            ani_tags.append(tags[i])

    return(ani_tags)


def find(user_ani):
    user_ani_genre = []
    user_ani_tags = []
    new_rec = {}
    user_ani_genre = findGenre(user_ani)
    user_ani_tags = findTags(user_ani)
    new_rec = result(user_ani_genre , user_ani_tags, user_ani)
    return new_rec


def result(user_ani_genre , user_ani_tags, user_ani ):
    random.shuffle(user_ani_tags)
    random.shuffle(user_ani_genre)
    genres = []
    tags = []
    name = []
    rank =[]
    for i in range(0 , 2):
        genres.append(user_ani_genre[i])

    for i in range(0 , 3):
        tags.append(user_ani_tags[i]['name'])
    variables = {

        'type':'ANIME',
        'genre_in': genres,
       'tag_in':tags
    }

    response = requests.post(url, json={'query': queryForFindingNewAnime, 'variables': variables})
    data = response.json()
    print(data)
    new_ani = ((data['data']['Media']['title']['english']))



    while(new_ani == user_ani or new_ani == None):
        new_ani = result(user_ani_genre , user_ani_tags , user_ani)



    for i in range(0 , 3):
        name.append(user_ani_tags[i]['name'])

    for i in range(0 , 3):
        rank.append(str(user_ani_tags[i]['rank']))



    newAni = {
        'name': new_ani,
        'genres': genres,
        'tags': {
            'name': name,
            'rank':rank
        }
    }
    return(newAni)
