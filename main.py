import json

import API_Integration

print("Headlines by country:")
json_str = json.dumps(API_Integration.get_news(country='us'), indent=4)
for line in json_str.splitlines():
    print(line)

print("Headlines by category:")
json_str = json.dumps(API_Integration.get_news_by_category(category='business'), indent=4)
for line in json_str.splitlines():
    print(line)