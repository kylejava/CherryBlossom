
import requests
import json
import os
import urllib


def result(user_ani_genre , user_ani_tags):
    genres = []
    tags = []
    new_ani = []
    query = '''
    query ($id: Int, $page: Int, $perPage: Int , $genre_in:[String] , $tag_in:[String]) {
        Page (page: $page, perPage: $perPage) {
            pageInfo {
                total
                currentPage
                lastPage
                hasNextPage
                perPage
            }
            media (id: $id, genre_in:$genre_in , tag_in:$tag_in )  {
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
    }
    '''
    for i in range(0 , 2):
        genres.append(user_ani_genre[i])
    for i in range(0 , 3):
        tags.append(user_ani_tags[i]['name'])

    variables = {

        'type':'ANIME',
        'genre_in': genres,
        'tag_in':tags,
        'page': 1,
        'perPage': 3
    }

    url = 'https://graphql.anilist.co'

    # Make the HTTP Api request
    response = requests.post(url, json={'query': query, 'variables': variables})
    data = response.json()

    for i in range(0 , 2):
        if(data['data']['Page']['media'][i]['title']['english'] == None):
            break
        else:
            new_ani.append(data['data']['Page']['media'][i]['title']['english'])
    return(new_ani)
