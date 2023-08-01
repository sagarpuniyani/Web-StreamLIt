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





# CSS class Selector in the Soups object 
print(soup.select("div.Italic"))
print(soup.select("span#text"))
p_text = soup.select("span#text > p")

for p in p_text:
    print(p.get_text().strip())

print(soup.span.get("class"))




# Find the elements by class Name 

print(soup.find_all(class_ = "Italic"))





# Finding the childs in soup page 

for child in soup.find(class_='sender').children:
    print(child)

for parent in soup.find(class_ = "box-1").parents:
    print(parent)
    break



# manupilation  in the HTML file of the DOM 
change_in_tag = soup.find(id="bg-1")
change_in_tag['class'] = "Myclass class-2"
change_in_tag.name = "p"
change_in_tag.string = "Okay Bhai Okay !!!"
print(change_in_tag)
