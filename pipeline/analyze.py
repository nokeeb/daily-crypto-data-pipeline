
def analyze_data(filename):
    with open(filename,'r',encoding='utf-8') as file:
        total_price=0
        count=0
        average_price=0
        biggest_cap_coin=None
        current_biggest_cap=0
        current_lowest_volume=0
        lowest_volume_coin=None
        temp=dict()
        real_list=None
        for line in file:
            if line.startswith('Name'):
                continue 
            else:
                fixed_line=line.rstrip()
                coin_data=fixed_line.split(',')
                cap=int(coin_data[3])
                if(cap>current_biggest_cap):
                    current_biggest_cap=cap
                    biggest_cap_coin=coin_data[0]
                volume=float(coin_data[4])
                if(current_lowest_volume==0):
                    current_lowest_volume=volume
                if(volume<current_lowest_volume):
                    current_lowest_volume=volume
                    lowest_volume_coin=coin_data[0]
                total_price+=float(coin_data[2])
                count+=1
                if coin_data[0] not in temp:
                    temp[float(coin_data[5])]=coin_data[0]
        if(total_price != 0 and count != 0):       
            average_price=total_price/count
        real_list=sorted(temp.items(),reverse=True)
        first_best=real_list[0]
        second_best=real_list[1]
        third_best=real_list[2]
    
    
        top3=list()
        top3.append(first_best)
        top3.append(second_best)
        top3.append(third_best)
        
        return{
            "average_price":average_price,
            "biggest_cap_coin":biggest_cap_coin,
            "lowest_volume_coin":lowest_volume_coin,
            "top3":top3


        }


   
    
        


