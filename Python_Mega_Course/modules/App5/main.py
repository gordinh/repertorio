import requests
from send_email import send_email
api_key = "6da7fb372e904db6b53a44a52d8dc576"

topic = "tesla"

url = "https://newsapi.org/v2/everything?" \
  f"q={topic}&" \
  "from=2024-01-29&" \
  "sortBy=publishedAt&" \
  "apiKey=6da7fb372e904db6b53a44a52d8dc576"

request = requests.get(url)

content = request.json()

body = ""
for article in content["articles"][0:20]:
  if article["title"] is not None:
    body = "Subject: Today's news" + "\n" \
      + body + article["title"] + "\n" \
      + article["description"] + "\n" + article["url"] + 2*"\n"

body = body.encode('utf8')
send_email(message=body)