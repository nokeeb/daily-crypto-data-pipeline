from transform import transform_data
data=transform_data()
def save_to_csv(data,filename):
    fhand=open(filename,'w')
    
    
    fhand.write('Name, Symbol, Current price, Market cap, Total volume, Price to volume ratio\n')
    for line in data:
        name=line['name']
        symbol=line['symbol']
        current_price=line['current_price']
        market_cap=line['market_cap']
        total_volume=line['total_volume']
        price_to_volume_ratio=line['price_to_volume_ratio']
        fhand.write(f'{name},{symbol},{current_price},{market_cap},{total_volume},{price_to_volume_ratio}\n')
save_to_csv(data,'test.csv')
    
