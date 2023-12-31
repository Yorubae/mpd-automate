import subprocess
import os

def isConfig(path):
    for file in os.listdir(path):
        if file == "config.py":
            return True
    return False


cwdpath = os.getcwd()
track_path = os.path.join(cwdpath, "tracks")
albumArtpath = os.path.join(cwdpath, 'art')

if not isConfig(cwdpath):
    path = input("Enter the path of your music directory: ")
    cl_id = input("Enter your spotify client id: ")
    secret = input("Enter your spotify secret: ")
    url = input("Enter the redirect url of your spotify app: ")
    mpdArtpath = input('Enter the path of your mpd client album art: ') 

    if not (
        os.path.exists(track_path) and not
        os.path.exists(os.path.join(cwdpath, 'art'))
    ):
        os.mkdir(os.path.join(cwdpath, 'tracks'))
        os.mkdir(os.path.join(cwdpath, 'art'))

    with open("config.py", "w") as f:
        f.write(
            f'Path = "{path}"\nclientId = "{cl_id}"\nTempPath = "{track_path}"\nclientSecret = "{secret}"\nredirectUrl = "{url}"\nmpdArtpath = "{mpdArtpath}"\nalbumArtpath = "{albumArtpath}"')
    print("config file generated!")

print("Installing dependencies....")
subprocess.run(["pip", "install", "-r", "requirements.txt"])
print("Done installing dependencies!")
