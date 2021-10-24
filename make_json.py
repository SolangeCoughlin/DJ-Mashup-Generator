import json

grail_song = {
        "title": "Grail",
        "artist": "Tripp St",
        "bpm": "120",
        "key": "C",
        "danceability": "4"
    }

def make_song_json(song_dict):
    song_json = json.dumps(song_dict)
    with open('grail_song.json', 'w') as outfile:
        outfile.write(song_json)


def main():
    make_song_json(grail_song)

if __name__ == '__main__':
    main()