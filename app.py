#!flask/bin/python
from flask import Flask, request, jsonify
from flask import json
import twitter
#from twitter import Authenticate_keys
#from twitter import create_tweet


api = ""

app = Flask(__name__)

@app.route('/auction', methods=['GET'])
def index():
	return "Hello, World!"

@app.route('/auction/set-keys', methods=['POST'])    
def setKeys():
	if request.headers['Content-Type'] == 'application/json':		
		inputData = request.json
		consumer_key = inputData["consumer_key"]
		consumer_secret = inputData["consumer_secret"]
		access_token = inputData["access_token "]
		access_token_secret = inputData["access_token_secret"]	
		api = Authenticate_keys(consumer_key,consumer_secret,access_token,access_token_secret)


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


#@app.route('/auction/get-latest-replies', methods=['POST'])    
#def getList():


#@app.route('/auction/create-reply', methods=['POST'])    
#def createReply():

#@app.route('/auction/create-winner-tweet', methods=['POST'])    
#def createWinnerTweet():


if __name__ == '__main__':
    app.run(debug=True)
