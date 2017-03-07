import os
import utils
from Authentication import Auth

def create_tweet(api,auction_id, product_name , image_url, cur_bidding_price , auction_end_time):	

	image_path = utils.download_image(auction_id, image_url)
	tweet = "Product: " + product_name[:50] + "\nStarting Bidding Price : " + cur_bidding_price + "\nAuction Ends in: " + auction_end_time + "\n#" + auction_id
	status =	api.update_with_media(image_path, status = tweet)	
	print(status.id) 
	return status.id

def create_tweet1(auction_id, product_name , image_url, cur_bidding_price , auction_end_time):	
	auth_instance = Auth("Nr8NWrnIr1huPmlTy3OFfizCl", "94MmEh9HSAGIiolIGSb6hBXXGlFM9weMZNrGjKs6hhJEoNfolr","835036132773605377-ChnMv7F4s7DO6eG1BbKVafgZjYBf1at","jiKWm8tUzXAXuY0ovxc7XWnsbdGj60frsBLUdVIuya7Hr")
	api = auth_instance.authorize()	
	image_path = utils.download_image(auction_id, image_url)
	weet = "Product: " + product_name[:50] + "\nCurr Bidding Price : " + cur_bidding_price + "\nAuction Ends in: " + auction_end_time + "\n#" + auction_id
	status =	api.update_with_media(image_path, status = tweet)	
	print(status.id) 
	return status.id



if __name__ == '__main__':
		create_tweet1("auct_1235456","Gym Bread","https://images.samsclubresources.com/is/image/samsclub/0007073310025_A?null" ,"$10","fri 3:00 pm, mar")	
		#837222903347208193