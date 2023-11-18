import requests
from bs4 import BeautifulSoup
from icecream import ic
import pandas as pd
import csv

def scrape(url, year):
  ic()
  r = requests.get(url + year)
  soup = BeautifulSoup(r.text, 'html.parser')

  return soup.find('table', id="stats")

def iterateTable(table):
  ic()

  pass

footballPlayer = 'Josh Allen'
url = 'https://www.pro-football-reference.com/players/A/AlleJo02' # understand the logic on the player name + number to automate to get multiple players
seasonYear = ['/gamelog/2022', '/gamelog/2021', '/gamelog/2020']

season_tables = [scrape(url, y) for y in seasonYear]

f = open('gameData.csv', 'w', newline='')
scrapedGames = csv.writer(f)

for s in season_tables:
  statList = []
  headerCount = 0
  for headers in s.find_all('th'):
    valueHeader = headers.text
    if valueHeader == 'Rk':
      ic()
      headerCount = 1
    if headerCount == 1:
      ic()
      statList.append(valueHeader)

  scrapedGames.writerow(statList)

  gameArray = []
  breakValue = 0

  for game in s.find_all('tr'):
    cols = game.find_all('td')
    statList = [footballPlayer]
    ic()

    for col in cols:
      if 'Upcoming' in col.text:
        ic()
        breakValue = 1
        break
      else:
        ic()
        stat_col = col.text
        statList.append(stat_col)
      if breakValue == 1:
        ic()
        break
    scrapedGames.writerow(statList)
    gameArray.append(statList)