import csv

with open('data/fanduel.csv', 'r') as csvfile:
    datareader = csv.reader(csvfile)
    total = 0
    for row in datareader:
        if row[0] == 'book':
            continue
        num = int(row[2].replace("+", ""))
        total += num
    
    print(total/32)