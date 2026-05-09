import datetime
date_micro=datetime.datetime.now()
date=date_micro.replace(microsecond=0)
def create_report(data):
    with open('report.txt','w',encoding='utf-8') as file:
        top3=data['top3']    
        file.write(f'''Crypto Report - {date}
                
Average Price: {data['average_price']}
Top Market Cap: {data['biggest_cap_coin']}
Lowest Volume: {data['lowest_volume_coin']}
Top 3 by Ratio:
1.{top3[0][1]} - {top3[0][0]}
2.{top3[1][1]} - {top3[1][0]}
3.{top3[2][1]} - {top3[2][0]}''')
    