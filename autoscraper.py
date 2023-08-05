import requests
from bs4 import BeautifulSoup


http_proxy  = "http://179.63.149.5"
https_proxy = "http://123.138.214.150"
ftp_proxy   = "http://58.20.77.168"

proxies = { 
            "http"  : http_proxy, 
            "http" : https_proxy, 
            "http"   : ftp_proxy
            }


# r = requests.get(url, headers=headers, proxies=proxies)

def Save(filename, text):
    with open(filename, "w", encoding="utf-8") as f:
        f.write(text)



def fetch(url):
    headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.24Safari537.36"}
    response = requests.get(url , headers= headers , proxies= proxies )
    # print(response.text)
    return response.text


def fetch_all_link(html):
    links_list = []
    soup = BeautifulSoup( html  , "html.parser")
    for link in soup.find_all('a'):
        # print(link.get('href'))
        if "/dp/" in link.get('href'):
            links_list.append(link.get('href'))




web_url = "https://www.amazon.in/s?k=laptop&i=computers&rh=n%3A1375424031&dc&ds=v1%3ARxXFPtdDoFuQMEI%2B%2FLmYJyiuOD6PRqqf%2F34%2FJeiCv3E&adgrpid=94221362531&ext_vrnc=hi&hvadid=590450674960&hvdev=c&hvlocphy=9075215&hvnetw=g&hvqmt=e&hvrand=9861650399147133875&hvtargid=kwd-353766051967&hydadcr=16601_2163995&qid=1691214944&rnid=7005020031&tag=googinhydr1-21&ref=sr_nr_p_n_feature_seven_browse-bin_7"


fetch_page = fetch( web_url)
Save("amazon.html" , fetch_page)
fetch_all_link(fetch_page)

