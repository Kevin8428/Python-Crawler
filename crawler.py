# access and make requests
import urllib.request as ur
# regex
import re

# string
# stringforregex = '<a\s+href=\"mailto:([a-zA-z0-9._@]*)\">"'

# convert string to be converted by regex library

pattern = re.compile(b"<a\s+href=\"mailto:([a-zA-Z0-9._@]*)\">", re.IGNORECASE)

sitefile = ur.urlopen("http://jana.com/contact")
sitetext = sitefile.read()
emails = re.findall(pattern,sitetext)
# emails = re.findall(b"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4}",sitetext)

title = re.findall(b"<title>(.+?)</title>",sitetext)

# print (emails)
# print (sitetext)
print (title)
