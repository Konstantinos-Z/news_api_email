import requests
from send_email import send_mail

topic = "tesla"

api_key = "c66a601dde0649948c2767aae1bd7ac6"
url = "https://newsapi.org/v2/everything?" \
      f"q={topic}" \
      "&sortBy=popularity" \
      "&apiKey=c66a601dde0649948c2767aae1bd7ac6" \
      "&language=en"

# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access the article titles and descriptions
message = "Subject: Today's news \n"
for article in content["articles"][:20]:
    if article is not None:
        message = message + article["title"] + "\n"\
               + article["description"] + "\n"\
               + article["url"] + 2*"\n"

encoded_message = message.encode('utf-8')
send_mail(encoded_message)
