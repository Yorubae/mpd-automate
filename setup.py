import subprocess
import os


def isConfig(path):
    for file in os.listdir(path):
        if file == "config.py":
            return True
    return False


cwdpath = os.getcwd()
track_path = os.path.join(cwdpath, "tracks")

path = input("Enter the path of your music directory: ")
cl_id = input("Enter your spotify client id: ")
secret = input("Enter your spotify secret: ")
url = input("Enter the redirect url of your spotify app: ")

if not isConfig(cwdpath) and os.path.exists(track_path):
    with open("config.py", "w") as f:
        f.write(
            f'Path = "{path}"\nclientId = "{cl_id}"\nTempPath = "{track_path}"\nclientSecret = "{secret}"\nredirectUrl = "{url}"'
        )
    print("config file generated!")

print("Installing dependencies....")
subprocess.run("pip", "install", "-r", "requirements.txt")
print("Done installing dependencies!")
