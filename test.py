
import requests
import json
import os
import urllib
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

genres = [u'Drama', u'Music', u'Romance', u'Slice of Life']
tags = ['Musical' , 'Coming Of Age']
variables = {

    #'type':'ANIME',
    'genre_in': genres,
    'tag_in':tags,
    'page': 1,
    'perPage': 3
}






url = 'https://graphql.anilist.co'

# Make the HTTP Api request
response = requests.post(url, json={'query': query, 'variables': variables})
data = response.json()
for i in range (0 , 2):

    print(data['data']['Page']['media'][i]['title']['english'])
    print("GENRES")
    for g in range (0 , 4):
        print(data['data']['Page']['media'][i]['genres'][g])
    print("TAGS")
    for x in range (0 , 5):
        print(data['data']['Page']['media'][i]['tags'][x])
#print(data)
