import requests
import os
from bs4 import BeautifulSoup
from urllib.request import urlretrieve
from urllib.request import urlopen

def download_image(auction_id, img_link) :
	if not os.path.exists("../auction_images"):
		os.system("mkdir ../auction_images")
		
	file_path = "../auction_images/" + auction_id + ".png"	
	#if os.path.exists(file_path):
	#	return

	urlretrieve(img_link, file_path)
	return file_path

