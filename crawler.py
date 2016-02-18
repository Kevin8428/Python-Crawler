import urllib.request as ur
import re
#BeautifulSoup --needs to be installed on user computer
from bs4 import BeautifulSoup
urls = set()


pattern = re.compile(b"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4}", re.IGNORECASE)
sitefile = ur.urlopen("http://web.mit.edu/comment-form.html")
site_base = ur.urlopen("http://web.mit.edu")
sitetext = sitefile.read()
emails = re.findall(pattern,sitetext)
soup = BeautifulSoup(sitetext, "lxml")


for anchor in soup.find_all("a"):

    # extract link url from the anchor
    link = anchor.attrs["href"] if "href" in anchor.attrs else ''
    # print(link)
    # resolve relative links
    if link.startswith('http'):
        urls.add(link)
        # print(link)





# print (emails)
# print (sitetext)
print (urls)
# print (soup)
