import os
import requests
import dotenv

dotenv.load()

api_key = os.getenv("NEWS_API_KEY")

# url = f'https://newsapi.org/v2/everything?q=%22AI%20tools%22%20OR%20%22AI%20apps%22&from=2024-05-10&sortBy=publishedAt&apiKey={api_key}'
# url = f'https://newsapi.org/v2/everything?q="Data%20Science"%20OR%20"ML"%20OR%20"AI"&language=en&sortBy=publishedAt&apiKey={api_key}'
url = f'https://newsapi.org/v2/everything?q="Data%20Science%20apps"%20OR%20"Machine%20Learning%20apps"%20OR%20"AI%20apps"&language=en&sortBy=publishedAt&apiKey={api_key}'


request = requests.get(url)
content = request.json()
text_content = request.text
for article in content["articles"]:
    print(article["title"])
    print(article["description"])
# print(text_content)





