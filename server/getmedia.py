import requests
import requests
import server.auth as login


class GetMedia:
    """
Gets all media types that are within the imdb database
        """

    movie_data_list = [

    #nowplaying_m 
    'https://api.themoviedb.org/3/movie/now_playing?language=en',
    #mpopular_m
    'https://api.themoviedb.org/3/movie/popular?language=en',
    #toprated_m
    'https://api.themoviedb.org/3/movie/top_rated?language=en',
    #upcoming_m
    'https://api.themoviedb.org/3/movie/upcoming?language=en']

    tv_data_list = [

    #air_today_tv 
    'https://api.themoviedb.org/3/tv/airing_today?language=en-US&page=1',
    #on_air_tv
    'https://api.themoviedb.org/3/tv/on_the_air?language=en-US&page=1',
    #popular_tv
    'https://api.themoviedb.org/3/tv/popular?language=en-US&page=1',
    #top_rated_tv
    'https://api.themoviedb.org/3/tv/top_rated?language=en-US&page=1'
    ]

    movie_index = []

    #data bool
    data_is_current = False
    @staticmethod
    def getMedia(category, debug_log = False):
        """
    Gets Media(Movies Or TV) from TMDB Server and saves them to CSV file
        """
        url = category
        headers = {
            "accept": "application/json",
            "Authorization": "Bearer" + " " + login.api_token
        }
        response = requests.get(url, headers=headers)
       
        if debug_log == True:

            pass
            GetMedia.movie_index.append(response.text)

        

    @staticmethod
    def checkCache(check_interval):
        """
    Checks if image files exist along with movie description data 
    on firebase server before calling a request to TMDB server
        """
        

        #if local data is different from current data then call getMovies() 
        #and overwrite current data stored on the server