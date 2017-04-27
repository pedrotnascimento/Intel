#!/usr/bin/env python
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
from numpy.random import rand
from numpy import sqrt
import csv
import operator

def load_data_set(filename, split):
    with open(filename, 'rb') as f:
        lines = csv.reader(f)
        dataset = list(lines)
        train = []
        test = []
        for x in xrange(len(dataset)-1):
            for y in xrange(4):
                dataset[x][y] = float(dataset[x][y])
            if rand() < split:
                train.append(dataset[x])
            else:
                test.append(dataset[x])

    return train, test
   
def distance(instance1, instance2, params_length):
    distance = 0
    for x in range(params_length):
        distance += (instance1[x] - instance2[x])**2
    return sqrt(distance)

def get_K_neighbors(train,test,K):
    distances = []
    #for i in range(len(test)):
    for j in range(len(train)):
        dist = distance(test,train[j],3)
        distances.append((train[j],dist))
    distances.sort(key=operator.itemgetter(1))
    neighbors = []
    for k in range(K):
        neighbors.append(distances[k][0])
    return neighbors
    
def getNeighbors(train, testInstance, k):
	distances = []
	length = len(testInstance)-1
	for j in range(len(train)):
		dist = distance(testInstance, train[j], length)
		distances.append((train[j], dist))
	distances.sort(key=operator.itemgetter(1))
	neighbors = []
	for x in range(k):
		neighbors.append(distances[x][0])
	return neighbors

def euclideanDistance(instance1, instance2, length):
	distance = 0
	for x in range(length):
		distance += pow((instance1[x] - instance2[x]), 2)
	return sqrt(distance)

def get_response(neighbors):
    class_votes = {}
    for n in neighbors:
        classe = n[-1]
        if classe in class_votes:
            class_votes[classe] += 1
        else:
            class_votes[classe] = 1
    sorted_votes = sorted(class_votes.iteritems(), key=operator.itemgetter(1), reverse=True)
    return sorted_votes[0][0]

def get_accuracy(tests, predictions):
    correct = 0 
    for i in range(len(tests)):
        correct += 1 if tests[i][-1] == predictions[i] else 0
    return correct/float(len(tests))*100.0

def __main__():
    train, tests = load_data_set("iris-dataset.csv", 0.66)
    # arr_neighbors = [getNeighbors(train, i,3) for i in tests]
    arr_neighbors = [get_K_neighbors(train, i,3) for i in tests]
    predictions = [get_response(arr_neighbors[i]) for i in range(len(tests))]
    accuracy  = get_accuracy(tests, predictions)
    for i in range(len(tests)):
        print "test: ", tests[i][-1], "-- predicted: ", predictions[i]
    print accuracy
        
__main__()
