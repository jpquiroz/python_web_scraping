import time
import random
import requests
from bs4 import BeautifulSoup

url_site = 'https://scholar.google.com'
url_search = '/citations?hl=en&view_op=search_authors&mauthors={}'

author = 'tesla'

url = url_site + url_search.format(author)

time.sleep(random.random())
page = requests.get(url)

if page.status_code != 200:
    print ('error' , page.reason)

soup = BeautifulSoup(page.content, 'html.parser')
#print(soup.prettify())

author_link = ""
for text in soup.findAll(attrs={'class': 'gs_ai_name'}):
            for links in text.findAll('a'):
                author_link = links.get('href')
                #print (author_link)

if author_link != "":
    author_url = url_site + author_link

    time.sleep(random.random())
    page_author = requests.get(author_url)
    print (author_url)

    if page_author.status_code != 200:
        print ('error' , page_author.reason)

    soup_author = BeautifulSoup(page_author.content, 'html.parser')

    domains = []
    for text in soup_author.findAll(attrs={'class': 'gsc_prf_il', 'id' : 'gsc_prf_int'}):
        for link in text.findAll('a'):
            domains.append(link.getText())
            print (link.getText())

