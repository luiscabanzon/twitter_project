####################################
# To translate TXT reports to JSON #
####################################
import pickle
from os import listdir
import json
def to_json(folder_name, n = 0):
	files = listdir(folder_name)
	for file_name in files:
		with open(folder_name + file_name, 'rb') as x:
			data = pickle.load(x)
		with open(folder_name + file_name[:(-4 - n)] + ".json", 'w') as f:
			json.dump(data, f)

to_json("/home/honu/projects/tweetpeek/db/json/", n = 5)
#to_json("/home/honu/projects/tweetpeek/db/trends/")