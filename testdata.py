'''
  ***** testdata.py *****

  This file contains the variables that will be used to store all calculated
  test data, organized appropriately for output.

  Author: Chris Blumer & Ryan Hinrichs.
  CSC461 Programming Languages, Fall 2017
'''

import csv
import sys

#variables to be filled with testing results
test_data = []
orig_data = []
samples = []
num_classes = 0
num_features = 0
total_samples = 0
dbname = ""
classnames = []
accuracies = []
output_data = []


def init_test_data( num_cases , classes , dbheader , features):
    """Intializes test arrays with 0's to be 
        filled later or class names"""

    #Appends 0's based on the number of cases
    for i in range(1, num_cases):
        test_data.append(0)
        orig_data.append(0)

    #Add the number of each class into an array
    for num in classes:
        samples.append(num)

    for i in range(1, len(dbheader)):
        classnames.append(dbheader[i].split('=',1)[-1])
        accuracies.append(0)

def fil_test_data( case , clas , ans):
    """Every time we test a point, their 
        result and the actual answer are put in"""
    test_data[case] = clas
    orig_data[case] = ans


def get_test_data( num_cases , classes , dbheader , features):
    """Final calucation of all accuracies
        and data"""
    #Fill variables with calculated values
    num_classes = len(classes)
    num_features = features
    dbname = dbheader[0]
    total_samples = 0
    avg_acc = 0

    #Total up the number of samples
    for num in samples:
        total_samples += num

    for i in range(2, len(test_data)):
        if(test_data[i] != orig_data[i]):
            accuracies[int(orig_data[i])] += 1

    #Set accuracies
    for i in range(0, len(accuracies)):
        if(samples[i] != 0):
            accuracies[i] = float(samples[i] - accuracies[i])/float(samples[i])
        else:
            accuracies[i] = 1

    #Find total average accuracy
    for i in range(0, len(accuracies)):
        if(samples[i] != 0):
            avg_acc += accuracies[i]

    avg_acc /= len(accuracies)

    output_data.append(dbname)          #Name of database is stored in output_data[0]
    output_data.append(num_classes)     #Number of classes is stored in output_data[1]
    output_data.append(num_features)    #Number of features is stored in output_data[2]
    output_data.append(total_samples)   #Total samples is stored in output_data[3]
    output_data.append(classnames)      #List of class names is stored in output_data[4]
    output_data.append(samples)         #List of quantity of samples is stored in output_data[5]
    output_data.append(accuracies)      #List of accuracies is stored in output_data[6]
    output_data.append(total_samples)   #Total samples is stored in output_data[7]
    output_data.append(avg_acc)         #Average accuracy is stored in output_data[8]
    output_data.append(test_data)       #List of tested class values is stored in output_data[9]
    output_data.append(orig_data)       #List of original class values is stored in output_data[10]

    return output_data
