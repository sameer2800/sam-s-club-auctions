from Authentication import Auth
import os


def Authenticate_keys(consumer_key , consumer_secret, access_token , access_token_secret):
	auth_instance = Auth(consumer_key , consumer_secret , access_token , access_token_secret)
	api = auth_instance.authorize()
	return api
	