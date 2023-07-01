from youtubesearchpython import VideosSearch
from pytube import YouTube
from config import Path, TempPath
from src.editor import _get_title_
import os

prohibited_chars = ['/']
pathFile = TempPath
def search_videos(query, max_results=10):
    videos_search = VideosSearch(query, limit=max_results)
    results = videos_search.result()['result']

    videos = []
    for result in results:
        videos.append({
            'title': result['title'],
            'video_id': result['id'],
            'url': result['link']
        })

    return videos

def download_song(url, title):
    yt = YouTube(url)
    if prohibited_chars[0] in title:
        trash = title.split('/')
        newTitle = ''
        for i in trash:
            newTitle += i
    else:
        newTitle = title
    audio = yt.streams.filter(only_audio=True).first()
    audio.download(
        output_path=pathFile,
        filename=newTitle,
    )

