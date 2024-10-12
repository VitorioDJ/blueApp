from flask import Flask, render_template, jsonify, redirect
import sys, json, os, time
sys.path.append('./modules')
from functions import update_json_with_tabs

app = Flask(__name__)

# @app.route("/")
# def splash():
#     return render_template('splash.html')
#     time.sleep(3)
#     return redirect("/main")
                                           
@app.route("/")
def blueApp():
    with open('./data/artists.json', 'r') as f1:
        ARTISTS = json.load(f1)
    
    with open('./data/playlist.json', 'r') as f2:
        PLAYLIST = json.load(f2)

    with open('./data/meditations.json', 'r') as f3:
        MEDITATIONS = json.load(f3)

    with open('./data/videos.json', 'r') as f4:
        VIDEOS = json.load(f4)

    return render_template('blue.html',
                            artists=ARTISTS,
                            playlist=PLAYLIST,
                            meditations=MEDITATIONS,
                            videos=VIDEOS
                            )


if __name__ == "__main__": 
    app.run(host='0.0.0.0', debug=True)