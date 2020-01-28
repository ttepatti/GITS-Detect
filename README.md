# GITS-Detect

Ghost In The Shell Facial Detection

## Overview

The point of this project was to be able to take a live video feed and draw the Ghost in the Shell "Laughing Man" image over every detected face. It was done as a fun way to get more familiar with both Python and OpenCV.

For context on the Ghost in the Shell laughing man, I highly recommend watching the source material.

https://www.amazon.com/Ghost-Shell-Complex-Season-Blu-ray/dp/B01NBHMO5B/

Otherwise, you can see the scene here:

https://www.youtube.com/watch?v=mrte6dseXWk

A bit more information:

https://ghostintheshell.fandom.com/wiki/Laughing_Man

## Current Progress

Currently, it can detect faces in still images (provided via command line argument) and draw the laughing man over them. Success!

The current To-Do list is as follows:

* Implement reading frames from a webcam instead of a single still image
* Possibly change the cascade to detect heads, rather than faces? It may be more accurate that way, and could cover someone who is turned around.

## Image Comparison

Below you can find the test image and result image from the current version of GITS-Detect.

![Test Image](https://github.com/ttepatti/GITS-Detect/raw/master/test_images/abba.png)

![Result Image](https://github.com/ttepatti/GITS-Detect/raw/master/result_images/abba_result.jpg)