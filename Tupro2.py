import numpy
import csv
import random
import math
import matplotlib.pyplot as plt

# Menghitung Jarak terdekat dari data ke neuron
def jarak(x,n):
    temp = 0 
    temp = math.sqrt(((x[0]-n[0])**2) + ((x[1]-n[1])**2)) 
    return temp

# Menghitung jarak neuron pemenang terhadap 2 tetangganya
def hitungsn(x):
    tempsn = []
    j = 2 
    for i in range(3): 
        tempsn.append(math.sqrt(((x[0]-n[x[j]][0])**2) + ((x[1]-n[x[j]][1])**2)))
        j+=1
    return tempsn

# Menghitung Tn 
def hitungtn(x):
    temptn = []
    for i in range(3):
        temptn.append(math.exp(-(x[i]**2)/(2*(sigma**2))))
    return temptn

# Menghitung Wn untuk di tambahkan pada Weight neuronnya 
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
            temp1.append(str(lr*y[j]*(x[i]-n[temptetangga[j]][i])))
        temp3.append((temp1[0],temp1[1]))
    # print(temp3)
    return temp3

# Menambahkan Wn dengan weight neuronnya
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
            n[temptetangga[i]][j] = n[temptetangga[i]][j] + float(x[i][j][:3])
    return k

def takeSecond1(elem):
    return elem[0]

f = open("Tugas 2 ML Genap_2018-2019_Dataset_Tanpa_Label.csv","r")
reader = csv.reader(f)

lis1,n = [],[]
for d in reader:
    lis1.append((float(d[0]),float(d[1])))

# Membangkitakan 4 neuron dengan weightnya di random dan tetangganya di tentukan sendiri
n.append([random.uniform(-20,20),random.uniform(-20,20),0,1,2])
n.append([random.uniform(-20,20),random.uniform(-20,20),1,0,3])
n.append([random.uniform(-20,20),random.uniform(-20,20),2,0,3])
n.append([random.uniform(-20,20),random.uniform(-20,20),3,1,2])

print(n)

sigma0 = 2
t0 = 2
lr0 = 0.1
tn = 2

sigma,lr = 0,0

# Perulangan untuk iterasi
for a in range(5):
    sigma = sigma0 * math.exp(-(a+1)/t0)
    lr = lr0 * math.exp(-(a+1)/tn)
    # Perulangan untuk setiap data
    for j in range(len(lis1)):
        tempjar = []
        # Perulangan untuk setiap neuron dan mencari jarak terdekat untuk data tersebut
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

hasil_final,n0_1,n0_2,n1_1,n1_2,n2_1,n2_2,n3_1,n3_2 = [],[],[],[],[],[],[],[],[]

# Perulangan untuk setiap data
for j in range(len(lis1)):
    tempjar = []
        # Perulangan untuk setiap neuron dan mencari jarak terdekat untuk data tersebut
    for i in range (len(n)):
        tempjar.append((jarak(lis1[j],n[i]),i))
        tempjar.sort(key=takeSecond1)
    
    if tempjar[0][1] == 0:
        n0_1.append(lis1[j][0])
        n0_2.append(lis1[j][1])
    elif tempjar[0][1] == 1:
        n1_1.append(lis1[j][0])
        n1_2.append(lis1[j][1]) 
    elif tempjar[0][1] == 2:
        n2_1.append(lis1[j][0])
        n2_2.append(lis1[j][1])
    elif tempjar[0][1] == 3:
        n3_1.append(lis1[j][0])
        n3_2.append(lis1[j][1])   

# print(hasil_final[1])

data1,data2 = [],[]
j = 0
for i in (lis1):
    j+=1
    data1.append(i[0])
    data2.append(i[1])

plt.scatter(n0_1, n0_2, c ='purple', alpha=1)
plt.scatter(n1_1, n1_2, c ='g', alpha=1)
plt.scatter(n2_1, n2_2, c ='b', alpha=1)
plt.scatter(n3_1, n3_2, c ='c', alpha=1)
plt.scatter(n[0][0], n[0][1], marker = 'x', label = 0, c='purple', alpha=1)
plt.scatter(n[1][0], n[1][1], marker = '^', c='g', alpha=1)
plt.scatter(n[2][0], n[2][1], marker = '*', c='b', alpha=1)
plt.scatter(n[3][0], n[3][1], marker = 's', c='c', alpha=1)
plt.title('Scatter plot SOM')
plt.xlabel('x')
plt.ylabel('y')
plt.show()

