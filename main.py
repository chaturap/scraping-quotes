import requests
from bs4 import BeautifulSoup


url = 'https://xquotes.toscrape.com/'

headers: dict = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)"
                  " Chrome/112.0.0.0 Safari/537.36",
}

def get_quotes(url: str):
    try:
        res = requests.get(url, headers=headers)
    except Exception:
        return None

    if res.status_code == 200:
        print("ok")
    else:
        print(f"Status Code not 200 , status code is : {res.status_code}")