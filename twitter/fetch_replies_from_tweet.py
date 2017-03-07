from Authentication import Auth
import os
import tweepy
import re


def extract_amount_from_tweet(tweet):
	amount = [word for word in tweet.split() if word.startswith('$')]
	return amount[0]


def jsonize(data) :
	
	jsonz = []

	for key ,value in data.items() :
		dictn = dict()
		dictn['username'] = key
		dictn['bids'] = value
		jsonz.append(dictn)

	return jsonz	

def fetch_replies_of_tweet(api,auction_id):
	
	replies = api.search(q="#"+ auction_id)
	
	dictnry = dict()	

	for reply in replies :
		tweet = reply.text
		amount = extract_amount_from_tweet(tweet)
		author =reply.author._json['screen_name']
		if author in dictnry:
			dictnry[author].append(amount)
		else :			
			dictnry[author] = []
			dictnry[author].append(amount)



	#return dictnry	
	return jsonize(dictnry)


def fetch_replies_of_tweet1(auction_id):
	auth_instance = Auth("Nr8NWrnIr1huPmlTy3OFfizCl", "94MmEh9HSAGIiolIGSb6hBXXGlFM9weMZNrGjKs6hhJEoNfolr","835036132773605377-ChnMv7F4s7DO6eG1BbKVafgZjYBf1at","jiKWm8tUzXAXuY0ovxc7XWnsbdGj60frsBLUdVIuya7Hr")
	api = auth_instance.authorize()

	replies = api.search(q="#"+ auction_id)
	
	dictnry = dict()	

	for reply in replies :
		tweet = reply.text
		amount = extract_amount_from_tweet(tweet)
		author =reply.author._json['screen_name']
		if author in dictnry:
			dictnry[author].append(amount)
		else :			
			dictnry[author] = []
			dictnry[author].append(amount)



	#return dictnry	
	return jsonize(dictnry)	

def user_timeline() :
	auth_instance = Auth("Nr8NWrnIr1huPmlTy3OFfizCl", "94MmEh9HSAGIiolIGSb6hBXXGlFM9weMZNrGjKs6hhJEoNfolr","835036132773605377-ChnMv7F4s7DO6eG1BbKVafgZjYBf1at","jiKWm8tUzXAXuY0ovxc7XWnsbdGj60frsBLUdVIuya7Hr")
	api = auth_instance.authorize()
	
	#api.update_status("hello ")
	tweets = api.user_timeline(screen_name="samsclubauct" , in_reply_to_status_id="835839191388991488")
	#data = json.dumps(tweets);
	#print(data['id_str'])
	

	#for status in tweepy.Cursor(api.user_timeline ,screen_name="samsclubauct", since_id="835839191388991488",in_reply_to_status_id="835839191388991488", count= 20).items() :
	#	print(status.text)

	#for status in tweepy.Cursor(api.user_timeline ,screen_name="samsclubauct", since_id="835839191388991488",in_reply_to_status_id="835839269621071872", count= 20).items() :
	#	print(status.text)

	#for status in tweepy.Cursor(api.user_timeline ,screen_name="samsclubauct", since_id="835839191388991488",conversation_id="835839191388991488", count= 20).items() :
	#	print(status.text)
	#	print(status.id)


	#for status in tweepy.Cursor(api.user_timeline ,screen_name="samsclubauct", in_reply_to_user_id_str="835839191388991488", count= 20).items() :
	#	print(status.text)

	for tweet in tweets :
		print(tweet.text)


if __name__ == '__main__':
		a =fetch_replies_of_tweet("auct_123456678")	
		print(a)
		#user_timeline()
