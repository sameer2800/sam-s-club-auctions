from Authorization import Auth

#reads timeline of a twitter handle
def read_timeline(api) :
	public_tweets = api.home_timeline()
	for tweet in public_tweets:
		print(tweet.text)


if __name__ == '__main__':
	auth_instance = Auth()
	api = auth_instance.authorize()
	read_timeline(api)
	#post_tweets() 