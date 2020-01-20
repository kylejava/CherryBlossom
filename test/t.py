import requests
import json
import os
import urllib

user_ani = "Naruto"

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
if('errors' in y):
    print("there is error")
else:
    print("there is no error")

print(y)
