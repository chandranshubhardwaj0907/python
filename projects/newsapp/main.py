import requests
query =input("Enter the query for news articles: ")
# This script fetches news articles based on a user-defined query using the News API.

api = "46dcb52f88a947f4949b6ef7b69c5d90"


url = f"https://newsapi.org/v2/everything?q={query}&from=2025-05-21&sortBy=publishedAt&apiKey={api}"

print(url)

c = requests.get(url)
data = c.json()
articles = data["articles"]


for article in articles:
    title = article["title"]
    description = article["description"]
    url = article["url"]
    print(f"Title: {title}")
    print(f"Description: {description}")
    print(f"URL: {url}")
    print("-" * 80)  # Separator for readability