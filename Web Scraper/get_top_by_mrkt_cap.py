import requests
from bs4 import BeautifulSoup
from threading import Thread


url = 'https://www.corporateinformation.com/Top-100.aspx?topcase=b'
response = requests.get(url).text
soup = BeautifulSoup(response, 'html.parser')
# URLs of pages related to top100 stocks on corporateinformation.com
list_of_names = [name.text.strip().replace('.', '') for name in soup.find_all('a')][22:-9]
list_of_names = [name.replace('Incorporation', 'Inc') if 'Incorporation' in name else name for name in list_of_names]

list_of_symbols = []
def find_symbol(name):
    url_response = requests.get(
        'https://www.marketwatch.com/tools/quotes/lookup.asp?siteID=mktw&Lookup='+name.replace(' ', '+')+'&Country=all&Type=All').text
    url_soup = BeautifulSoup(url_response, 'html.parser')
    try:
        symbol = url_soup.find('td').text
        list_of_names[list_of_names.index(name)] = symbol
    except AttributeError:
        pass

    

threads = []
for name in list_of_names:
    thread = Thread(target=find_symbol, args=(name,))
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()

# Removing symbols of stocks that are not trading on US stock market
list_of_names = [sym if sym.upper() == sym else '' for sym in list_of_names]
list_of_symbols = list(filter(None, list_of_names))