from Authentication import Auth
import os
import utils

def winner_tweet_temp(winner_handle, product_url , product_image, product_name) :
	auth_instance = Auth("Nr8NWrnIr1huPmlTy3OFfizCl", "94MmEh9HSAGIiolIGSb6hBXXGlFM9weMZNrGjKs6hhJEoNfolr","835036132773605377-ChnMv7F4s7DO6eG1BbKVafgZjYBf1at","jiKWm8tUzXAXuY0ovxc7XWnsbdGj60frsBLUdVIuya7Hr")
	api = auth_instance.authorize()

	api.update_status("The winner of this auction for "+ product_name + " is : " + winner_handle + "\n Get your product at : "+ product_url + " image " + product_image)



def winner_tweet(api, winner_handle, auction_id,image_url, product_url , product_name) :
	
	image_path = utils.download_image(auction_id, image_url)
	tweet = "The auction for "+ product_name[:50] + " is won by: " + winner_handle + "\n Get your product here : "+ product_url
	api.update_with_media(image_path, status = tweet)
	

if __name__ == '__main__':
		winner_tweet_temp("@sameer2800", "url" ,"image","Tamarind")	