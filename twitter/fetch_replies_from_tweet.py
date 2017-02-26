from Authentication import Auth
import os

def fetch_replies_from_tweet(tweet_id):
	auth_instance = Auth("Nr8NWrnIr1huPmlTy3OFfizCl", "94MmEh9HSAGIiolIGSb6hBXXGlFM9weMZNrGjKs6hhJEoNfolr","835036132773605377-ChnMv7F4s7DO6eG1BbKVafgZjYBf1at","jiKWm8tUzXAXuY0ovxc7XWnsbdGj60frsBLUdVIuya7Hr")
	api = auth_instance.authorize()

	tweet = api.get_status(tweet_id)
	print(tweet)


if __name__ == '__main__':
		fetch_replies_from_tweet("835839191388991488")	



