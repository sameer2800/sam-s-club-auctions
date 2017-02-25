import os
from bs4 import BeautifulSoup
from urllib.request import urlretrieve
from urllib.request import urlopen


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
	#print(link[2:-8])
	return "http://" + link[2:-8] + "300x300$"


def get_auction_end_time(auction) :
	end_time  = auction.find('span',attrs={'class':'countdown'}).get('data-end-time')
	#print(end_time[:-9])
	return end_time[:-9]

def download_image(img_link, auction_id) :
	if not os.path.exists("../auction_images"):
		os.system("mkdir ../auction_images")

	file_path = "../auction_images/" + auction_id + ".png"	

	#if os.path.exists(file_path):
	#	return

	urlretrieve(img_link, file_path)	


def save_auction_details(auction_id, curr_bid_amnt, auction_name ,auction_end_time):
	if not os.path.exists("../auction_details"):
		os.system("mkdir ../auction_details")

	file_path = "../auction_details/" + auction_id + ".txt"	

	#if os.path.exists(file_path):
	#	return

	with open(file_path, "w") as text_file:
		text_file.write("Product : " + auction_name + "\n Current Bidding Price : " + curr_bid_amnt + "\n Auction Ends in : " + auction_end_time)



def scraper(url):
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
		auction_end_time = get_auction_end_time(auction)
		download_image(auction_img_link, auction_id)
		save_auction_details(auction_id, curr_bid_amnt, auction_name ,auction_end_time)


if __name__ == '__main__':
	scraper("https://auctions.samsclub.com/auction/endingsoon/new/?p=1#toolbar")
	scraper("https://auctions.samsclub.com/auction/endingsoon/new/?p=2#toolbar")



