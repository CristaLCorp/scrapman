import requests
from bs4 import BeautifulSoup as bs
import pandas

# headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:20.0) Gecko/20100101 Firefox/20.0'}
headers = {
           # 'Host': 'detectportal.firefox.com',
           'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:125.0) Gecko/20100101 Firefox/125.0', 
           'Accept': "*/*",
           'Accept-Language': 'en-US,en;q=0.5',
           'Accept-Encoding': 'gzip, deflate, br',
           'Cache-Control': 'no-cache',
           'Pragma': 'no-cache',
           'Connection': 'keep-alive'
           }
# Host: detectportal.firefox.com
# url = "https://fr.wikipedia.org/wiki/France"
# url = "https://www.carrefour.fr/p/pates-torsades-barilla-8076809512268"
url ="https://www.pokepedia.fr/Liste_des_Pok%C3%A9mon_dans_l%27ordre_du_Pok%C3%A9dex_National"

response = requests.get(url, headers=headers, allow_redirects=True, verify=False)
soup = bs(response.content, 'html.parser')
print(soup)
