from tmdbv3api import TMDb

# Keys
api_key = '5ac54eb7818f27002da84c5cf1631b1f'
api_token = 'eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI1YWM1NGViNzgxOGYyNzAwMmRhODRjNWNmMTYzMWIxZiIsInN1YiI6IjY0NzRjMzRhNWNkMTZlMDEzM2UyOWE2YiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.cghB4_ozMf9C_5JMmaIbGzfLqeY-lB1xiNZE11XsZyk'


# Keys

def keyAuth(debug_mode, lang):
    tmdb = TMDb()
    tmdb.api_key = api_key
    tmdb.language = lang
    tmdb.debug = debug_mode
