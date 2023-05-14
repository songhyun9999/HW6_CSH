import csv
import matplotlib.pyplot as plt
from random import randrange
import pandas as pd
def main():
    rnum = []
    for i in range (100):
        x = randrange(1,7,1)
        rnum.append(x)
    
    for i in range (1000):
        x = randrange(1,7,1)
        rnum.append(x)
    for i in range (10000):
        x = randrange(1,7,1)
        rnum.append(x)
    for i in range (100000):
        x = randrange(1,7,1)
        rnum.append(x)

    df = pd.DataFrame({'data':rnum})
    df.to_csv('random.csv',index=False,encoding='cp949')

    f=open('random.csv',encoding='cp949')
    num = []
    data = csv.reader(f)
    next(data)
    count=0
    for row in data:
        row[0] = int(row[0])
        num.append(row[0])
        count+=1
        if(count>=100):
            break
    plt.title('100 tries')
    plt.xlabel("dice number")
    plt.ylabel("total count")
    plt.hist(num,color='red',bins=6,density=True)
    plt.legend()
    plt.show()
    num = []
    count=0
    for row in data:
        row[0] = int(row[0])
        num.append(row[0])
        count+=1
        if(count>=1000):
            break
    plt.title('1000 tries')
    plt.xlabel("dice number")
    plt.ylabel("total count")
    plt.hist(num,color='red',bins=6,density=True)
    plt.legend()
    plt.show()
    num = []
    count=0
    for row in data:
        row[0] = int(row[0])
        num.append(row[0])
        count+=1
        if(count>=10000):
            break
    plt.title('10000 tries')
    plt.xlabel("dice number")
    plt.ylabel("total count")
    plt.hist(num,color='red',bins=6,density=True)
    plt.legend()
    plt.show()
    num = []
    count=0
    for row in data:
        row[0] = int(row[0])
        num.append(row[0])
        count+=1
        if(count>=100000):
            break
    plt.title('100000 tries')
    plt.xlabel("dice number")
    plt.ylabel("total count")
    plt.hist(num,color='red',bins=6,density=True)
    plt.legend()
    plt.show()

if __name__=="__main__":
    main()