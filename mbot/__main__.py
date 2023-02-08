from os import mkdir, path

from mbot import Mbot

if __name__ == "__main__":
    if not path.exists("cache"):
        mkdir("cache")
    Mbot().run()
