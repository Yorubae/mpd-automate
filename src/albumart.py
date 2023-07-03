import os
import subprocess
from config import Path, albumArtpath, mpdArtpath
from src import editor
import requests
import shutil

def moveClient():
    for file in os.listdir(albumArtpath):
        src = os.path.join(albumArtpath, file)
        dst = os.path.join(mpdArtpath, file)
        if file not in os.listdir(mpdArtpath):
            shutil.copy(src, dst)

def getAlbumArt():
    for file in os.listdir(Path):
        filename = file.split('.')[:-1][0]
        url = editor._get_title_(filename)[-1]
        for art in os.listdir(albumArtpath):
            if not filename in art:
                buffer = requests.get(url)
                with open(f'{albumArtpath}/{filename}.jpg', 'wb') as f:
                    f.write(buffer.content)
                moveClient()
