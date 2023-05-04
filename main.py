import requests
from bs4 import BeautifulSoup
import json


url = 'https://quotes.toscrape.com'
# quote = 0

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
        print(f"Status Code is Ok , status code is : {res.status_code}")
        soup = BeautifulSoup(res.text, 'html.parser')

        # proses scraping
        contents = soup.find_all('div', {'class': 'quote'})
        # print(result)

        # proses looping
        i = 0
        quotes_list: list = []
        for content in contents:
            # print(i, res)
            quote = content.find('span', attrs={'class': 'text'}).text.strip()
            author = content.find('small', attrs={'class': 'author'}).text.strip()
            author_detail = content.find('a')['href']
            # print(quote)
            i = i + 1
            hasil : dict = {
                "quote": quote,
                "author": author,
                "author_detail": url + author_detail,
            }
            quotes_list.append(hasil)

        # proses pengolahan data
        with open('quotes.json', 'w+') as f:
            json.dump(quotes_list, f)

        print("data berhasil di generate")




    else:
        print(f"Status Code not 200 , status code is : {res.status_code}")


    return hasil

def GetDetail(detailurl: str):
    pass

if __name__ == '__main__':
    print("Aplikasi Utama")
    get_quotes(url)
