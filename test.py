from bs4 import BeautifulSoup
import requests
import datetime
import scraper
import utils.download
from urllib.parse import urlparse
import json
from collections import defaultdict

#url = 'https://crawler-test.com/links/page_with_external_links'
#url = "https://archive.ics.uci.edu/ml/datasets/Letter+Recognition"
#url = "https://ics.uci.edu/~thornton/ics46/Notes/SmartPointers/"
#url = "https://crawler-test.com"
url = "https://vision.ics.uci.edu"
parsed_url = urlparse(url)
print(parsed_url.hostname)
grab = requests.get(url)


host_name = parsed_url.hostname.lstrip("www.").split(".")
print(host_name)

if host_name[0] != "ics" and host_name[1] == "ics":
    print("ahhhh")

soup = BeautifulSoup(grab.text, 'lxml')

#print(soup.get_text())

page_word_counts = defaultdict(int)
common_words = defaultdict(int)


subdomains = defaultdict(int)
redirects = defaultdict(str)
general_analytics = defaultdict(int)

# print(scraper.is_redirect(url, grab.url))


# print(page_word_dict)

# print("unique pages:", len(unique_pages))
# print(next_links)





