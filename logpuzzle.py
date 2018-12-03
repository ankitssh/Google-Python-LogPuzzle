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
  myFile=open(filename,"r")
  contents=myFile.readlines()
  #print(contents)
  urls=[]
  for s in contents:
      string=s
      pat=r'/edu.*.jpg'
      match = re.search(pat,string)
      if match:
          print("Matched")
         # print(match.group())
          urls.append("http://code.google.com"+match.group())
      else:
          print("Failed")
  myFile.close()
  return urls
  

  

def download_images(img_urls, dest_dir):
    counter=1
    filenames=[]
    for u in img_urls:
        cururl=u
        pat=r'puzzle/.*.jpg'
        match=re.search(pat,cururl)
        filename=match.group()
        filenames.append(filename[7:])
        print((counter/len(img_urls))*100,"%")
        urllib.request.urlretrieve(cururl,dest_dir+filename[7:])
        counter+=1
    return filenames
  

def main():
    myUrls=read_urls("./animal_code.google.com")
    myFileNames=download_images(myUrls,"./downloaded_images/")
    htmlfile=open("./downloaded_images/image.html","w")
    myFileNames.sort()
    htmlfile.write("<html><head><body>")
    for i in myFileNames:
        htmlfile.write("<img src=./"+i+">")
    htmlfile.write("</body></head></html>")
    
    
    

if __name__ == '__main__':
  main()
