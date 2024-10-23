import requests
from password import api, email_password
import smtplib, ssl

message = ""

def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    username = "mariotest856@gmail.com"
    password = email_password

    receiver = username
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host=host, port=port, context=context) as server:
        server.login(user=username, password=password)
        server.sendmail(username, receiver, message)
        

def create_message(title, description):
    global message
    if article["title"] is not None:
        add_message =title + "\n" + description + 2*"\n"
        message = message + add_message


url = f"https://newsapi.org/v2/everything?q=tesla&from=2024-09-25&sortBy=publishedAt&apiKey={
    api}"

# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access the articles titles and description
for article in content["articles"]:
    create_message(title=article["title"], description=article["description"])

send_email(message=message.encode("utf-8"))
