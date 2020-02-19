#!/usr/bin/python3
import os

# grabs the names of the sound effects from their respective file names, e.g. "sound1" from "sound1.wav"
def grabSoundNames():
    
    assert os.path.isdir("./sounds")

    (dirpath, dirnames, filenames) = next(os.walk("./sounds"))

    return filenames