from flask import Flask, render_template, jsonify
import sys, json, os
sys.path.append('./modules')
from functions import update_json_with_tabs

app = Flask(__name__)
# Load playlists from JSON file
def load_playlists():
    with open(os.path.join('data', 'playlists.json'), 'r') as f0:
        return json.load(f0)

@app.route("/")
def splash():
    return render_template('splash.html')
                                           
@app.route("/main")
def blueApp():
    with open('./data/artists.json', 'r') as f1:
        ARTISTS = json.load(f1)
    
    with open('./data/tabs.json', 'r') as f2:
        TABS = json.load(f2)

    with open('./data/art.json', 'r') as f3:
        ART = json.load(f3)

    return render_template('blue.html',
                            tabs=TABS,
                            art=ART,
                            artists=ARTISTS
                            )

@app.route("/temp")
def jovCareer():

    with open('./data/tabs.json', 'r') as f1:
        TABS = json.load(f1)

    with open('./data/art.json', 'r') as f3:
        ART = json.load(f3)

    return render_template('home.html', 
                            tabs=TABS,
                            art=ART,
                            company_name='Jovian33'
                            )


@app.route("/api/update-tabs")
def update_tabs():
    try:
        update_json_with_tabs('./data/tabs-start.json', './data/tabs.json')
        return jsonify({'message': 'Tabs updated successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == "__main__": 
    app.run(host='0.0.0.0', debug=True)