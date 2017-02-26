# sam-s-club-auctions
Members of sam's club can bid on a product listed in auctions site . The following automated scripts makes users work painless. All they need is a twitter account and guts to reply with their bid value on tweets posted by sam's club . Doesn't this sounds awesome ? 

![Alt text](/utils/image1.png?raw=true "Image 1")
 

## Scraper
The scraper is written in python language.It scrapes the auctions from sam's club new auctions page. we can restrict number of auction pages to be scraped. As soon as scraping is completed , auctions images are stored in auction_images sub repo with auction_id as a file name , similarly auction details such as item name, auction end time , current bid value are stored in auction_details sub repo.

## Twitter
The script reads all the auction images and its details from the corresponding auctions_images and auctions_details folders and posts it in sam's club twitter page.

##Installation
python3 samsclubscraper.py
python3 ../twitter/post_tweets.py




###dependencies
[beautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)

[Urllib](https://docs.python.org/2/library/urllib.html)

[Tweepy](http://tweepy.readthedocs.io/en/v3.5.0/api.html)



