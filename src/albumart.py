import os
import subprocess
from config import albumArtpath, mpdArtpath
from src import editor
import requests
import shutil
from rich.progress import Progress


def moveClient() -> None:
    for file in os.listdir(albumArtpath):
        src = os.path.join(albumArtpath, file)
        dst = os.path.join(mpdArtpath, file)
        shutil.copy(src, dst)


def getAlbumArt(path: str, url: str) -> None:
    filename = path.split("/")[-1]
    artsInmpd = os.listdir(mpdArtpath)
    if not filename + ".jpg" in artsInmpd:
        response = requests.get(url, stream=True)
        file_size = int(response.headers.get("Content-Lenght", 0))
        progress = Progress()
        task = progress.add_task("[cyan] Downloading....", total=file_size)
        task_complete = progress.add_task(f"[lime] {filename} downloaded!")
        with progress as p:
            with open(f"{albumArtpath}/{filename}.jpg", "wb") as f:
                for chunk in response.iter_content(chunk_size=1024):
                    p.update(task_id=task, total=file_size)
                    f.write(chunk)
                moveClient()
                p.update(task_complete)
                print("")
    else:
        print(f"{filename.split('.')[0]} already found!")
