def save_to_csv(data,filename):
    with open(filename,'w',encoding='utf-8') as file:
        file.write('Name, Symbol, Current price, Market cap, Total volume, Price to volume ratio\n')
        for line in data:
            name=line['name']
            symbol=line['symbol']
            current_price=line['current_price']
            market_cap=line['market_cap']
            total_volume=line['total_volume']
            price_to_volume_ratio=line['price_to_volume_ratio']
            file.write(f'{name},{symbol},{current_price},{market_cap},{total_volume},{price_to_volume_ratio}\n')

    
