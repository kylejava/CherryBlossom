
import requests
import json
import os
import urllib
import random

def result(user_ani_genre , user_ani_tags ):

    random.shuffle(user_ani_tags)

    random.shuffle(user_ani_genre)
    genres = []
    tags = []

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
    new_ani = data['data']['Media']['title']['english']
    return(new_ani)
