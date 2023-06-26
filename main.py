from server.auth import keyAuth
from server.getmedia import GetMedia

most_popular_m = []

nowplaying_m = []

toprated_m = []

upcoming_m = []


keyAuth(True, 'en')

#Step 1; Check Cache Server for images
GetMedia.checkCache(5);


for i in GetMedia.movie_data_list:
    GetMedia.getMedia(i, True)
    most_popular_m = GetMedia.movie_index[0]
print(most_popular_m[0])
