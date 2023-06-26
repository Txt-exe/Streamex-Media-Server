import requests
import json
import csv
import os
import server.auth as login


class GetMedia:
    """
Gets all media types that are within the imdb database
        """

    data_response = ''
    page_number = 1
    page_number_string = str(page_number)
    nowplaying_m ='https://api.themoviedb.org/3/movie/now_playing?language=en'
    mpopular_m = 'https://api.themoviedb.org/3/movie/popular?language=en'
    toprated_m ='https://api.themoviedb.org/3/movie/top_rated?language=en'
    upcoming_m = 'https://api.themoviedb.org/3/movie/upcoming?language=en'

 

    air_today_tv = 'https://api.themoviedb.org/3/tv/airing_today?language=en-US&page=' + page_number_string
    on_air_tv = 'https://api.themoviedb.org/3/tv/on_the_air?language=en'
    popular_tv ='https://api.themoviedb.org/3/tv/popular?language=en'
    top_rated_tv ='https://api.themoviedb.org/3/tv/top_rated?language=en'


    #data bool
    data_is_current = False
    @staticmethod
    def getAllMedia(category, debug_log = False):
        """
    Gets Media(Movies Or TV) from TMDB Server and saves them to CSV file
        """
        url = category
        headers = {
            "accept": "application/json",
            "Authorization": "Bearer" + " " + login.api_token
        }
        response = requests.get(url, headers=headers)
        #Adding separate var for response Text for easy modifying
        data_response = response.text
        if debug_log == True:
            obj = json.loads(data_response)
            json_formatted_str = json.dumps(obj, indent=4)
            print(json_formatted_str)
        

    @staticmethod
    def checkCache(check_interval):
        """
    Checks if image files exist along with movie description data 
    on firebase server before calling a request to TMDB server
        """
        

        #if local data is different from current data then call getMovies() 
        #and overwrite current data stored on the server