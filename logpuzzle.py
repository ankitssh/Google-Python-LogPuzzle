#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import os
import re
import sys
import urllib.request

"""Logpuzzle exercise
Given an apache logfile, find the puzzle urls and download the images.

Here's what a puzzle url looks like:
10.254.254.28 - - [06/Aug/2007:00:13:48 -0700] "GET /~foo/puzzle-bar-aaab.jpg HTTP/1.0" 302 528 "-" "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.6) Gecko/20070725 Firefox/2.0.0.6"
"""


def read_urls(filename):
  myFile=open(filename,"r") ##opening the provided file in read mode
  contents=myFile.readlines() ## saving the contents of the file in a list called contents
  #print(contents)
  urls=[] ##creating a empty list that'll haev all the complete urls
  for s in contents: ##Now iterate the contents list
      string=s ## current string is saved in a variable string
      pat=r'/edu.*.jpg' ##The pattern to match the image
      match = re.search(pat,string) ##matching with regex
      if match: ##If image exists in current string
          print("Matched")
         # print(match.group())
          urls.append("http://code.google.com"+match.group()) ##insert in urls list the complete url obtained from current string
      else:
          print("Failed") ##else do nothing
  myFile.close() ##close the file to transfer the data from buffer to file
  return urls ##return the urls list so as we can pass this to other function
  

  

def download_images(img_urls, dest_dir):
    counter=1 ## counter to show progress
    filenames=[] ## here we save filenames in this list
    for u in img_urls: ##iterate over image urls strings
        cururl=u
        pat=r'puzzle/.*.jpg'
        match=re.search(pat,cururl)
        filename=match.group()
        filenames.append(filename[7:]) #Getting filename to use it for writing 
        print((counter/len(img_urls))*100,"%") ##showing progress
        urllib.request.urlretrieve(cururl,dest_dir+filename[7:]) ##downloading file and saving it in folder. The downloaded file is saved by name extraced above
        counter+=1
    return filenames ## return the list of file names
  

def main():
    myUrls=read_urls("./animal_code.google.com") ##Passing the log file name. This function returns a list of complete urls+
    myFileNames=download_images(myUrls,"./downloaded_images/") ## Passing the above url list and folder name
    htmlfile=open("./downloaded_images/image.html","w") ##open manually created html file
    myFileNames.sort() ##Sort the list of file names
    htmlfile.write("<html><head><body>") #write the contents of html
    for i in myFileNames:
        htmlfile.write("<img src=./"+i+">") ##this file is in same directory as downloaded images so ./filname works for src
    htmlfile.write("</body></head></html>") ##closing tags
    
    
    

if __name__ == '__main__':
  main()
