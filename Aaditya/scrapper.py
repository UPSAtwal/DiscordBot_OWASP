#adjusting code from ./Adamay/TwitterScrapper_boi.ipynb to use with the bot

import snscrape.modules.twitter as sntwitter
import pandas as pd

class Scraper:
    def __init__(self):
        pass
    def scrape(self, text, num, likes, ldate, sdate):
        fQuery = fQuery = f"{text} min_faves:{likes} until:{ldate} since:{sdate}"
        data=sntwitter.TwitterSearchScraper(fQuery)
        tweets=[]

        for i,tweet in enumerate(data.get_items()):
            data1=[tweet.url,tweet.user.username,tweet.rawContent]
            tweets.append(data1)
            if i>num:
                break

        fData=pd.DataFrame(tweets,columns='Link Username Content'.split())
        data = {fData.at[i, 'Content']: fData.at[i, 'Link'] for i in range(num)}
        return data