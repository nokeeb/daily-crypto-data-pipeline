def transform_data(data):
    coins_info=data
    coin_list=list()
    for coin_info in coins_info:
        coin=dict()
        coin['name']=coin_info['name']
        coin['symbol']=coin_info['symbol']
        coin['current_price']=coin_info['current_price']
        coin['market_cap']=coin_info['market_cap']
        coin['total_volume']=coin_info['total_volume']
        if(coin['total_volume']==0):
            price_to_volume=0
        else:
            price_to_volume=coin['current_price']/coin['total_volume']
        
        coin['price_to_volume_ratio']=price_to_volume
        coin_list.append(coin)
    return coin_list



