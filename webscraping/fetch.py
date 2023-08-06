import re

from bs4 import BeautifulSoup


with open("1.html", "r") as f:
    html_doc = f.read()


class parsed_item_loaction:
    """
    A class which are able to locate the item where they are llocated in the HTML
    page

    This Allow to see what will be our code looking at as well as change it quickly

    seprating the how and what should program do
    """





class parsed_item :
    """
    A class takes the HTML page and find the properties of it
    """

    def __init__(self , page ):
        self.soup = BeautifulSoup(page , "html.parser")


    def find_h1(slef):
        h1_tag  = slef.soup.find('h1')
        print(h1_tag.string)



    def find_list_item(self):
        list_item = self.soup.find_all("li")
        list_content = [e.string for e in list_item]
        print(list_content)




    def find_table(self):
        table_item = self.soup.find_all("table")

        for i in table_item:
            print(i.get_text().strip())




    def find_p(self):
        p_tag = self.soup.find_all('p')
        list_para_other = [p for p in p_tag if 'base' not in p.attrs.get('class' , []) ]
        print(list_para_other[0].string)


    def locator_item(self):
        locating_item = self.soup.select_one("div.container h3 a ")
        locating_link = locating_item.attrs['title']
        print(locating_link)


    def locator_link(self):
        locating_item = self.soup.select_one("div.container h3 a ")
        locating_link = locating_item.attrs['href']
        print(locating_link)




    def find_item_price(self):
        item_price = self.soup.select_one('div.container h3 a p.price')

        if item_price:
            pattern = r'Rs\. ([0-9]+\.([0-9]++))'
            matcher = re.search(pattern, item_price.get_text())

            if matcher:
                print(matcher.group(0))
                print(float(matcher.group(1)))
                print("0.",float(matcher.group(2)))
                # print(float(matcher.group(1)))
            else:
                print("Pattern not found in item price.")
        else:
            print("Item price element not found.")





    def find_item_rating(self):
        item_rating = self.soup.select_one('p.star_rating')
        class_rating = item_rating.attrs['class']

        list_classes = [r for r in class_rating if r!= 'star_rating']
        print("list_classes = " , list_classes)
        list_class = filter(lambda x : x != 'star_rating' , class_rating)
        print("list_class = " , list(list_class))


    # find_item_rating()
    # find_h1()
    # find_item_price()
    # locator_link()
    # locator_item()
    # find_p()
    # find_table()
    # find_list_item()

item = parsed_item(html_doc)
item.find_p()
item.locator_item()
item.find_list_item()
item.find_table()
item.find_item_rating()
item.find_item_price()
item.locator_link()
item.find_h1()