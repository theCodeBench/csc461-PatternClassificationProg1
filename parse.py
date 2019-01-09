'''
  ***** parse.py *****

  This file contains the leave-one-out cross validation teaching technique for
  the program, calculating minimum distance between centroids and choosing the
  class based on smallest distance.

  Author: Chris Blumer & Ryan Hinrichs.
  CSC461 Programming Languages, Fall 2017
'''

import csv
import sys
import testdata


def parseLists( fin ):
    """Parses data into a list of lists and runs the leave-one-out
        cross validation on the test data"""
    reader = csv.reader( fin )
    data = list( reader )
    count = []
    accumul = [[] for x in range(len(data[0])-1)]

    #Turn all numbers into floats
    for i in range( 2, len(data)):
        for j in range( 0, len(data[i])):
            data[i][j] = float(data[i][j])

    #Fill accumulator array with 0's
    for clas in accumul:
        count.append(0)
        for i in range(len(data[1])-2):
            clas.append(0)

    #Normalize data
    make_normal(data, count)

    #Initialize test data arrays
    testdata.init_test_data( len(data) , count , data[0] , len(data[1]) - 2)

    #Run leave-one-out cross validation on all data points
    for k in range(2, len(data)-1):
        test_datapoint( data, accumul, k, count)
        for i in range(0, len(accumul)):
            count[i] = 0
            for j in range(0, len(accumul[i])):
                accumul[i][j] = 0

    #Fill data list with calculated results
    data = testdata.get_test_data(len(data) , count , data[0] , len(data[1]) - 2)

    return data


def make_normal( data , count):
    """Normalizes the value points to the formula:
        (datapoint - minimum) / (maximum - minimum)"""
    max = []
    min = []

    #Initializes the max and min to the first value in the data set
    for i in range(2, len(data[1]) ):
        max.append(data[2][i])
        min.append(data[2][i])

    #Set the max and min based on the data set
    for j in range(2,len(data)):
        for i in range(2, len(data[1])):
            if data[j][i] > max[i - 2]:
                max[i - 2] = data[j][i]
            if data[j][i] < min[i - 2]:
                min[i - 2] = data[j][i]

    #Normalize data
    for j in range(2,len(data)):
        for i in range(2, len(data[1])):
            data[j][i] = (data[j][i] - min[i - 2])/(max[i - 2] - min[i - 2])

    #Find the number of each given class in the sample set
    for j in range(2,len(data)):
        count[int(data[j][1])] = count[int(data[j][1])] + 1

def test_datapoint( data, accumul, lvout, count): 
    """Test a given datapoint off a copy of the dataset, calculating centroids
        and guessing the class of the datapoint off the minimum distance"""

    copy = []
    for row in data:
        copy.append(row[:])

    #Add up all the values to find the average
    for j in range(2,len(data)):
        if j != lvout:
            count[int(data[j][1])] = count[int(data[j][1])] + 1
            for i in range(2, len(data[1])):
                accumul[int(copy[j][1])][i-2] = accumul[int(copy[j][1])][i-2] + copy[j][i]

    #Divide by total number of samples in each class
    for j in range(len(accumul)):
        for i in range(len(data[1])-2):
            if count[j]!= 0:
                accumul[j][i] = accumul[j][i] / count[j]

    #Square root the sum of the squares in the first index of the accumulator
    #array
    for i in range(0, len(accumul)):
        for j in range(0, len(accumul[0])):
            accumul[i][j] = (accumul[i][j] - copy[lvout][j + 2])**2
        for j in range(1, len(accumul[0])):
            accumul[i][0] += accumul[i][j]
        accumul[i][0] = accumul[i][0]**(0.5)

    min_dist = float("inf")
    targ_class = -1

    #Find the minimum distance and assign the class based on that
    for i in range(0, len(accumul)):
        if accumul[i][0] < min_dist:
            min_dist = accumul[i][0]
            targ_class = i

    #Save data
    testdata.fil_test_data( lvout , targ_class , data[lvout][1])

