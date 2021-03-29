from __future__ import print_function
import os

print("File Word Search")
print("Program that reads text file and iterates through each line to serach for a word.")
print("This program reads redhat.txt and searches for the word, worm.")
print("--------------------------------------------------------\n")

uniqueWorms = set()

with open("redhat.txt", 'r') as logFile:
    for eachLine in logFile:
        lineList = eachLine.split()
        for eachColumn in lineList:
            if 'worm' in eachColumn.lower():
                uniqueWorms.add(eachColumn)
            
for eachFileName in uniqueWorms:
    print(eachFileName)
    

            
        

      

    
    


        
        
