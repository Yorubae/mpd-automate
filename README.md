# Mpd-automate

## Introduction

MPD Automate is a Python project designed to automate the process of searching for songs on YouTube, downloading them using the PyTube library, and extracting their metadata using the Spotipy library. This project aims to simplify the task of acquiring songs and their relevant information, making it easier for users to manage their music collection on your mpd client.

The main functionality of MPD Automate revolves around using the `youtube-search-python` module to perform a search query for a specific song. Once the desired song is found, the `PyTube` library is utilized to download the song from YouTube. Finally, the `Spotipy` library is employed to extract the metadata associated with the downloaded song.

By combining these powerful libraries, MPD Automate provides a streamlined solution for music enthusiasts to discover and manage their favorite songs effectively. Whether you want to create playlists, organize your music library, or explore new tracks, MPD Automate offers a comprehensive set of tools to simplify these tasks.

## Features

- Efficiently search for songs using the `youtube-search-python` module.
- Download songs from YouTube using the PyTube library.
- Extract metadata from downloaded songs using the Spotipy library.
- Simplify the process of managing and organizing your music collection.
- Store it on your Music directory to access it through your mpd client effortlessly

## Installation

To use MPD Automate, follow these installation steps:

1. Clone the GitHub repository:
```
git clone https://github.com/Yorubae/mpd-automate.git
```
2. Navigate to the project folder:
```
cd mpd-automate
```
3. Run the setup script
```
python setup.py
```
4. Provide your spotify client id, secret id and redirect url. You can get it done on [spotify](https://developer.spotify.com/dashboard) 

An example of the config file, you can also manually configure this variable tho
```python
Path = ""
TempPath = ""
clientId = ""
clientSecret = ""
redirectUrl = ""
```

## License

MPD Automate is licensed under the [MIT License](https://opensource.org/licenses/MIT).

## Contributing

Contributions to MPD Automate are welcome! If you would like to contribute to this project, please follow the guidelines outlined in the [CONTRIBUTING.md](https://github.com/Yorubae/mpd-automate/blob/main/CONTRIBUTING.md) file.

## Acknowledgments

I would like to express my gratitude to the developers of the youtube-search-python, PyTube, and Spotipy libraries, as MPD Automate relies heavily on their functionality.


