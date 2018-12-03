# Google-Python-LogPuzzle

This is the solution to Google's python <a href="https://developers.google.com/edu/python/exercises/log-puzzle">logpuzzle</a> part A and B. The exercise requires you to use python to download image-slices from Apache-server's log files.

* Python version used: 3.7
* IDE used: Spyder
* Modules used: urllib, re, sys, os


### Working ###
1. The function **read_urls** takes the logfile name as the parameter
2. We read the contents of the log file and save them into an array
3. We use regex to extract the image urls and concatenate the urls with the server name. The complete urls are now saved one-by-one into an array **urls**
4. The **read_urls** function returns the array of urls
5. The **download_images** function takes the array of urls and the destination folder as parameters. The destination folder is the directory where the images will be stored when downloaded
6. We download the images one-by-one using **urllib.request.urlretrieve**. The naming of the files are done by name extracted using regex
7. At the end, we write a html file and append the images into it by using html img tag.
