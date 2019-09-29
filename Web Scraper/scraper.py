import requests
import time
from get_top_by_mrkt_cap import list_of_symbols


url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/market/get-quotes"


querystring = {"region": "US", "lang": "en",
               "symbols": ','.join(list_of_symbols)}

headers = {
    'x-rapidapi-host': "apidojo-yahoo-finance-v1.p.rapidapi.com",
    'x-rapidapi-key': "8e70861f23msh9d643224683934ap198ea5jsnd38b026de709"
}

start = time.time()
response = requests.request(
    "GET", url, headers=headers, params=querystring).json()
response = response.get('quoteResponse')['result']

i = 0
for result in response:
    try:
        name, symbol, price, prev_close, volume = (
            result['longName'], result['symbol'], result['regularMarketPrice'],
            result['regularMarketPreviousClose'], result['regularMarketVolume'])

        print('Name: ', name, ' Symbol: ', symbol, ' Price: ',
              price, ' Close: ', prev_close, ' Volume: ', volume)
        i += 1
    except:
        pass
print('Response time: ', time.time()-start, 'seconds.')
