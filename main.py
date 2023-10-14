import csv
import pandas as pd

def merge_csv(files, output):
    data = []
    for file in files:
        data.append(pd.read_csv(file))
    merge = pd.concat(data)
    merge.to_csv(output, index=False)

def calc():
    with open('data/output_cleaned.csv', 'r') as csvfile:
        datareader = csv.reader(csvfile)
        total = 0
        for row in datareader:
            if row[0] == 'book':
                continue
            num = int(row[2].replace("+", ""))
            total += num
        print(total/32)

merge_csv(['data/draftkings.csv', 'data/bet365.csv', 'data/fanduel.csv'], 'data/output.csv')

# Read the CSV file into a pandas DataFrame
data = pd.read_csv('data/output.csv')

# Group the data by team and find the maximum odds for each team
max_odds_per_team = data.groupby('team')['odds'].max()

# Merge the data to get the book associated with the maximum odds
result = data.merge(max_odds_per_team, on=['team', 'odds'], suffixes=('', '_max')).drop_duplicates(subset=['team', 'odds'])

# Save the result to a new CSV file
result.to_csv('data/output_cleaned.csv', index=False)

calc()