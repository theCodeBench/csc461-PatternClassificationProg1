'''
  ***** IOfile.py *****

  This file contains all functions for input from a file and output
  to the .cv file and to the console screen.

  Author: Chris Blumer & Ryan Hinrichs.
  CSC461 Programming Languages, Fall 2017
'''

def screenOut(filename, data):
   """Print classification parameters, classification accuracy for each class,
      and overall classification accuracy to the standard output."""
   print(data[0])
   print("MDC parameters: nclasses = ", data[1], ", nfeatures = ", data[2], ", nsamples = ", data[3])

   # outputs class #, class name, # of sample, & accuracy to the screen
   for i in range(0, data[1]):
      print("class ", i, " (", data[4][i], "): ", data[5][i], " samples, "
         '{:0.1f}'.format(data[6][i]*100), "% accuracy")
   print("overall:   ", data[7], " samples,   ", '{:0.1f}'.format(data[8]*100), "% accuracy")


def cvOut(filename, fout, data):
   """Print classification parameters, classification accuracy, and individual
      sample cross-validation results to an output file, marking incorrectly
      classified samples with an asterisk."""
   oString = data[0] + "\n"
   oString += "MDC parameters: nclasses = "  + str(data[1]) + ", nfeatures = "
   oString += str(data[2]) + ", nsamples = " + str(data[3]) + "\n"
   fout.write(oString)

   # outputs class #, class name, # of sample, & accuracy to file
   for i in range(0, data[1]):
      oString = "class " + str(i) + " (" + str(data[4][i]) + "): " +  str(data[5][i])
      oString += " samples " + str('{:0.1f}'.format(data[6][i]*100)) + "% accuracy\n"
      fout.write(oString)

   # outputs total # of sample and avg accuracy
   oString = "\noverall:   " + str(data[7]) + " samples,   "
   oString += str('{:0.1f}'.format(data[8]*100)) + "% accuracy"
   fout.write(oString)

   # prints the class predictions to the file if prediction is wrong appends *
   fout.write("\nSample, Class, Predicted\n")
   for j in range(0, data[3]):
      if data[10][j] !=  data[9][j]:
         oString = str(j+1) + ',' + str('{:0.0f}'.format(data[10][j])) + ',' + str(data[9][j]) + ' *\n'
         fout.write(oString)
      else:
         oString = str(j+1) + ',' + str('{:0.0f}'.format(data[10][j])) + ',' + str(data[9][j]) + '\n'
         fout.write(oString)


def finOpen(filename):
   """This function opens the input file to be read in."""
   try:
      fin = open( filename , "r")
   except IOError:
      print("cannot open", filename)
   except: #error messge for any other error
      print("some other error happened")
   #else:
      #print("successfully opened ", filename)
   return fin


def foutOpen(filename):
   """This function constructs and opens the output file to be writen
      to using the global string as the base"""
   outFile = (filename[0:len(filename)-4] + ".cv")
   try:
      fout = open(outFile , "w")
   except IOError:
      print("cannot open ", outFile)
   except: #error message for any other error
      print("some other error happened")
   #else:
      #print("successfully opened ", outFile)
   return fout
