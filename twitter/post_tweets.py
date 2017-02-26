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
		print(image_path)
		api.update_with_media(image_path, status = text.read())
	except Exception as e:
		print("Unexpected error: ",e.message )


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

def post_dummy(api) :
	status = api.update_status("hey everyone")
	print(status)

if __name__ == '__main__':
	auth_instance = Auth("Nr8NWrnIr1huPmlTy3OFfizCl", "94MmEh9HSAGIiolIGSb6hBXXGlFM9weMZNrGjKs6hhJEoNfolr","835036132773605377-ChnMv7F4s7DO6eG1BbKVafgZjYBf1at","jiKWm8tUzXAXuY0ovxc7XWnsbdGj60frsBLUdVIuya7Hr")
	api = auth_instance.authorize()
	#read_timeline(api)
	#fetch_auction_elements(api)
	#post_dummy(api)