import requests
from urllib.parse import urljoin
from bs4 import BeautifulSoup
import time
import random

url_max = 50000

urls = list()
with open("urls.txt", "r") as f:
    urls = f.read().split("\n")


def pause_random_time():
    # Generate a random float between 0.1 and 1.0 (adjust the range as needed)
    random_time = random.uniform(0.1, 0.5)
    time.sleep(random_time)

def save_urls():
    print(f"\nloaded {len(urls)} urls")
    with open("urls.txt", 'w') as f:
        f.write('\n'.join(urls))

def search_HTML(html_content):

    soup = BeautifulSoup(html_content, 'html.parser')
    links = soup.find_all('a')

    # get only the links with hrefs
    links = [link for link in links if "href" in link.attrs]

    # get the references from the links
    links = [link["href"] for link in links]

    # clear out empy links
    links = [link for link in links if link != '']

    
    _links = list()
    for link in links:
        
        if "wikipedia.org" in link:
            continue

        if "wikidata.org" in link:
            continue

        if "wikimedia" in link:
            continue

        if "https://" in link:
            continue

        if ":" in link:
            continue

        if "#" in link:
            continue

        if "%" in link:
            continue

        if "&" in link:
            continue
        
        if 'disambiguation' in link:
            continue

        if not "https://" in link:
            link = urljoin("https://wikipedia.org",link)

        _links.append(link)

    links = _links
    del _links

    return links
    

max_recursion_depth = 20

def get_page(url, recursion_depth = 0):

    

    

    if url in terminate_urls:
        return

    if recursion_depth >= max_recursion_depth:
        return
    recursion_depth += 1

    if len(urls) >= url_max:
        return

    urls.append(url)
    print(f"({len(urls)}) ({recursion_depth}) {url}")

    if len(urls) % 200 == 0:
        save_urls()

    pause_random_time()

    response = requests.get(url)
    if response.status_code == 200:

        html = response.text
        links = search_HTML(html)

        for link in links:
            if not link in urls:
                get_page(link, recursion_depth=recursion_depth)

                


start_url = "https://wikipedia.org/wiki/Google_Search"

terminate_urls = list()

get_page(start_url)

