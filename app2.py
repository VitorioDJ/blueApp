from flask import Flask, render_template, jsonify
import json
import os

app = Flask(__name__)

# Load playlists from JSON file
def load_playlists():
    with open(os.path.join('data', 'playlists.json'), 'r') as f:
        return json.load(f)

@app.route('/player')
def index():
    playlists = load_playlists()
    return render_template('player.html', playlists=playlists)

@app.route('/playlists')
def get_playlists():
    playlists = load_playlists()
    return jsonify(playlists)

if __name__ == '__main__':
    app.run(debug=True)
