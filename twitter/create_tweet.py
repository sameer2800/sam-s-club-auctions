from Authentication import Auth
import os


def create_tweet(auction_id, product_name , image_url, cur_bidding_price , auction_end_time):
	auth_instance = Auth("Nr8NWrnIr1huPmlTy3OFfizCl", "94MmEh9HSAGIiolIGSb6hBXXGlFM9weMZNrGjKs6hhJEoNfolr","835036132773605377-ChnMv7F4s7DO6eG1BbKVafgZjYBf1at","jiKWm8tUzXAXuY0ovxc7XWnsbdGj60frsBLUdVIuya7Hr")
	api = auth_instance.authorize()
	status = api.update_status("Product: " + product_name[:50] + "\nCurr Bidding Price : " + cur_bidding_price + "\nAuction Ends in: " + auction_end_time)
	print(status.id) 
	return status.id

if __name__ == '__main__':
		create_tweet("!2","sam","q" ,"$4000","sadd")	
