from Authentication import Auth
import os


def Authenticate_keys(consumer_key , consumer_secret, access_token , access_token_secret):
	auth_instance = Auth(consumer_key , consumer_secret , access_token , access_token_secret)
	api = auth_instance.authorize()
	

if __name__ == '__main__':
		Authenticate_keys("Nr8NWrnIr1huPmlTy3OFfizCl", "94MmEh9HSAGIiolIGSb6hBXXGlFM9weMZNrGjKs6hhJEoNfolr","835036132773605377-ChnMv7F4s7DO6eG1BbKVafgZjYBf1at","jiKWm8tUzXAXuY0ovxc7XWnsbdGj60frsBLUdVIuya7Hr")	