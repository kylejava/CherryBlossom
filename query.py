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


queryForFindingGenre = '''
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

queryForFindingTag = '''
query ($id: Int , $search: String) {
  Media (id: $id, search: $search) {
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

queryForFindingNewAnime = '''
query ($id: Int ,  $genre_in:[String], $tag_in:[String] ) {
    Media (id: $id, genre_in:$genre_in,, tag_in:$tag_in  )  {
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

url = 'https://graphql.anilist.co'
