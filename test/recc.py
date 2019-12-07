
import requests
import json
import os
import urllib
import random

def result(user_ani_genre , user_ani_tags, user_ani ):

    random.shuffle(user_ani_tags)

    random.shuffle(user_ani_genre)
    genres = []
    tags = []
    new_ani = []
    query = '''
    query ($id: Int ,  $genre_in:[String], $tag_in:[String] ) {
        Media (id: $id, genre_in:$genre_in,, tag_in:$tag_in  )  {
            id
            title {
                english

            }

            genres
            tags{
                name
            }
        }

    }
    '''

    for i in range(0 , 2):
        genres.append(user_ani_genre[i])

    for i in range(0 , 3):
        tags.append(user_ani_tags[i]['name'])

    variables = {

        'type':'ANIME',
        'genre_in': genres,
       'tag_in':tags
    }

    url = 'https://graphql.anilist.co'

    # Make the HTTP Api request
    response = requests.post(url, json={'query': query, 'variables': variables})
    data = response.json()
    new_ani.append((data['data']['Media']['title']['english']))
    new_ani.append(genres)
    new_ani.append(tags)
    #new_ani[0] = name
    #new_ani[1] = genres
    #new_ani[2] = tags

    while(new_ani[0] == user_ani or new_ani[0] == None):
        new_ani = result(user_ani_genre , user_ani_tags , user_ani)

    return(new_ani)
