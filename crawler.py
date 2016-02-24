import urllib.request as ur
from urllib.request import Request, urlopen
import re
from bs4 import BeautifulSoup
from pprint import pprint
import sys
sys.path
# currently works for web.mit.edu/comment-form.html

urls = set()
urlsupdate = set()
allemails = set()

req = Request('http://' + sys.argv[1], headers={'User-Agent': 'Mozilla/44.0.2'})
sitetext = urlopen(req).read()


soup = BeautifulSoup(sitetext, "lxml")

# ID all urls and push to global variable
for each in soup.find_all("a"):
    link = each.attrs["href"] if "href" in each.attrs else ''
    if 'http' not in link:
        link = ('http://' + sys.argv[1]+ link)
    urls.add(link)
    # print(link)


for each in urls:
    start = ('http://' + sys.argv[1])
    if start in each:
        urlsupdate.add(each)

# cycle thru urls, ID emails and push to global variable
for link in urlsupdate:
    try:
        pattern = re.compile(b"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4}", re.IGNORECASE)
        req = Request(link, headers={'User-Agent': 'Mozilla/44.0.2'})
        sitetext = urlopen(req).read()
        emails = re.findall(pattern,sitetext)
        for subemail in emails:
            allemails.add(subemail)
    except:
        pass

pprint (allemails)
# pprint (urlsupdate)
