import requests

api_key = "c66a601dde0649948c2767aae1bd7ac6"
url = "https://newsapi.org/v2/everything?q=tesla&from=2023-06-10&" \
      "sortBy=publishedAt&apiKey=c66a601dde0649948c2767aae1bd7ac6"

# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access the article titles and descriptions
for article in content["articles"]:
    print(article["title"])
    print(article["description"])
