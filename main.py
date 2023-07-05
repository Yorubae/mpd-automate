from src.editor import _add_metadata, _get_title_
from src.downloadtrack import search_videos
from src.downloadtrack import download_song
import os, sys
from config import Path, TempPath
import shutil
from pydub import AudioSegment
from src import albumart


def _moveTomusic_():
    for file in os.listdir(TempPath):
        srcpath = os.path.join(TempPath, file)
        dstpath = os.path.join(Path, file)
        with open(srcpath, "rb") as f:
            audio = AudioSegment.from_file(f)
        audio.export(dstpath + ".mp3", format="mp3")
        print("Cleaning up the mess, ehheh")
        os.remove(srcpath)


def check_aud_exists(title):
    for file in os.listdir(Path):
        if title.lower() in file.lower():
            return True


def event(option):
    if option == 1:
        query = input("Name of the Track: ")
        results = search_videos(query)
        for index, result in enumerate(results, 1):
            print(str(index) + ".", result["title"])

        choice = int(input("Option: ")) - 1
        title = results[choice]["title"]
        url = results[choice]["url"]
        if check_aud_exists(title):
            print("Song already exists!")
            return

        print("Getting the song from the Youtube servers...")
        download_song(url, title)
        print(f'{results[choice]["title"]} Successfully Downloaded')
        if os.listdir(TempPath):
            print(
                "Performing audio coversion....This might take a few secs. Hold tight!"
            )
            _moveTomusic_()
            print("Audio conversion done!")
            print("Getting it's metadata from spotify servers....")
            spotitle, artist, url = _get_title_(title)
            _add_metadata(os.path.join(Path, title + ".mp3"), spotitle, artist)
            print("Song added to library")
    elif option == 2:
        print("Fetching metadata from spotify servers")
        for file in os.listdir(Path):
            filename = file.split(".")[:-1][0]
            title, artist, artUrl = _get_title_(filename)
            _add_metadata(f"{os.path.join(Path,file)}", title, artist)
            albumart.getAlbumArt(os.path.join(Path, file), artUrl)

        print("Updated library")
    elif option == 99:
        print("Exiting!")
        sys.exit(0)
    else:
        print("Invalid option")


def main():
    print("1) Download a track")
    print("2) Generate metadata for tracks")
    print("99) Exit")
    while True:
        choice = int(input("Option > "))
        event(choice)


if __name__ == "__main__":
    main()
