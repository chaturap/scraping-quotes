import pandas as pd
import requests
from bs4 import BeautifulSoup
import json

url = 'https://quotes.toscrape.com'
# quote = 0

class Crawler(object):
    def __init__(self, url:str):
        self.url = url
        self.headers = dict = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)"
                          " Chrome/112.0.0.0 Safari/537.36"
        }

    # disini method
    def get_quotes(self, url: str):
        try:
            res = requests.get(url, headers=self.headers)
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
                hasil: dict = {
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

        return quotes_list

    def GetDetail(self, detail_url: str):
        try:
            res = requests.get(detail_url, headers=self.headers)
        except Exception:
            return None

        if res.status_code == 200:
            soup = BeautifulSoup(res.text, 'html.parser')
            # print(soup)
            # proses scraping
            author_title = soup.find('h3', {'class': 'author-title'}).text.strip()
            born_date = soup.find('span', {'class': 'author-born-date'}).text.strip()
            born_location = soup.find('span', {'class': 'author-born-location'}).text.strip()
            description = soup.find('div', {'class': 'author-description'}).text.strip()

            # proses maping
            data_dict: dict = {
                "author_title": author_title,
                "born_date": born_date,
                "born_location": born_location,
                "description": description,
            }

            # print(data_dict)
            return data_dict

    def generateFormat(self, filename: str, results: list):
        df = pd.DataFrame(results)
        if ".csv" or ".xlsx" not in filename:
            df.to_csv(filename + ".csv", index=False)
            df.to_excel(filename + ".xlsx", index=False)
        print("data genereted")

    def crawling(self) -> list[dict[str, str]]:
        results: list[dict[str, str]] = []

        quotes: list = self.get_quotes(url=url)

        for quote in quotes:
            # print("quote :", quote)
            detail = self.GetDetail(detail_url=quote['author_detail'])
            final_results: dict = {**quote, **detail}
            # print(final_results)
            results.append(final_results)

        # olah data
        self.generateFormat(results=results, filename="reports")

        return results


if __name__ == '__main__':
    print("Aplikasi Utama")
    # get_quotes(url)
    # GetDetail("https://quotes.toscrape.com/author/Steve-Martin")
    scraper: Crawler = Crawler(url=url)
    scraper.crawling()
