from bs4 import BeautifulSoup # webscraping
import requests # webscraping
import re # regex
import pandas as pd # displaying table
import datetime # dealing with date stuff
import json # read JSON
from tqdm import tqdm # for-loop iteration progress bar


subreddit = "classicwow"

list_filenameold = []
list_filenamenew = []

initutc = 1546300800 # 2019-01-01 in UNIX
finalutc = initutc + 86400 # + 1 day

for i in range(365):
    d = datetime.datetime.fromtimestamp(initutc)
    list_filenameold.append(subreddit+"_"+str(d.date())+".txt")
    list_filenamenew.append(subreddit+"_"+str(d.date())+"_nodupe.txt")
    initutc = finalutc
    finalutc = initutc + 86400

for outfilename,infilename in zip(list_filenamenew,list_filenameold):

    lines_seen = set() # holds lines already seen
    outfile = open("C:/Users/decep/OneDrive/Documents/Reddit Corpora Project/"+subreddit+"_nodupe/"+outfilename, "w", encoding="utf+8")
    for line in open("C:/Users/decep/OneDrive/Documents/Reddit Corpora Project/"+subreddit+"/"+infilename, "r", encoding="utf+8"):
        if line not in lines_seen: # not a duplicate
            outfile.write(line)
            outfile.write('---')
            outfile.write('\n')
            lines_seen.add(line)
    outfile.close()
