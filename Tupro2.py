import numpy
import csv
import random
import math

def jarak(x,n):
    temp = 0 
    temp = math.sqrt(((x[0]-n[0])**2) + ((x[1]-n[1])**2)) 
    return temp

def hitungsn(x):
    tempsn = []
    j = 2 
    for i in range(3): 
        tempsn.append(math.sqrt(((x[0]-n[x[j]][0])**2) + ((x[1]-n[x[j]][1])**2)))
        j+=1
    return tempsn

def hitungtn(x):
    temptn = []
    for i in range(3):
        temptn.append(math.exp(-(x[i]**2)/8))
    return temptn

def hitungwn(x,y):
    temp3,temptetangga = [],[]
    l = tempjar[0][1]
    j = 2
    for i in range(3):
        temptetangga.append(n[l][j])
        j+=1

    for j in range(3):
        temp1 = []
        for i in range (2):
            temp1.append(str(0.1*y[j]*(x[i]-n[temptetangga[j]][i])))
        temp3.append((temp1[0],temp1[1]))
    # print(temp3)
    return temp3

def gantiw(x):
    temptetangga= []
    l = tempjar[0][1]
    j = 2
    for i in range(3):
        temptetangga.append(n[l][j])
        j+=1
    # print("tetangga")
    # print(temptetangga)
    # print(x)
    for i in range(len(x)):
        k = []
        for j in range(2):
            n[temptetangga[i]][j] = n[temptetangga[i]][j] + float(x[i][j][:10])
    return k

def takeSecond1(elem):
    return elem[0]

f = open("Tugas 2 ML Genap_2018-2019_Dataset_Tanpa_Label.csv","r")
reader = csv.reader(f)
# next(reader)

lis1,n = [],[]
for d in reader:
    lis1.append((float(d[0]),float(d[1])))

n.append([random.uniform(-15,15),random.uniform(-15,15),0,1,2])
n.append([random.uniform(-15,15),random.uniform(-15,15),1,0,3])
n.append([random.uniform(-15,15),random.uniform(-15,15),2,0,3])
n.append([random.uniform(-15,15),random.uniform(-15,15),3,1,2])

print(n)
# for j in range (1):
# for lis in range(100):

for a in range(10):
    for j in range(len(lis1)):
        tempjar = []
        for i in range (len(n)):
            tempjar.append((jarak(lis1[j],n[i]),i))
            tempjar.sort(key=takeSecond1)
        tempsn = hitungsn(n[tempjar[0][1]])
        # print(tempsn)
        temptn = hitungtn(tempsn)
        # print(temptn)
        temp1 = hitungwn(lis1[j],temptn)
        k = gantiw(temp1)
print(n)

