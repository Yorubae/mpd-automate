import glob
import os
from mutagen.easyid3 import EasyID3
from spotipy.oauth2 import SpotifyOAuth
import spotipy
from config import Path, clientId, redirectUrl, clientSecret

auth = SpotifyOAuth(
    client_id=clientId, client_secret=clientSecret, redirect_uri=redirectUrl
)

client = spotipy.Spotify(auth_manager=auth)


def _get_title_(title: str):
    metaData = client.search(title, limit=1, type="track")
    artist = metaData["tracks"]["items"][0]["artists"][0]["name"]
    track_name = metaData["tracks"]["items"][0]["name"]
    return (track_name, artist)


def _add_metadata(songpath, title, artist):
    try:
        audio = EasyID3(songpath)
        audio["title"] = title
        audio["artist"] = artist
        audio.save()
    except Exception as e:
        print(f"Error in {songpath}", e)


def edit_meta(title=None, album=None, Artist=None, Path=Path):
    if not os.path.exists(Path):
        return
    files = []
    for file in glob.glob(Path + "/*.mp3", recursive=True):
        files.append(file)
        track_title = file.split("/")[-1].split(".")[0]
        trackName, artist = _get_title_(track_title)
        # _add_metadata(file, trackName, artist)

if __name__ == "__main__":
    pass
