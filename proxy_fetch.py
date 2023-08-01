import requests

http_proxy = "http://10.10.1.10:3128"
https_proxy = "https://10.10.1.11:1080"
ftp_proxy = "ftp://10.10.1.10:3128"

proxies = {
    "http": http_proxy,
    "https": https_proxy,
    "ftp": ftp_proxy
}

url = "https://lionsgateplay.com/"

# Add the headers you want to include in the request
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

r = requests.get(url, headers=headers, proxies=proxies)

print(r.status_code)  # Print the status code to check if the request was successful
print(r.text)  # Print the response content

# Not giving the response 

# ipaddress is getting blocked and getting the data from other ip's



