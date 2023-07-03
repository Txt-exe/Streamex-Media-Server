from server.auth import keyAuth
from server.getmedia import GetMedia
from flask import Flask
most_popular_m = []

nowplaying_m = []

toprated_m = []

upcoming_m = []

json_response = {}

app = Flask(__name__)

#MOVIES
@app.route("/nowplaying_m")
def nowPlaying():

    keyAuth(True, 'en')
    return GetMedia.getAllMedia(GetMedia.nowplaying_m)

@app.route("/mpopular_m")
def mostPopular():

    keyAuth(True, 'en')
    return GetMedia.getAllMedia(GetMedia.mpopular_m)


@app.route("/toprated_m")
def topRated():

    keyAuth(True, 'en')
    return GetMedia.getAllMedia(GetMedia.toprated_m)

@app.route("/upcoming_m")
def upComing():

    keyAuth(True, 'en')
    return GetMedia.getAllMedia(GetMedia.upcoming_m)


#TV SHOWS
@app.route("/air_today_tv")
def onAirToday():

    keyAuth(True, 'en')
    return GetMedia.getAllMedia(GetMedia.air_today_tv)

@app.route("/on_air_tv")
def onAirGeneral():

    keyAuth(True, 'en')
    return GetMedia.getAllMedia(GetMedia.on_air_tv)


@app.route("/popular_tv")
def popularTv():

    keyAuth(True, 'en')
    return GetMedia.getAllMedia(GetMedia.popular_tv)

@app.route("/top_rated_tv")
def topRAtedTv():

    keyAuth(True, 'en')
    return GetMedia.getAllMedia(GetMedia.top_rated_tv)



#print(json_response['results'][0]['backdrop_path'])

