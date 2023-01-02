import matplotlib.pyplot as plt
import numpy as np
path1="infection.txt"
path2="vaccinated.txt"
k=0
GEN=[0]
IN=[0]
VAC=[0]
with open(path1,'r') as att:
    for r in att:
        row = r.split('\n')
        row=row[0].split(' ')
        GEN.append(int(row[0]))
        IN.append(int(row[1]))
        VAC.append(int(row[2]))

X=[i for i in range(len(VAC))]  
Y=[GEN,IN]

col=["blue","red", "green"]
lab=["Recovered","Confirmed", "Vaccination"]

plt.figure(figsize=(20,15))
for i in range(len(Y)):
    plt.plot(X, Y[i], label = lab[i],color=col[i])
plt.title("Covid-19", fontsize = 25)
plt.xlabel("Time t", fontsize = 25)
plt.ylabel("Number of cells", fontsize = 25)
plt.legend(fontsize = 25)
plt.yticks(fontsize=20)
plt.xticks(fontsize=20)
plt.savefig("GIV.png")
plt.show()
plt.clf()

for i in range(len(Y)):
    plt.figure(figsize=(20,15))
    plt.plot(X, Y[i], label = lab[i],color=col[i])
    plt.title("Covid-19", fontsize = 25)
    plt.xlabel("Time t", fontsize = 25)
    plt.ylabel("Number of cells", fontsize = 25)
    plt.legend(fontsize = 25)
    plt.legend(fontsize = 25)
    plt.yticks(fontsize=20)
    plt.xticks(fontsize=20)
    plt.savefig(lab[i]+".png")
    plt.show()
    plt.clf()

z=[]
for i in range(len(IN)):
    z.append(int(IN[i]-GEN[i]))
plt.plot(X, z,color="red")
plt.title("Covid-19", fontsize = 25)
plt.xlabel("Time t", fontsize = 25)
plt.ylabel("Number of cells", fontsize = 25)
plt.legend(fontsize = 7)
plt.yticks(fontsize=5)
plt.xticks(fontsize=5)
plt.savefig("wave.png")
plt.show()
plt.clf()
    