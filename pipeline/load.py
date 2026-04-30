from transform import transform_data
def save_to_csv(data,filename):
    fhand=open(filename,'w')
    fhand.write('Name, Symbol, Current price, Market cap, Total volume, Price to volume ratio')
    data=transform_data()
    for line in data:
        fhand.write('{line['name']}')


    
