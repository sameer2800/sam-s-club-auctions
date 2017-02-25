from Authentication import Auth
import os

#reads timeline of a twitter handle
def read_timeline(api) :
	public_tweets = api.home_timeline()
	for tweet in public_tweets:
		print(tweet.text)


def post_tweet(api, image_file , text_file) :
	image_path = "../auction_images/" + image_file
	text_path = "../auction_details/" + text_file

	
	text= open(text_path,'rb')
	try :
		api.update_with_media(image_path, status = text.read())
	except :
		print("Unexpected error:")


def get_auctiontext_from_image(image) :
	text = image[:-3] + "txt"
	return text

def fetch_auction_elements(api) :
	image_files = os.listdir("../auction_images")

	i =0;
	for image_file in image_files :
		if i == 4 :
			break

		auction_text_file = get_auctiontext_from_image(image_file)
		post_tweet(api, image_file, auction_text_file)
		i += 1

if __name__ == '__main__':
	auth_instance = Auth()
	api = auth_instance.authorize()
	#read_timeline(api)
	fetch_auction_elements(api)
	