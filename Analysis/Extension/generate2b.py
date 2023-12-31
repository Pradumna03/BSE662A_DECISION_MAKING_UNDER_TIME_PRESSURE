import numpy as np
import pandas
import matplotlib.pyplot as plt
from scipy.stats import entropy
import random
from statistics import mean

def myent(x):
    _, counts = np.unique(x, return_counts=True)
    return entropy(counts, base=2)/ np.log2(len(x))

i = 1
l1 = []
l2 = []
l3 = []

e1 = []
e2 = []
e3 = []

while(i<16):
    csvFile = pandas.read_csv('./dataneeded/Participant_'+str(i)+'.csv',usecols=["Choice","Time Condition"])
    data_list = csvFile.T.values.tolist()
    
    rep_resp_unlim = 0
    rep_resp_lim400 = 0
    rep_resp_lim800 = 0
    
    j = 0
    while (j<480):
        if(data_list[1][j] == 'Unlimited Time'):
            l3.append(data_list[0][j])
        elif(data_list[1][j] == 'Limited Time - 800ms'):
            l2.append(data_list[0][j])
        elif(data_list[1][j] == 'Limited Time - 400ms'):
            l1.append(data_list[0][j])
        j = j + 1
        
    e1.append(myent(l1))
    e2.append(myent(l2))
    e3.append(myent(l3))
    i = i + 1


fig, axs = plt.subplots(figsize=(8, 6))

lis = e1+e2+e3
lis2 = []
colors = []
for i in range(len(lis)):
    if(i<len(lis)/3):
        lis2.append('Limited Time - 400ms')
        colors.append('khaki')
    elif(i<2*len(lis)/3):
        lis2.append('Limited Time - 800ms')
        colors.append('skyblue')
    else:
        lis2.append('Unlimited Time')
        colors.append('palegreen')

ran = []
for i in range(480):
    ran.append(random.choice(['q','w','o','p']))

plt.axhline(y = myent(ran), color = 'black',linestyle = 'dashed')

axs.scatter(lis2, lis,c=colors)
mx = ['Limited Time - 400ms','Limited Time - 800ms','Unlimited Time']
my = [mean(lis[:len(lis)//3]),mean(lis[len(lis)//3:(2*len(lis))//3]),mean(lis[(2*len(lis))//3:])]
axs.scatter(mx,my,marker = 'X',color = 'black')
axs.set_title('Entropy')

plt.savefig('Figure2b.png')


