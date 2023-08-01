import requests

from  fetch_ip import * 

def FetchdataSaveTofile(url, path):
    r = requests.get(url)
    # print(r.text)

    with open(path, "w", encoding="utf-8") as f:
        f.write(r.text)

url = "https://lionsgateplay.com/"
FetchdataSaveTofile(url, r"D:\streamlit\assets\timesofindia.html")

proxy_list = get_free_proxy(url)
# print(proxy_list)




