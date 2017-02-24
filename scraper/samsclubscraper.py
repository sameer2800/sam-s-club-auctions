import os
from bs4 import BeautifulSoup
from urllib.request import urlretrieve
from urllib.request import urlopen

# use this image scraper from the location that 
#you want to save scraped images to

def make_soup(url):
	html = urlopen(url).read()
	return BeautifulSoup(html)



#extracts current  bidding amount from auction.
def get_bidding_amnt(auction) :
	curr_bid_amnt = auction.find('span', attrs={'current_bid_amt'})
	#print(curr_bid_amnt.text)	
	return curr_bid_amnt.text


def get_auction_name(auction) :
	#print(auction.find('h5').text)
	return auction.find('h5').text


def get_auction_image_link(auction) :
	link = auction.find('img').get('src')
	#print(link[2:])
	return link[2:]

def download_image(img_link, auction_id) :
	


def get_images2(url):
	soup = make_soup(url)
	#finding  all tags with li having attribute class 'item'
	auction_list = []
	for object in soup.findAll('li', attrs={'class':'item'}) :
		auction_list.append(object)
	
	#print(auction_list)	

	for auction in auction_list :
		auction_id = auction.get('id')
		curr_bid_amnt = get_bidding_amnt(auction)
		auction_name = get_auction_name(auction)
		auction_img_link = get_auction_image_link(auction)
		download_image(auction_img_link, auction_id)


	#x = soup.findall('li',attrs={'id':'auction_*'})
	#images = [img for img in soup.findAll(id = 'auction_3035378')]
	#print(x)
	



def get_images1(url):
	soup = make_soup(url)
	#this makes a list of bs4 element tags
	images = [img for img in soup.findAll('img')]
	print(images)
	print (str(len(images)) + "images found.")
	print('Downloading images to current working directory.')
	#compile our unicode list of image links
	image_links = [each.get('src') for each in images]
	for each in image_links:
		filename=each.split('/')[-1]
		urlretrieve(each, filename)
	return image_links

#a standard call looks like this
#get_images('http://www.wookmark.com')



if __name__ == '__main__':
	get_images2("https://auctions.samsclub.com/auction/endingsoon/new/")