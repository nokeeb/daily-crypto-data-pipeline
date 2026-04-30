from extract import fetch_crypto_data
coinsInfo=fetch_crypto_data()
coinList=list()
def transform_data():
    for coinInfo in coinsInfo:
        coin=dict()
        coin['name']=coinInfo['name']
        coin['symbol']=coinInfo['symbol']
        coin['current_price']=coinInfo['current_price']
        coin['market_cap']=coinInfo['market_cap']
        coin['total_volume']=coinInfo['total_volume']
        price_to_volume=coin['current_price']/coin['total_volume']
        
        coin['price_to_volume_ratio']=price_to_volume
        coinList.append(coin)
    return coinList



