import requests


def get_news(country, api_key='890603a55bfa47048e4490069ebee18c'):
  url = f'https://newsapi.org/v2/top-headlines?country={country}&apiKey={api_key}'
  r = requests.get(url)
  content = r.json()
  articles = content['articles']
  results = []
  for article in articles:
    results.append(f"{article['title']}\n"
                   f" {article['description']}\n")
  return results



def get_news_by_category(category, api_key='890603a55bfa47048e4490069ebee18c'):
  url = f'https://newsapi.org/v2/top-headlines?category={category}&apiKey={api_key}'
  r = requests.get(url)
  content = r.json()
  articles = content['articles']
  results = []
  for article in articles:
    results.append(f"{article['title']}\n"
                   f" {article['description']}\n")
  return results