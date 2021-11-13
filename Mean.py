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
total=0
for a in data_list:
   total=total+a
mean=total/n 
print("MEAN IS",mean)