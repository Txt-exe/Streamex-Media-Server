import requests
import auth as login
import mediaurls as media_urls
login.keyAuth(True, 'en')


class GetMedia:
    """
Gets all media types that are within the imdb database
        """

    @staticmethod
    def getMovies(category, ):
        """
Gets Movies from TMDB Server and saves them to CSV file
        """
        url = category
        headers = {
            "accept": "application/json",
            "Authorization": "Bearer" + " " + login.api_token
        }
        response = requests.get(url, headers=headers)
        print(response.text)
