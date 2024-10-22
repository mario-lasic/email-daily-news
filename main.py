import requests
from password import api, email_password

url = f"https://newsapi.org/v2/everything?q=tesla&from=2024-09-22&sortBy=publishedAt&apiKey={
    api}"

request = requests.get(url)
content = request.text
print(content)