from bs4 import BeautifulSoup
import csv

# https://sportsbook.fanduel.com/navigation/nhl?tab=stanley-cup

html = ''
with open("input/fanduel.txt") as f:
    html = f.read()
book = 'fanduel'

soup = BeautifulSoup(html, "html.parser")
divs = soup.find_all('li')

with open('data/fanduel.csv', 'w', newline='') as csvfile:
    fieldnames = ['book','team','odds']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for div in divs[2:]:
        if div.find('div', class_='je') == True:
            break
        try:
            divs1 = div.find('div', class_='aq').find_all('div', class_='at')
            for div1 in divs1:
                spans = div1.find_all('span')
                team = spans[0].text.split()[-1]
                odds = spans[1].text
                writer.writerow({'book': book,'team': team, 'odds': odds})
                print(team, odds)
        except Exception as e:
                break    
# with open('data/bet365.csv', 'w', newline='') as csvfile:
#     fieldnames = ['book','team', 'odds']
#     writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
#     writer.writeheader()
#     for div in divs:
#         team = div.find('span', class_='gl-ParticipantBorderless_Name').text.split()[1]
#         odds = div.find('span', class_='gl-ParticipantBorderless_Odds').text
#         writer.writerow({'book': book,'team': team, 'odds': odds})