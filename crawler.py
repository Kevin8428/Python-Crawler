import logging
import urllib.request as ur
from urllib.request import Request, urlopen
from urllib.parse import urlsplit
import re
from bs4 import BeautifulSoup
from pprint import pprint
import sys
sys.path

urls = set()
allemails = set()

req = Request('http://' + sys.argv[1], headers={'User-Agent': 'Mozilla/44.0.2'})
sitetext = urlopen(req).read()


soup = BeautifulSoup(sitetext, "lxml")

###### ID all urls and push to global variable
for each in soup.find_all("a"):

    link = each.attrs["href"] if "href" in each.attrs else ''
    if link.startswith('/'):
        link = 'http://' + sys.argv[1]
    if 'twitter' not in link and 'facebook' not in link and 'blog' not in link:
        urls.add(link)

for each in soup.find_all("span"):

    route = each.attrs["ng-click"] if "ng-click" in each.attrs else ''
    route = re.findall(r"'(.*?)'", route, re.DOTALL)
    routestring = ''.join(route)
    link = 'http://' + sys.argv[1] + '/' + routestring
    urls.add(link)
# pprint(urls)


###### cycle thru urls, ID emails and push to global variable

for link in urls:
    try:
        pattern = re.compile(b"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4}", re.IGNORECASE)
        req = Request(link, headers={'User-Agent': 'Mozilla/44.0.2'})
        sitetext = urlopen(req).read()
        # print(sitetext)
        emails = re.findall(pattern,sitetext)
        for subemail in emails:
            allemails.add(subemail)

        otherpattern = re.compile(b"mailto:([a-z0-9!#$%&'*+\/=?^_`{|}~-]+@[a-z0-9]+\.[a-zA-Z0-9-.]+)")
        otheremails = re.findall(otherpattern,sitetext)
        for subemail in otheremails:
            allemails.add(subemail)

    except:
        # logging.exception('')
        pass

pprint (allemails)
