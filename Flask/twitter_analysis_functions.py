import tweepy
import time
import pandas as pd
import re
import collections
import json
from datetime import datetime, timedelta
import pickle

consumer_key ='pX1VF2Mp5FicThnpyWmP7GyH3'
consumer_secret = 'zuesUN6OPburvzMssJivbGNwgjfSj3vNCaJ4hbH9WrZlbwhweM'
access_token = '440434796-7YLC6Tnpv8beLCjVhHXLxa9XLxC1aoYI4iP2XrNy'
access_token_secret = '0VzybqOTxPoUQLeuAdmsdAmOtCCyDdPb8wIht12Vg2ukP'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

def analysis(trending_topic):
	last_month = str(datetime.today() - timedelta(days=30))[:10]
	today = str(datetime.today())[:10]
	tomorrow = str(datetime.today() + timedelta(days=1))[:10]
	trend = tweepy.Cursor(api.search, q=trending_topic, since=last_month, until=tomorrow).items()
	data = []
	for i in trend:
		try:
			data.append(i)
			data_text = ' '.join([data[i].text.lower() for i in xrange(len(data))]).encode('utf-8')

	with open("/home/honu/projects/twitter/Flask/" + "db/data/" + today + "_" + trending_topic + ".txt", 'wb') as f:
		pickle.dump(data, f)

	df = pd.DataFrame(columns= ["created_at", "user", "favs", "rt", "lang", "time_zone", "text", "user_pic"])
	for entry in data:
		df = df.append(load_entry(entry), ignore_index = True)

	output = {}
	top_hashtags = hashtags_frequency.most_common(10)
	top_users = at_user_frequency.most_common(10)
	most_fav = df[df["favs"] == df["favs"].max()].head(1)
	most_rt = data[df[df["rt"] == df["rt"].max()].head(1).index[0]].retweeted_status
	time_zones = collections.Counter(df["time_zone"]).most_common(25)

	output["len"] = str(len(df))
	output["lang"] = [[df["lang"].value_counts().head().index[i], str(df["lang"].value_counts().head().values[i])] for i in xrange(5)]
	output["time_zones"] = [[entry[0], str(entry[1])] for entry in time_zones]
	output["hashtags"] = [[top_hashtags[i][0], str(top_hashtags[i][1])] for i in xrange(10)]
	output["users"] = [[top_users[i][0], str(top_users[i][1])] for i in xrange(10)]
	output["most_fav"] = {"user": str(most_fav["user"][most_fav.index[0]]), "user_pic": str(most_fav["user_pic"][most_fav.index[0]]), "text": str(most_fav["text"][most_fav.index[0]]), "favs": str(most_fav["favs"][most_fav.index[0]]), "rt": str(most_fav["rt"][most_fav.index[0]]), "created_at": str(most_fav["created_at"][most_fav.index[0]])}
	output["most_rt"] = {"user": str(most_rt.user.screen_name.encode("utf-8")), "user_id": str(most_rt.user.id),"user_pic": str(most_rt.user.profile_image_url.encode("utf-8")), "text": most_rt.text.encode("utf-8"), "tweet_id": str(most_rt.id), "favs": str(most_rt.favorite_count), "rt": str(most_rt.retweet_count), "created_at": str(most_rt.created_at)}
	output["text"] = data_text

	json_output = json.dumps(output)

	with open("/home/honu/projects/twitter/Flask/" + "db/json/"today + "_" + trending_topic + "_json.txt", 'wb') as f:
		pickle.dump(json_output, f)



###########################
# COMPLEMENTARY FUNCTIONS #
###########################

def load_entry(entry):
	#row = pd.DataFrame(columns= ["created_at", "user", "favs", "rt", "lang", "text", "user_pic"])
	row = pd.Series()
	row["created_at"] = str(entry.created_at)
	row["user"] = entry.user.screen_name.encode("utf-8")
	row["favs"] = entry.favorite_count
	row["rt"] = entry.retweet_count
	row["lang"] = entry.lang.encode("utf-8")
	row["time_zone"] = get_time_zone(entry)
	row["text"] = entry.text.encode("utf-8")
	row["user_pic"] = entry.user.profile_image_url.encode("utf-8")
	
	return row

def get_time_zone(entry):
	if entry._json["user"]["time_zone"] == None:
		return "N/A"
	else:
		return entry._json["user"]["time_zone"].encode("utf-8")