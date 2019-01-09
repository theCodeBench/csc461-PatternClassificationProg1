'''
  ***** main.py *****

  This python program implements a minimum distance classifier.
  The input data will be read in from a comma-seperated value file.
  Consol outpt will include classifier accuracy.
  Sample classification results will be written to an output file.

  Usage:	python main.py datafile.csv

  Author: Chris Blumer & Ryan Hinrichs.
  CSC461 Programming Languages, Fall 2017
'''

import sys
import IOfile
import parse

def main():
   '''runs all of the key functions to bring this program together'''
   filename = sys.argv[-1]
   fin = IOfile.finOpen(filename)
   data = parse.parseLists( fin )     #Results from leave-one-out validation
   IOfile.screenOut(filename, data)
   fout = IOfile.foutOpen(filename)
   IOfile.cvOut(filename, fout, data)
   fin.close()
   fout.close()

'''Runs the main function'''
if __name__ =='__main__':
   main()
