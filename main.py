import requests
from password import api, email_password

url = f"https://newsapi.org/v2/everything?q=tesla&from=2024-09-25&sortBy=publishedAt&apiKey={
    api}"

# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access the articles titles and description
for article in content["articles"]:
    print(article["title"])
    print(article["description"])

