import urllib.error,urllib.parse,urllib.request
import json
def fetch_crypto_data():
    url='https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=20&page=1'
    try:
        with urllib.request.urlopen(url,timeout=10) as response:
            return json.loads(response.read())
    except urllib.error.URLError:
        print('Network/API error')
        return[]
    except json.JSONDecodeError:
        print('Invalid JSON response')
        return[]

    # rawData=urllib.request.urlopen(url)
    # data=rawData.read().decode()
    # jsonApiData=json.loads(data)
    # return jsonApiData
     