# GITS-Detect

Ghost In The Shell Facial Detection

![Test Image](https://github.com/ttepatti/GITS-Detect/raw/master/test_images/abba.png)

Test Image

![Result Image](https://github.com/ttepatti/GITS-Detect/raw/master/result_images/abba_result.jpg)

Result Image

## Overview

The point of this project was to be able to take a live video feed and draw the Ghost in the Shell "Laughing Man" image over every detected face. It was done as a fun way to get more familiar with both Python and OpenCV.

## Current Progress

Currently, it can detect faces in still images (provided via command line argument) and draw the laughing man over them. Success!

The current To-Do list is as follows:

* Implement reading frames from a webcam instead of a single still image
* Increase GITS image size by 20-30% to cover the individual's entire head
* Possibly chance cascade to detect heads, rather than faces? It may be more accurate that way, and could cover someone who is turned around.