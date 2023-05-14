import csv
import matplotlib.pyplot as plt
def main():
    f1 = open('2022.csv',encoding='cp949')
    f2 = open('2012.csv',encoding='cp949')
    f3 = open('2000.csv',encoding='utf-8')
   
    data1 = csv.reader(f1)
    data2 = csv.reader(f2)
    data3 = csv.reader(f3)

    man = []
    woman = []
    for row in data3:
        row[2]=int(row[2])
        row[3]=int(row[3])
        man.append(row[2])
        woman.append(row[3])
    for row in data2:
        row[3]=int(row[3])
        row[4]=int(row[4])
        man.append(row[3])
        woman.append(row[4])
    for row in data1:
        row[3]=int(row[3])
        row[4]=int(row[4])
        man.append(row[3])
        woman.append(row[4])
    
    
    
    x_data = [2000,2012,2022]
    plt.title('Jeju Gender Ratio')
    plt.xlabel("year")
    plt.ylabel("Gender Ratio")
    plt.plot(x_data,man,color='b',label = "man")
    plt.plot(x_data,woman,color='r',label = "woman")
    plt.xticks(x_data)
    plt.legend()
    plt.show()
    
    f1.close()
    f2.close()
    f3.close()

if __name__=="__main__":
    main()