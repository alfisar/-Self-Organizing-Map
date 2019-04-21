from numpy import *
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

    for i in range(10):
        hasil = math.sqrt(((x[0]-n[i][0])**2) + ((x[1]-n[i][1])**2))
        # print(hasil)
        if (hasil < sigma) :
            tempsn.append([i,hasil])

    return tempsn

# Menghitung Tn 
def hitungtn(x):
    temptn = []
    for i in range(len(x)):
        temptn.append(double(math.exp(-(x[i][1]**2)/(2*(sigma**2)))))
    return temptn

# Menghitung Wn untuk di tambahkan pada Weight neuronnya 
def hitungwn(x,y):
    temp3 = []
    for j in range(len(y)):
        temp1 = []
        for i in range (2):
            temp1.append(lr*y[j]*(x[i]-n[tempsn[j][0]][i]))
        temp3.append((temp1[0],temp1[1]))
    # print(temp3)
    return temp3

# Menambahkan Wn dengan weight neuronnya
def gantiw(x):
    for i in range(len(x)):
        k = []
        for j in range(2):
            n[tempsn[i][0]][j] = n[tempsn[i][0]][j] + x[i][j]
    return k

def takeSecond1(elem):
    return elem[0]

f = open("Tugas 2 ML Genap_2018-2019_Dataset_Tanpa_Label.csv","r")
reader = csv.reader(f)

lis1,n,tetangga = [],[],[]
for d in reader:
    lis1.append((float(d[0]),float(d[1])))

# Membangkitakan 4 neuron dengan weightnya di random dan tetangganya di tentukan sendiri
for i in range(10):
    n.append([random.uniform(-15,15),random.uniform(-15,15)])
print('n awal')
print(n)

sigma0 = 2
t0 = 2
lr0 = 0.1
tn = 2

sigma,lr = 0,0

# Perulangan untuk iterasi
for a in range(50):
    sigma = sigma0 * math.exp(-(a+1)/t0)
    # print(sigma)
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
        # print('tn')
        # print(temptn)
        temp1 = hitungwn(lis1[j],temptn)
        # print('wn')
        # print(temp1)
        k = gantiw(temp1)
print('n akhir')    
print(n)

coba = []

# Perulangan untuk setiap data
for j in range(len(lis1)):
    tempjar = []
        # Perulangan untuk setiap neuron dan mencari jarak terdekat untuk data tersebut
    for i in range (len(n)):
        tempjar.append((jarak(lis1[j],n[i]),i))
        tempjar.sort(key=takeSecond1)
    
    coba.append([tempjar[0][1],lis1[j][0],lis1[j][1]])

# print(coba)

data1,data2 = [],[]
j = 0
for i in (coba):
    if (i[0] == 0):
        plt.scatter(i[1], i[2], c ='purple', alpha=1)
    elif (i[0] == 1):
        plt.scatter(i[1], i[2], c ='g', alpha=1)
    elif (i[0] == 2):
        plt.scatter(i[1], i[2], c ='b', alpha=1)
    elif (i[0] == 3):
        plt.scatter(i[1], i[2], c ='black', alpha=1)
    elif (i[0] == 4):
        plt.scatter(i[1], i[2], c ='pink', alpha=1)
    elif (i[0] == 5):
        plt.scatter(i[1], i[2], c ='red', alpha=1)
    elif (i[0] == 6):
        plt.scatter(i[1], i[2], c ='c', alpha=1)
    elif (i[0] == 7):
        plt.scatter(i[1], i[2], c ='brown', alpha=1)
    elif (i[0] == 8):
        plt.scatter(i[1], i[2], c ='yellow', alpha=1)
    elif (i[0] == 9):
        plt.scatter(i[1], i[2], c ='orange', alpha=1)
plt.title('Scatter plot SOM')
plt.xlabel('x')
plt.ylabel('y')
plt.show()

