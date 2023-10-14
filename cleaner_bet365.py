from bs4 import BeautifulSoup
import csv

# https://www.bet365.com/#/AC/B17/C20890481/D1/E90598494/F2/

html = ''
with open("input/bet365.txt") as f:
    html = f.read()
book = 'bet365'

soup = BeautifulSoup(html, "html.parser")
divs = soup.find_all('div', class_='gl-ParticipantBorderless')

with open('data/bet365.csv', 'w', newline='') as csvfile:
    fieldnames = ['book','team','odds']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for div in divs:
        team = div.find('span', class_='gl-ParticipantBorderless_Name').text.split()[-1]
        odds = div.find('span', class_='gl-ParticipantBorderless_Odds').text
        writer.writerow({'book': book,'team': team, 'odds': odds})
        print(team, odds)