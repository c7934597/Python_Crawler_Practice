import csv

with open('CsvSample.csv', 'r') as csvFile:
    readFile = csv.reader(csvFile)
    for row in readFile:
        print (row)