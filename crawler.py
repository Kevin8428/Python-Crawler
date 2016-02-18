import urllib.request as ur
import re
from bs4 import BeautifulSoup
from pprint import pprint
urls = set()
allemails = set()

# set page html to variable
sitefile = ur.urlopen("http://web.mit.edu/comment-form.html")
sitetext = sitefile.read()
soup = BeautifulSoup(sitetext, "lxml")

# ID all urls and push to global variable
for anchor in soup.find_all("a"):
    link = anchor.attrs["href"] if "href" in anchor.attrs else ''
    if link.startswith('http'):
        urls.add(link)

# cycle thru urls, ID emails and push to global variable
for link in urls:
    pattern = re.compile(b"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4}", re.IGNORECASE)
    sitefile = ur.urlopen(link)
    sitetext = sitefile.read()
    emails = re.findall(pattern,sitetext)

    for subemail in emails:
        allemails.add(subemail)

pprint (allemails)
# pprint (urls)
