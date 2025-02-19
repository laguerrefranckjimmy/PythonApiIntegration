import API_Integration

print("Headlines by country:")
print(API_Integration.get_news(country='us'))

print("Headlines by category:")
print(API_Integration.get_news_by_category(category='business'))