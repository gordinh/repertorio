import requests
from bs4 import BeautifulSoup
from icecream import ic
import csv

def scrape(url, year):
    ic()
    r = requests.get(url + year)
    soup = BeautifulSoup(r.text, 'html.parser')
    return soup.find('table', id="stats")

def extract_headers(table):
    ic()
    header_count = 0

    return [header.text for header in table.find_all('th') if (header_count := header_count + 1) and header.text == 'Rk']

def extract_game_data(table, player_name):
    ic()
    game_list = []

    for game_row in table.find_all('tr'):
        cols = game_row.find_all('td')
        game_list.append([player_name] + [col.text for col in cols if 'Upcoming' not in col.text] )

    return game_list

def main():
    football_player = 'Josh Allen'
    url = 'https://www.pro-football-reference.com/players/A/AlleJo02'  # Update the URL logic for multiple players
    season_years = ['/gamelog/2022', '/gamelog/2021', '/gamelog/2020']

    f = open('gameData.csv', 'w', newline='')
    scraped_games = csv.writer(f)

    for year in season_years:
        season_table = scrape(url, year)
        if season_table:
            headers = extract_headers(season_table)
            scraped_games.writerow(headers)

            game_data = extract_game_data(season_table, football_player)
            [scraped_games.writerow(game) for game in game_data]

if __name__ == "__main__":
    main()
