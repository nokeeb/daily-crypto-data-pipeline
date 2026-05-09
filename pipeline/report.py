import datetime
datum=datetime.date.today()
def create_report(data):
    fhand=open('report.txt','w')
    top3=data[3]
    fhand.write(f'''Crypto Report - {datum}
Average Price: {data[0]}
Top Market Cap: {data[1]}
Lowest Volume: {data[2]}
Top 3 by Ratio:
1.{top3[0][1]} - {top3[0][0]}
2.{top3[1][1]} - {top3[1][0]}
3.{top3[2][1]} - {top3[2][0]}''')
    

