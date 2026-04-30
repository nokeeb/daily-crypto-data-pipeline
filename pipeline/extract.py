import urllib.error,urllib.parse,urllib.request
import json
def fetch_crypto_data():
    url='https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=20&page=1'
    rawData=urllib.request.urlopen(url)
    data=rawData.read().decode()
    dzejson=json.loads(data)
    return dzejson
