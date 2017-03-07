from Authentication import Auth
import os
import tweepy
import re

def create_new_reply_temp(status_id, auction_id, bid_value) :
	auth_instance = Auth("Nr8NWrnIr1huPmlTy3OFfizCl", "94MmEh9HSAGIiolIGSb6hBXXGlFM9weMZNrGjKs6hhJEoNfolr","835036132773605377-ChnMv7F4s7DO6eG1BbKVafgZjYBf1at","jiKWm8tUzXAXuY0ovxc7XWnsbdGj60frsBLUdVIuya7Hr")
	api = auth_instance.authorize()
	tweet = "@samsclubauct #"+ auction_id + " Bid from Website User: " + bid_value
	api.update_status(tweet, status_id)



def create_new_reply(api, status_id, auction_id, bid_value) :
	
	tweet = "@samsclubauct #"+ auction_id + " Bid from Website User: " + bid_value
	api.update_status(tweet, status_id)


if __name__ == '__main__':
	create_new_reply_temp("835839191388991488","auct_123456678" , "$2345")

