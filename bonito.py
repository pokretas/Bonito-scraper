from bs4 import BeautifulSoup as bs4
import requests
import pandas as pd
import re

pages = []
prices = []
titles = []
authors = []
details = []
descriptions = []
links = []

books = {'Author':authors,
         'Title': titles,
         'Details': details,
         'Price':prices,
         'Descriptions': descriptions,
         'Links': links}
pages_to_scrape = 1
for websites in range (0,pages_to_scrape,+1):
    url = ('https://bonito.pl/l-658-{}-literatura-piekna').format(websites)
    pages.append(url)
for book in pages:
    page = requests.get(book)
    soup = bs4(page.text, 'html.parser')
    for Title in soup.findChildren('a', rel='follow', recursive=True):
        title = Title.getText()
        titles.append(title)
    for Price in soup.findAll('font', color='black', style='font-size: 12pt;', recursive=True):
        price = Price.getText()
        prices.append(price)
    for Author in soup.find_all('div', style='margin-right: 10px; margin-bottom: 5px;'):
        author = Author.getText()
        if "wydawnictwo:" in author:
            details.append(author)
        else:
            authors.append(author)
    for Description in soup.findAll('div', align="justify", style="margin-bottom: 5px;", recursive=True):
        description = Description.getText()
        descriptions.append(description)
    for Link in soup.find_all('a', rel='follow', href=True):
        link = "https://bonito.pl" + Link.get('href')
        links.append(link)

#Exportdf
df = pd.DataFrame(data=books)
df.index += 1
df.to_excel("próóóóba.xlsx")