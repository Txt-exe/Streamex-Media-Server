from server.auth import keyAuth
from server.getmedia import GetMedia
from flask import Flask
most_popular_m = []

nowplaying_m = []

toprated_m = []

upcoming_m = []

json_response = {}

app = Flask(__name__)

@app.route("/")
def getdata():

    keyAuth(True, 'en')
    GetMedia.getAllMedia(GetMedia.nowplaying_m)


#print(json_response['results'][0]['backdrop_path'])

