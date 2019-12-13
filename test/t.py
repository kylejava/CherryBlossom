import requests
import json
import os
import urllib

user_ani = "Your Lie in April"

url = 'https://graphql.anilist.co'

queryForVerifying = '''
query ($id: Int , $search: String) {
  Media (id: $id, search: $search) {
    id
    title {
      english
    }
  }
}
'''
def verify(user_ani):
    variables = {
        'search':user_ani
    }
    response = requests.post(url, json={'query': queryForVerifying, 'variables': variables})
    data = response.json()
    return(data)

y= verify(user_ani)
print(y)
