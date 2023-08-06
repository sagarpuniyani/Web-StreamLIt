from bs4 import BeautifulSoup


with open("1.html", "r") as f:
    html_doc = f.read()


soup = BeautifulSoup(html_doc, "html.parser")
h1_tag = soup.find("h1")
print(h1_tag.string)


def find_list_item():
    list_item = soup.find_all("li")
    list_content = [e.string for e in list_item]
    print(list_content)


find_list_item()


def find_table():
    table_item = soup.find_all("table")

    for i in table_item:
        print(i.get_text().strip())


find_table()
