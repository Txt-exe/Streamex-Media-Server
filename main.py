from server.auth import keyAuth
from server.getmedia import GetMedia

most_popular_m = {}

nowplaying_m = []

toprated_m = []

upcoming_m = []


keyAuth(True, 'en')

#Step 1; Check Cache Server for images
GetMedia.checkCache(5);
