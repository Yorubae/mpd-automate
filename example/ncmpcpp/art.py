import os
import subprocess

title, artist = (
    subprocess.check_output(["mpc -f '%title% \n%artist%'"], shell=True)
    .decode("utf-8")
    .splitlines()[0:2]
)


def genNotifs(artpath):
    subprocess.run(
        [
            f'dunstify --replace=27072 -i "{artpath}" \'Playing...\' "{artist} \n{title}"',
        ],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        shell=True,
    )


def getart(path):
    cp_track = (
        subprocess.check_output(["mpc -f %file%"], shell=True)
        .decode("utf-8")
        .splitlines()[0]
        .split(".")[:-1]
    )
    if os.path.isdir(path):
        for jpg in os.listdir(path):
            isJpg = jpg.split(".")[:-1]
            # print(isJpg , cp_track)
            if isJpg[0] in cp_track[0]:
                return os.path.join(path, jpg)
    else:
        print("Invalid path")


def main():
    artpath = getart("/home/Yoru/.config/ncmpcpp/albumarts/")
    defaultArt = "/home/Yoru/Pictures/pins/emo-girl.jpg"
    genNotifs(artpath) if artpath else genNotifs(defaultArt)


if __name__ == "__main__":
    main()
