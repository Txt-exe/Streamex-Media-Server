from server.auth import keyAuth
from server.getmedia import GetMedia

keyAuth(True, 'en')

#Step 1; Check Cache Server for images
GetMedia.checkCache(5);


for i in GetMedia.movie_data_list:
    GetMedia.getMovies(i)
    print("Everything works")

