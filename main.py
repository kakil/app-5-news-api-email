import os
import requests
import dotenv
import smtplib
import ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

dotenv.load_dotenv()

api_key = os.getenv("NEWS_API_KEY")
google_username = os.getenv("GOOGLE_USERNAME")
google_app_password = os.getenv("GOOGLE_APP_PASSWORD")

# url = f'https://newsapi.org/v2/everything?q=%22AI%20tools%22%20OR%20%22AI%20apps%22&from=2024-05-10&sortBy=publishedAt&apiKey={api_key}'
# url = f'https://newsapi.org/v2/everything?q="Data%20Science"%20OR%20"ML"%20OR%20"AI"&language=en&sortBy=publishedAt&apiKey={api_key}'
url = f'https://newsapi.org/v2/everything?q="Data%20Science%20apps"%20OR%20"Machine%20Learning%20apps"%20OR%20"AI%20apps"&language=en&sortBy=publishedAt&apiKey={api_key}'


def get_articles():
    request = requests.get(url)
    content = request.json()
    text_content = request.text
    # for article in content["articles"]:
    #     print(article["title"])
    #     print(article["description"])
    # print(text_content)

    return content["articles"]


def send_email():
    host = "smtp.gmail.com"
    port = 465

    username = google_username
    password = google_app_password

    receiver = "kakil@me.com"
    context = ssl.create_default_context()

    articles = get_articles()

    body = ""

    for article in articles:
        if article["title"] is not None:
            title = article.get("title", "No Title Available")
            description = article.get("description", "No Description Available")
            body += f"<p><strong>{title}</strong><br/>{description}</p>\n"

    # Create MIME message
    msg = MIMEMultipart()
    msg['From'] = username
    msg["To"] = receiver
    msg["Subject"] = "Daily News Update"
    msg.attach(MIMEText(body, 'html'))

    try:
        with smtplib.SMTP_SSL(host, port, context=context) as server:
            server.login(username, password)
            server.sendmail(username, receiver, msg.as_string())
    except Exception as e:
        print(f"There was an error sending the email: {e}")
    else:
        print("Email sent.")


if __name__ == "__main__":
    # articles = get_articles()
    send_email()