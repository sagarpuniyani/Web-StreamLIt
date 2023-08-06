import requests

page = requests.get("https://books.toscrape.com/")
p_content = page.content
print(p_content)