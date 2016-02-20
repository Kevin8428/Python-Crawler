import urllib.request as ur
from urllib.request import Request, urlopen
import re
from bs4 import BeautifulSoup
from pprint import pprint
import sys
sys.path
# currently works for web.mit.edu/comment-form.html

urls = set()
allemails = set()

req = Request('http://' + sys.argv[1], headers={'User-Agent': 'Mozilla/5.0'})
sitetext = urlopen(req).read()

# sitefile = ur.urlopen('http://' + sys.argv[1])#WORKS
# sitetext = sitefile.read()

soup = BeautifulSoup(sitetext, "lxml")

# ID all urls and push to global variable
for each in soup.find_all("a"):
    link = each.attrs["href"] if "href" in each.attrs else ''
    print (link)
    if link.startswith('http'):
        urls.add(link)

# cycle thru urls, ID emails and push to global variable
for link in urls:
    pattern = re.compile(b"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4}", re.IGNORECASE)

    req = Request(link, headers={'User-Agent': 'Mozilla/5.0'})
    sitetext = urlopen(req).read()
    emails = re.findall(pattern,sitetext)

    for subemail in emails:
        allemails.add(subemail)


# pprint (allemails)
