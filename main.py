import requests
from password import api, email_password
import smtplib
import ssl

message = "Subject: Today's news \n"

topic="amazon"

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


def create_message(title="", description="", article=""):
    global message
    print(title, description, article)
    add_message = title + "\n" + description + "\n" + article + 2*"\n"
    message = message + add_message


url = f"https://newsapi.org/v2/everything?q={topic}&sortBy=publishedAt&language=en&apiKey={
    api}"

# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()
print(content)

# Access the articles titles and description
for article in content["articles"][0:20]:
    if article["title"] is not None:
        if article["description"] is not None:
            create_message(
                title=article["title"], description=article["description"].strip(), article=article["url"])
        else:
            create_message(title=article["title"],
                           description="", article=article["url"])

send_email(message=message.encode("utf-8"))