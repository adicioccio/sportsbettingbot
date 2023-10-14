import csv
import pandas as pd

csv_files = ['data/draftkings.csv', 'data/bet365.csv', 'data/fanduel.csv']
output_name = 'data/output.csv'
calculate_csv = 'data/output.csv'

return_num = 100

def merge_csv(csv_files, output):
    data = pd.DataFrame()
    for file in csv_files:
        df = pd.read_csv(file)
        data = data.append(df, ignore_index=True)
    max_odds_per_team = data.groupby('team')['odds'].max()
    result = data.merge(max_odds_per_team, on=['team', 'odds'], suffixes=('', '_max')).drop_duplicates(subset=['team', 'odds'])
    result.to_csv(output, index=False)

def calc_dec(american):
    if american >= 0:
        return 1 + (american / 100)
    return 1 - (100 / american)

def calc(csv_file):
    with open(csv_file, 'r') as csvfile:
        rows = csv.reader(csvfile)
        total_cost = 0
        for row in rows:
            if row[0] == 'book':
                continue
            num = int(row[2].replace("+", ""))
            bet = round(return_num / calc_dec(num), 2)
            total_cost += bet
        print(f"Total bet: ${total_cost} | Total return: ${return_num}")
merge_csv(csv_files, output_name)

calc(calculate_csv)