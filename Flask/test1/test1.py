from flask import Flask, render_template
app = Flask(__name__)

from flask.ext.bootstrap import Bootstrap
bootstrap = Bootstrap(app)


#############
###  TWEEPY LOADING
#############
import tweepy
import time

consumer_key ='pX1VF2Mp5FicThnpyWmP7GyH3'
consumer_secret = 'zuesUN6OPburvzMssJivbGNwgjfSj3vNCaJ4hbH9WrZlbwhweM'
access_token = '440434796-7YLC6Tnpv8beLCjVhHXLxa9XLxC1aoYI4iP2XrNy'
access_token_secret = '0VzybqOTxPoUQLeuAdmsdAmOtCCyDdPb8wIht12Vg2ukP'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

###############
###############


# @app.route('/index')
# def index():
# 	return render_template('index.html')

@app.route('/user/<name>')
def  user(name):
	user = api.get_user(name)
	user_data = {}
	user_data["name"] = user.screen_name
	user_data["followers"] = []
	user_data["following"] = []

	for page in tweepy.Cursor(api.followers, screen_name= name).pages():
		user_data["followers"].extend(page)
		time.sleep(2)

	user_data["n_followers"] = len(user_data["followers"])
	#user_data["followers"] = [] 

	#for i in user_data["followers_ids"]:
	#	follower = api.get_user(i)
	#	name = follower.screen_name
	#	user_data["followers"].append(name)

	for page in tweepy.Cursor(api.friends, screen_name= name).pages():
		user_data["following"].extend(page)
		time.sleep(2)

	user_data["n_following"] = len(user_data["following"])

	return render_template('user.html', user_data = user_data)


@app.route('/hashtag/<hashtag>')
def hashtag(hashtag):
	data = tweepy.Cursor(api.search, q= '#' + hashtag).items()
	return render_template('hashtag.html', data = data)


"""
@app.errorhabdler(404)
def page_not_found(e)
	return render_template("404.html"), 404

@app.errorhabdler(500)
def internal_server_error(e)
	return render_template("500.html"), 500

"""

#from flask.ext.script import Manager
#manager = Manager(app)

if __name__ == '__main__':
	app.run(debug=True) #manager.run()

# python test1.py runserver --host 0.0.0.0