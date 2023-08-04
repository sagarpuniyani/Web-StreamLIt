import requests

def Save(filename, text):
    with open(filename, "w", encoding="utf-8") as f:
        f.write(text)

def fetch(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

    response = requests.get(url , headers=headers)
    if response.status_code == 200:
        return response.text  # Extract the text content from the response
    else:
        print("Error: Unable to fetch URL")
        return None

if __name__ == "__main__":
    print("This is the main program.")
    query = "laptop"
    url = "https://www.amazon.in/s?k="+ query
    print(url)
    HTMLtext = fetch(url)
    if HTMLtext is not None:
        Save("amazon.html", HTMLtext)
