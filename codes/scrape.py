from bs4 import BeautifulSoup # webscraping
import requests # webscraping
import re # regex
import pandas as pd # displaying table
import datetime # dealing with date stuff
import json # read JSON
from tqdm import tqdm # for-loop iteration progress bar

# 1 YEAR DATA

# API ENDPOINT

endpoint = "https://api.pushshift.io/reddit/comment/search/"

# TARGETTED SUBREDDIT

#subreddit = "2007scape"

subreddit_list = ['classicwow','Guildwars2','Eve','fo76','heartstone','BrawlStars','destiny2','deadbydaylight','Rainbow6']

for subreddit in subreddit_list

    # SET INITIAL DATE IN UNIX TIMESTAMP

    initutc = 1546300800 # 2019-01-01
    finalutc = initutc + 600 # + 10 minutes

    # ITERATE FOR 1 YEAR

    for i in tqdm(range(365)): # 365 days in 1 year

    # CONVERT UNIX TO DATE

    d = datetime.datetime.fromtimestamp(initutc)

    # CREATE WRITE FILE

    corpus = open("C:/Users/decep/OneDrive/Documents/Reddit Corpora Project/"+subreddit+"/"+subreddit+"_"+str(d.date())+".txt",'w')

    # COLLECT DATA FOR 1 DAY

    for i in range(144): # 144 * 10 min = 1 day
        query = "?subreddit="+subreddit+"&after="+str(initutc)+"&before="+str(finalutc)+"&size=100"
        url = endpoint+query
        r = requests.get(url)

        # ADD 10 MINUTE INCREMENT FOR NEXT FOR-LOOP

        initutc = finalutc
        finalutc = initutc + 600

        # JUST IN CASE IF SOMETHING IS BORKED

        try:
            result = json.loads(r.text)
        except:
            pass

        # WRITE IN FILE

        for s in result['data']:
        corpus.write(s['body'])
        corpus.write('\n')
        corpus.write('---')
        corpus.write('\n')

    # CLOSE FILE
        
    corpus.close()