import os
import requests
import dotenv
import smtplib
import ssl

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

    titles = ""
    descriptions = ""

    for article in articles:
        titles += f"{article['title']} \n"
        descriptions += f"{article['description']} \n"

    message = f"Titles: \n{titles} \n\n Descriptions: \n{descriptions}"

    try:
        with smtplib.SMTP_SSL(host, port, context=context) as server:
            server.login(username, password)
            server.sendmail(username, receiver, message.encode('utf-8'))
    except Exception as e:
        print(f"There was an error sending the email: {e}")
    else:
        print("Email sent.")


if __name__ == "__main__":
    # articles = get_articles()
    send_email()