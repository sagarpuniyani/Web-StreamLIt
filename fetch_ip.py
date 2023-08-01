import requests
from bs4 import BeautifulSoup as bs

def get_free_proxy(url):
    r = requests.get(url)
    soup = bs(r.content, "html.parser")

    proxies = []

    # Check if the table with class "table-striped" is found
    tables = soup.find("table", attrs={"class": "table-striped"})
    if tables:
        for row in tables.find_all("tr")[1:]:
            tds = row.find_all("td")
            try:
                ip = tds[0].text.strip()
                port = tds[1].text.strip()
                proxies.append(ip + ":" + port)
            except IndexError:
                continue

    return proxies

url = "https://proxyscrape.com/free-proxy-list"
proxy_list = get_free_proxy(url)
# print(proxy_list)

length = len(proxy_list)
len_str = str(length)

for i in range(len(proxy_list)):
    proxy = proxy_list[i]

    print("Proxy number:", (i + 1), "/", len_str)
    try:
        # Replace 'https://www.example.com' with the website URL you want to test with the proxies
        response = requests.get("https://www.example.com", proxies={"http": proxy, "https": proxy}, timeout=5)

        # Display the status code and response content
        print("Status Code:", response.status_code)
        print(response.text)

    except requests.RequestException as e:
        # If the IP is not reachable or response not available
        print("Not Available:", e)

