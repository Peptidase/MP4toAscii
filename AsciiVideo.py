#!/usr/bin/env python3

from contextlib import closing
from videosequence import VideoSequence
from AsciConversion import main
import time
import os
video = input("Please enter a video file path: \n")

with closing(VideoSequence(video)) as frames:
    for i in range(len(frames)):
        os.system('clear')
        main(input_image=frames[i])
        time.sleep(0.1)
