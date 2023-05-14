import csv
import matplotlib.pyplot as plt
def main():
    f1 = open('전국.csv',encoding='cp949')
    f2 = open('서울.csv',encoding='cp949')
    f3 = open('대전.csv',encoding='cp949')
    f4 = open('부산.csv',encoding='cp949')
    f5 = open('제주.csv',encoding='cp949')
    data1 = csv.reader(f1)
    data2 = csv.reader(f2)
    data3 = csv.reader(f3)
    data4 = csv.reader(f4)
    data5 = csv.reader(f5)
    next(data1)
    next(data2)
    next(data3)
    next(data4)
    next(data5)
    x_data=[1,2,3,4,5,6,7,8,9,10,11,12]
    avg_1 = getdata(data1)
    avg_2 = getdata(data2)
    avg_3 = getdata(data3)
    avg_4 = getdata(data4)
    avg_5 = getdata(data5)
    
    plt.title('2022 Average Temperature by Month')
    plt.xlabel("month")
    plt.ylabel("temperature")
    plt.plot(x_data,avg_1,color='black',label = "south_korea")
    plt.plot(x_data,avg_2,'g',label = "seoul(108)")
    plt.plot(x_data,avg_3,'b',label = "daejeon")
    plt.plot(x_data,avg_4,'c',label = "busan")
    plt.plot(x_data,avg_5,'r',label = "jeju")
    plt.xticks(x_data)
    plt.legend()
    plt.show()
    
    korea = getavg(avg_1)

    print("***전국과 평균 온도 차이 ***")
    print("서울 : %.2f"%(korea-getavg(avg_2)))
    print("대전 : %.2f"%(korea-getavg(avg_3)))
    print("부산 : %.2f"%(korea-getavg(avg_4)))
    print("제주 : %.2f"%(korea-getavg(avg_5)))
    
    korea = gethigh(avg_1)
    print("***전국과 최고 온도 차이 ***")
    print("전국 평균 최고 기온 : %.2f"%(korea))
    print("서울 : %.2f"%(korea-gethigh(avg_2)))
    print("대전 : %.2f"%(korea-gethigh(avg_3)))
    print("부산 : %.2f"%(korea-gethigh(avg_4)))
    print("제주 : %.2f"%(korea-gethigh(avg_5)))

    korea = getlow(avg_1)
    print("***전국과 최저 온도 차이 ***")
    print("전국 평균 최저 기온 : %.2f"%(korea))
    print("서울 : %.2f"%(korea-getlow(avg_2)))
    print("대전 : %.2f"%(korea-getlow(avg_3)))
    print("부산 : %.2f"%(korea-getlow(avg_4)))
    print("제주 : %.2f"%(korea-getlow(avg_5)))


    f1.close()
    f2.close()
    f3.close()
    f4.close()
    f5.close()

def getdata(data):
    arr = []
    for row in data:
        if(row[2]!=''):
            arr.append(float(row[2]))
    return arr
def getavg(data):
    count=0
    avg=0.0
    for row in data:
        avg+=row
        count+=1
    avg = avg/count
    return avg
def gethigh(data):
    max=-99999
    for i in data:
        if (i > max):
            max = i
    return max

def getlow(data):
    min=99999
    for i in data:
        if (i < min):
            min = i
    return min
if __name__=="__main__":
    main()