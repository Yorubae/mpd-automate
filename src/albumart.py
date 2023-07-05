import os
import subprocess
from config import albumArtpath, mpdArtpath
from src import editor
import requests
import shutil


def moveClient():
    for file in os.listdir(albumArtpath):
        src = os.path.join(albumArtpath, file)
        dst = os.path.join(mpdArtpath, file)
        shutil.copy(src, dst)


def getAlbumArt(path, url):
    filename = path.split("/")[-1]
    if not filename in mpdArtpath:
        buffer = requests.get(url)
        with open(f"{albumArtpath}/{filename}.jpg", "wb") as f:
            f.write(buffer.content)
        moveClient()
