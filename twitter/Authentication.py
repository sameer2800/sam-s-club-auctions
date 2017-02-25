import tweepy
import os


class Auth :

	consumer_key = "Nr8NWrnIr1huPmlTy3OFfizCl"
	consumer_secret = "94MmEh9HSAGIiolIGSb6hBXXGlFM9weMZNrGjKs6hhJEoNfolr"
	access_token ="835036132773605377-ChnMv7F4s7DO6eG1BbKVafgZjYBf1at"
	access_token_secret="jiKWm8tUzXAXuY0ovxc7XWnsbdGj60frsBLUdVIuya7Hr"

	def __init__(self) :
		print("Auth class")

	def authorize(self) :
		self.auth = tweepy.OAuthHandler(Auth.consumer_key, Auth.consumer_secret)
		self.auth.set_access_token(Auth.access_token, Auth.access_token_secret)
		self.api = tweepy.API(self.auth)
		self.api.update_status('tweepy + oauth!')
		return self.api

	