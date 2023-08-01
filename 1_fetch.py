import requests
from bs4 import BeautifulSoup

with open("sample.html" , "r") as f:
    html_doc = f.read()

soup = BeautifulSoup( html_doc , "html.parser")
# print(soup.prettify())
# print(soup.title , type(soup.title))
print(soup.div)

print(soup.find_all("div")[1])

for link in soup.find_all("a"):
    print("Link ---> " , link.get("href"))


# Finding the text of the  tags 
text_div = soup.find_all("div")

for div in text_div:
    print(div.get_text().strip())