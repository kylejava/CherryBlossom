
import requests
import json
import os
import urllib




def findGenre(user_ani):

    query = '''
    query ($id: Int , $search: String) {
      Media (id: $id, search: $search) {
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

    # Define our query variables and values that will be used in the query request
    variables = {
        'search':user_ani
    }

    url = 'https://graphql.anilist.co'

    # Make the HTTP Api request
    response = requests.post(url, json={'query': query, 'variables': variables})
    data = response.json()
    return(data['data']['Media']['genres'])

def findTags(user_ani):
    tags = []
    ani_tags = []
    query = '''
    query ($id: Int , $search: String) { # Define which variables will be used in the query (id)
      Media (id: $id, search: $search) { # Insert our variables into the query arguments (id) (type: ANIME is hard-coded in the query)
        id
        title {

          english

        }
        genres
        tags{
            name
            rank
        }
      }
    }
    '''

    # Define our query variables and values that will be used in the query request
    variables = {
        'search':user_ani
    }

    url = 'https://graphql.anilist.co'

    # Make the HTTP Api request
    response = requests.post(url, json={'query': query, 'variables': variables})
    data = response.json()
    tags = (data['data']['Media']['tags'])

    for i in range(0 , len(tags)):
        if(int(tags[i]['rank']) < 60):
            pass
        else:
            ani_tags.append(tags[i])

    return(ani_tags)
