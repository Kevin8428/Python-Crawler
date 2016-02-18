import urllib.request as ur
import re
from bs4 import BeautifulSoup
urls = set()
allemails = set()


pattern = re.compile(b"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4}", re.IGNORECASE)
sitefile = ur.urlopen("http://web.mit.edu/comment-form.html")
site_base = ur.urlopen("http://mit.edu")
sitetext = sitefile.read()
emails = re.findall(pattern,sitetext)
soup = BeautifulSoup(sitetext, "lxml")


for anchor in soup.find_all("a"):
    link = anchor.attrs["href"] if "href" in anchor.attrs else ''
    if link.startswith('http'):
        urls.add(link)

for link in urls:
    pattern = re.compile(b"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4}", re.IGNORECASE)
    sitefile = ur.urlopen(link)
    sitetext = sitefile.read()
    emails = re.findall(pattern,sitetext)
    # print(emails)

    for subemail in emails:
        allemails.add(subemail)
        # print(subemail)
    # allemails.add(emails)
    # print(link)

print (allemails)
# print (sitetext)
# print (urls)
# print (soup)
