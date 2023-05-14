import csv
import matplotlib.pyplot as plt
def main():
    f = open('subway.csv')
    data = csv.reader(f)
    class subway:
        name = ""
        gin=0
        gout=0
        total=0
        def __init__(self,a,b,c):
            self.name=a
            self.gin =b
            self.gout=c
        def getTotal(self):
            self.total=self.gin + self.gout
    
    sub=[]
    for row in data:
        row[4]=int(row[4])
        row[5]=int(row[5])
        row[6]=int(row[6])
        row[7]=int(row[7])
        tmp = subway(row[3],row[4]+row[6],row[5]+row[7])
        tmp.getTotal()
        sub.append(tmp)

    for i in range(len(sub)-1):
        for j in range(i+1,len(sub)):
            if(sub[i].gin<sub[j].gin):
                tmp = sub[i]
                sub[i]=sub[j]
                sub[j]=tmp
    tmp=[]
    index=[]
    for i in range(30):
        tmp.append(sub[i].gin)
        index.append(sub[i].name)
        
    plt.rc('font',family='Malgun Gothic')
    plt.rcParams['axes.unicode_minus']=False
    plt.title('지하철 승객 수 (승차)')
    plt.xlabel("지하철")
    plt.ylabel("승객수")
    plt.bar(index,tmp,color='pink')
    plt.xticks(index,fontsize=5)
    plt.show()


    for i in range(len(sub)-1):
        for j in range(i+1,len(sub)):
            if(sub[i].gout<sub[j].gout):
                tmp = sub[i]
                sub[i]=sub[j]
                sub[j]=tmp
    tmp=[]
    index=[]
    for i in range(30):
        tmp.append(sub[i].gout)
        index.append(sub[i].name)
        
    plt.rc('font',family='Malgun Gothic')
    plt.rcParams['axes.unicode_minus']=False
    plt.title('지하철 승객 수 (하차)')
    plt.xlabel("지하철")
    plt.ylabel("승객수")
    plt.bar(index,tmp,color='pink')
    plt.xticks(index,fontsize=5)
    plt.show()


    for i in range(len(sub)-1):
        for j in range(i+1,len(sub)):
            if(sub[i].total<sub[j].total):
                tmp = sub[i]
                sub[i]=sub[j]
                sub[j]=tmp
    tmp=[]
    index=[]
    for i in range(30):
        tmp.append(sub[i].total)
        index.append(sub[i].name)
        
    plt.rc('font',family='Malgun Gothic')
    plt.rcParams['axes.unicode_minus']=False
    plt.title('지하철 승객 수 (승하차)')
    plt.xlabel("지하철")
    plt.ylabel("승객수")
    plt.bar(index,tmp,color='pink')
    plt.xticks(index,fontsize=5)
    plt.show()
    
    f.close()


if __name__=="__main__":
    main()