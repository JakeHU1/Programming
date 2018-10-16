import csv
with open('gamers.csv', 'r') as myCSVFile:
    reader = csv.reader(myCSVFile, delimiter=';')
    score = 0
    highest_score = None
    for row in reader:
        if int(row[2]) > score:
            score = int(row[2])
            highest_score = 'De hoogste score is: ' + row[2] + ' op ' + row[1] + ' behaald door ' + row[0]
    print(highest_score)