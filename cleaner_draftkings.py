from bs4 import BeautifulSoup
import csv

# https://sportsbook.draftkings.com/leagues/hockey/nhl?category=team-futures

html = ''
with open("input/draftkings.txt") as f:
    html = f.read()
book = 'draftkings'

soup = BeautifulSoup(html, "html.parser")
divs = soup.find_all('li')

with open('data/draftkings.csv', 'w', newline='') as csvfile:
    fieldnames = ['book','team','odds']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for div in divs[2:]:
        team = div.find('span', class_='sportsbook-outcome-cell__label').text.split()[-1]
        odds = div.find('span', class_='sportsbook-odds american default-color').text
        writer.writerow({'book': book,'team': team, 'odds': odds})
        print(team, odds)
