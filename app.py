from flask import Flask, render_template
import os, json

# Configuration
 
app = Flask(__name__)

# Functions

def get_dict_from_json(json_file):
    fjson = open(json_file, 'r')
    song_dict = json.loads(fjson.read())
    return song_dict


# Routes 

@app.route('/')
def root():
    song_dict = get_dict_from_json('grail_song.json')
    song_info_keys = song_dict.keys()
    return render_template('home.html', keys = song_info_keys, data = song_dict)

# Listener

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 9112)) 
    #                                 ^^^^
    #              You can replace this number with any valid port
    
    app.run(port=port, debug=True) 