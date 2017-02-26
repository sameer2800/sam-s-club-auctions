from Authentication import Auth
import Authenticate_keys
import os


def create_tweet(api,auction_id, product_name , image_url, cur_bidding_price , auction_end_time):	
	status = api.update_status("Product: " + product_name[:50] + "\nCurr Bidding Price : " + cur_bidding_price + "\nAuction Ends in: " + auction_end_time)
	print(status.id) 
	return status.id

if __name__ == '__main__':
		create_tweet("!2","sam","q" ,"$4000","sadd")	
