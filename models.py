import requests
import time
import json
import os
import urllib
from search import findGenre , findTags
from query import * 
def find(user_ani):
    user_ani_genre = []
    user_ani_tags = []

    user_ani_genre = findGenre(user_ani)
    user_ani_tags = findTags(user_ani)

    return[user_ani_genre , user_ani_tags]
