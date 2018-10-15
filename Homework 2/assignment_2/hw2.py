import requests
import re
import matplotlib.pyplot as plt
import json

def lyrics_word_count_easy(artist, song, phrase):
	response = requests.get("https://api.lyrics.ovh/v1/" + artist + "/" + song)
	if response.status_code != 200:
		print(response.status_code)
		return -1
	json = response.json()
	n = re.findall(phrase, json["lyrics"], re.IGNORECASE)
	return len(n)

def lyrics_word_count(artist, phrase):
    response = requests.get("http://api.musicgraph.com/api/v2/artist/suggest?api_key=c8303e90962e3a5ebd5a1f260a69b138&prefix=gree&limit=3")
    return response.status_code

print(lyrics_word_count("thihng", "thing"))
def visualize():
    pass
