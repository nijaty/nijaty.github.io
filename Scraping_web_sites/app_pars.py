import requests
from bs4 import BeautifulSoup

r = requests.get("https://www.infocenter.gov.az/page/voters/?s=1&sm=1")
c = r.content

soup = BeautifulSoup(c, "html.parser")
all_l = soup.find_all("div", {"id": "conright"})
# print(all_l)
print(all_l[0].find_all("td").txt)
