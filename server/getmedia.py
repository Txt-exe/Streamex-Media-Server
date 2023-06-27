import requests
import json
import csv
import os
import server.auth as login


class GetMedia:
    """
Gets all media types that are within the imdb database
        """
    obj  = None    
    page_number = 1
    page_number_string = str(page_number)

    nowplaying_m ='https://api.themoviedb.org/3/movie/now_playing?language=en'+ page_number_string
    mpopular_m = 'https://api.themoviedb.org/3/movie/popular?language=en'+ page_number_string
    toprated_m ='https://api.themoviedb.org/3/movie/top_rated?language=en'+ page_number_string
    upcoming_m = 'https://api.themoviedb.org/3/movie/upcoming?language=en'+ page_number_string

 

    air_today_tv = 'https://api.themoviedb.org/3/tv/airing_today?language=en-US&page=' + page_number_string
    on_air_tv = 'https://api.themoviedb.org/3/tv/on_the_air?language=en'+ page_number_string
    popular_tv ='https://api.themoviedb.org/3/tv/popular?language=en'+ page_number_string
    top_rated_tv ='https://api.themoviedb.org/3/tv/top_rated?language=en'+ page_number_string


    #data bool
    data_is_current = False
    @staticmethod
    def getAllMedia(category, list_to_convert, debug_log = False):
        """
    Gets Media(Movies Or TV) from TMDB Server and saves them to CSV file
        """

        url = category
        headers = {
            "accept": "application/json",
            "Authorization": "Bearer" + " " + login.api_token
        }
        response = requests.get(url, headers=headers)
        
        #Get data and return a json text object
        obj = json.loads(response.text)


        list_to_convert = obj['results'][0]['backdrop_path']


        #prints Data from request in orginzed JSON format
        if debug_log == True:     
            json_formatted_str = json.dumps(obj, indent=4)
            print(obj)                                                                                         
        

    @staticmethod
    def checkCache(check_interval):
        """
    Checks if image files exist along with movie description data 
    on firebase server before calling a request to TMDB server
        """
        

        #if local data is different from current data then call getMovies() 
        #and overwrite current data stored on the server