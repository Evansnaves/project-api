from bs4 import BeautifulSoup
import requests

page_to_scrape = requests.get("https://www.hobbystation-single.jp/db/product/list?HbstSearchOptions[0][id]=80&HbstSearchOptions[0][search_keyword]=(BANNER)%E3%83%96%E3%83%BC%E3%82%B9%E3%82%BF%E3%83%BC%E3%83%91%E3%83%83%E3%82%AF%E3%80%80%E9%99%90%E7%95%8C%E3%82%92%E8%B6%85%E3%81%88%E3%81%97%E8%80%85%5BFB04%5D(BANNER)&HbstSearchOptions[0][Type]=2")
print(f'Succesfull Request...')

soup = BeautifulSoup(page_to_scrape.text, "html.parser")

