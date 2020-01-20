
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
    name = []
    rank =[]
    query = '''
    query ($id: Int ,  $genre_in:[String] ) {
        Media (id: $id, genre_in:$genre_in )  {
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
        'genre_in': genres

    }

    url = 'https://graphql.anilist.co'

    # Make the HTTP Api request
    response = requests.post(url, json={'query': query, 'variables': variables})
    data = response.json()
    new_ani = ((data['data']['Media']['title']['english']))

    print(new_ani)
    for i in range(0 , 3):
        name.append(user_ani_tags[i]['name'])

    for i in range(0 , 3):
        rank.append(str(user_ani_tags[i]['rank']))

    #new_ani[0] = name
    #new_ani[1] = genres
    #new_ani[2] = tags

    while(new_ani== user_ani or new_ani == None):
        new_ani = result(user_ani_genre , user_ani_tags , user_ani)



    mydict = {
        'name': new_ani,
        'genres': genres,
        'tags': {
            'name': name,
            'rank':rank
        }
    }
    return(mydict)
