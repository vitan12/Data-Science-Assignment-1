#
# CS 196 Data Hackerspace
# Assignment 1: Data Parsing and NumPy
# Due September 24th, 2018
#

import json
import csv
import numpy as np
import re

def histogram_times(filename):
	f = open(filename)
	csv_file = csv.reader(f)
	crashes_per_hour = []
	for row in csv_file:
		if row[1] != "" and row[1] != "Time":
  			crashes_per_hour.append(row[1][:2])
	crashes = []
	for x in range(24):
		y = "%02d" % x
		i = 0
		for time in crashes_per_hour:
			if y == time:
				i += 1
		crashes.append(i)
	return crashes


def weigh_pokemons(filename, weight):
	with open(filename) as json_file:  
		data = json.load(json_file)
	returnList = []
	for p in data['pokemon']:
		weight1 = re.findall("[+-]?\d+\.\d+", p['weight'])
		weight12 = weight1[0]	
		if weight12 == weight:
			returnList.append(p['name'])
	return returnList
    

def single_type_candy_count(filename):
	with open(filename) as json_file:  
		data = json.load(json_file)
	candyCount = 0
	for p in data['pokemon']:
		if len(p['type']) == 1:
			if 'candy_count' in p:
				candyCount += p['candy_count']
	return candyCount

def reflections_and_projections(points):
	pointsFloat = points.astype(float)
	points1 = np.flip(pointsFloat,0)
	cols = points1.shape[1]
	print(points1)
	rotate90 = np.array([[0, -1],[1, 0]])
	for y in range(0, cols):
		flippedCordinate = np.array([[points1[0,y]],[points1[1,y]]])
		flippedRotated = np.matmul(rotate90, flippedCordinate)
		points1[0,y] = flippedRotated[0,0]
		points1[1,y] = flippedRotated[1,0]
		projection = np.array([[1,3],[3,9]])
		rotatedCord = np.array([[points1[0,y]],[points1[1,y]]])
		projected = (np.matmul(projection, rotatedCord))
		points1[0,y] = .1*projected[0,0]
		points1[1,y] = .1*projected[1,0]
	print(points1)


def normalize(image):
	image *= 255
	image = image/(np.max(image)-np.min(image))
	image *= (image - np.min(image))
	return image

def sigmoid_normalize(image, a):
    image = image/(1+(1/(1 / np.exp((1 / a)+image - 128))))
    image *= 255
    print(image)



