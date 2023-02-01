#adjusting code from ./Adamay/TwitterScrapper_boi.ipynb to use with the bot

import snscrape.modules.twitter as sntwitter
import pandas as pd

class Scraper:
    def __init__(self):
        pass
    def scrape(self, text):
        fQuery=text+' min_faves:4000'
        data=sntwitter.TwitterSearchScraper(fQuery)
        tweets=[]

        for i,tweet in enumerate(data.get_items()):
            data1=[tweet.url,tweet.user.username,tweet.rawContent]
            tweets.append(data1)
            if i>50:
                break

        fData=pd.DataFrame(tweets,columns='Link Username Content'.split())
        csvFile=text+'.csv'
        fData.to_csv(csvFile,index=False)
        return csvFile
