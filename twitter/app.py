#!flask/bin/python
from flask import Flask, request, jsonify
from flask import json
from Authenticate_keys import Authenticate_keys
from create_tweet import create_tweet
from fetch_replies_from_tweet import fetch_replies_of_tweet
from create_new_reply import create_new_reply
from winner_tweet import winner_tweet

app = Flask(__name__)

@app.route('/auction', methods=['GET'])
def index():
	return "Hello, World!"

@app.route('/auction/set-keys', methods=['POST'])    
def setKeys():
	if request.headers['Content-Type'] == 'application/json':		
		global api
		inputData = request.json
		consumer_key = inputData["consumer_key"]
		consumer_secret = inputData["consumer_secret"]
		access_token = inputData["access_token"]
		access_token_secret = inputData["access_token_secret"]	
		api = Authenticate_keys(consumer_key,consumer_secret,access_token,access_token_secret)
		data = {}
		data['status'] = 200
		json_data = json.dumps(data)
		return json_data



@app.route('/auction/create-auction-tweet', methods=['POST'])    
def createTweet():
	if request.headers['Content-Type'] == 'application/json':		
		inputData = request.json
		auction_id = inputData["auction_id"]
		product_name = inputData["product_name"]
		image_url = inputData["image_url"]
		cur_bidding_price = inputData["cur_bidding_price"]		
		auction_end_time = inputData["auction_end_time"]
		status_id = create_tweet(api,auction_id,product_name,image_url,cur_bidding_price,auction_end_time)
		data = {}
		data['tweet_id'] = status_id
		json_data = json.dumps(data)
		return json_data

		

#@app.route('/auction/parse-tweet', methods=['POST'])    
#def parseTweet():


@app.route('/auction/get-all-replies', methods=['POST'])    
def getList():
	if request.headers['Content-Type'] == 'application/json':		
		inputData = request.json
		auction_id = inputData["auction_id"]
		replies = fetch_replies_of_tweet(api,auction_id)
		data = {}
		data['replies'] = replies
		json_data = json.dumps(data)
		return json_data		


@app.route('/auction/create-reply', methods=['POST'])    
def createReply():
	if request.headers['Content-Type'] == 'application/json':		
		inputData = request.json
		tweet_id = inputData["tweet_id"]
		auction_id = inputData["auction_id"]
		bid_value = inputData["bid_value"]

		create_new_reply(api, tweet_id, auction_id, bid_value)
		data = {}
		data['status'] = 200
		json_data = json.dumps(data)
		return json_data

		
@app.route('/auction/create-winner-tweet', methods=['POST'])    
def createWinnerTweet():
	if request.headers['Content-Type'] == 'application/json':		
		inputData = request.json
		auction_id = inputData["auction_id"]
		product_name = inputData["product_name"]
		image_url = inputData["image_url"]
		product_url = inputData["product_url"]
		winner_handle = inputData["winner_handle"]		
		winner_tweet(api, winner_handle, auction_id,image_url, product_url , product_name)	
		data = {}
		data['status'] = 200
		json_data = json.dumps(data)
		return json_data

if __name__ == '__main__':
    #app.run(debug=True)
    app.run(host='127.0.0.1', port=8016, debug=True)








