import csv

with open("height-weight.csv",newline="") as a:
    reader=csv.reader(a)
    new_list=list(reader)
new_list.pop(0)
data_list=[]
for i in range(len(new_list)):
    num=new_list[i][1]
    data_list.append(float(num))

n=len(data_list)
data_list.sort()
if n%2==0:
    median1=float(data_list[n//2])
    median2=float(data_list[n//2+1])
    medianFinal=(median1+median2)/2
else:
    medianFinal=float(data_list[n//2])
print("MEDIAN IS",medianFinal)