import requests
API_KEY = '96e7bc70b12c3baa51589b869b6b2cfe'

def get_data(place, forecast_days=1):
  url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&cnt={8*forecast_days}&appid={API_KEY}"
  response = requests.get(url=url)
  filtered_data = response.json()["list"]
  return filtered_data

if __name__ == '__main__':
  print(get_data(place="Tokyo", forecast_days=3))