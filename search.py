
import requests
import json
import os
import urllib
from query import *

def verifyAnime(user_ani):
    variables = {
        'search':user_ani
    }
    url = 'https://graphql.anilist.co'
    response = requests.post(url, json={'query': queryForVerifying, 'variables': variables})
    data = response.json()
    


def findGenre(user_ani):

    variables = {
        'search':user_ani
    }

    url = 'https://graphql.anilist.co'

    response = requests.post(url, json={'query': queryForFindingGenre, 'variables': variables})
    data = response.json()
    return(data['data']['Media']['genres'])


def findTags(user_ani):
    tags = []
    ani_tags = []

    # Define our query variables and values that will be used in the query request
    variables = {
        'search':user_ani
    }
    url = 'https://graphql.anilist.co'
    # Make the HTTP Api request
    response = requests.post(url, json={'query': queryForFindingTag, 'variables': variables})
    data = response.json()
    tags = (data['data']['Media']['tags'])

    for i in range(0 , len(tags)):
        if(int(tags[i]['rank']) < 60):
            pass
        else:
            ani_tags.append(tags[i])

    return(ani_tags)
