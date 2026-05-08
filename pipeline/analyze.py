
def analyze_data(filename):
    fhand=open(filename)
    sum=0
    count=0
    averagePrice=0
    biggestCapCoin=None
    currentBiggestCap=0
    currentLowestVolume=0
    lowestVolumeCoin=None
    temp=dict()
    pravaLista=None
    for line in fhand:
        if line.startswith('Name'):
           continue 
        else:
            fixedLine=line.rstrip()
            coinData=fixedLine.split(',')
            cap=int(coinData[3])
            if(cap>currentBiggestCap):
                currentBiggestCap=cap
                biggestCapCoin=coinData[0]
            volume=float(coinData[4])
            if(currentLowestVolume==0):
                currentLowestVolume=volume
            if(volume<currentLowestVolume):
                currentLowestVolume=volume
                lowestVolumeCoin=coinData[0]
            sum+=float(coinData[2])
            count+=1
            if coinData[0] not in temp:
                temp[float(coinData[5])]=coinData[0]
            
    averagePrice=sum/count
    pravaLista=sorted(temp.items(),reverse=True)
    firstBest=pravaLista[0]
    secondBest=pravaLista[1]
    thirdBest=pravaLista[2]
    data=list()
    data.append(averagePrice)
    data.append(biggestCapCoin)
    data.append(lowestVolumeCoin)
   
    top3=list()
    top3.append(firstBest)
    top3.append(secondBest)
    top3.append(thirdBest)
    data.append(top3)
    print(data)



   
    
        


analyze_data('test.csv')