import numpy as np
import pandas
import matplotlib.pyplot as plt
from scipy.stats import entropy
import random
from statistics import mean

def myent(x):
    _, counts = np.unique(x, return_counts=True)
    return entropy(counts)/ np.log2(len(x))

i = 1
l1 = []
l3 = []

e1 = []
e3 = []

while(i<16):
    csvFile = pandas.read_csv('./dataneeded/Participant_'+str(i)+'.csv',usecols=["Choice","Time Condition"])
    data_list = csvFile.T.values.tolist()
    
    rep_resp_unlim = 0
    rep_resp_lim400 = 0
    rep_resp_lim800 = 0
    
    j = 0
    while (j<320):
        if(data_list[1][j] == 'Unlimited Time'):
            l3.append(data_list[0][j])
        elif(data_list[1][j] == 'Limited Time'):
            l1.append(data_list[0][j])
        j = j + 1
        
    e1.append(myent(l1))
    e3.append(myent(l3))
    i = i + 1


fig, axs = plt.subplots(figsize=(8, 6))

lis = e1+e3
lis2 = []
colors = []
for i in range(len(lis)):
    if(i<len(lis)/2):
        lis2.append('Limited Time')
        colors.append('khaki')
    else:
        lis2.append('Unlimited Time')
        colors.append('palegreen')

ran = []
for i in range(320):
    ran.append(random.choice(['q','w','o','p']))

plt.axhline(y = myent(ran), color = 'black',linestyle = 'dashed')

axs.scatter(lis2, lis,c=colors)
mx = ['Limited Time','Unlimited Time']
my = [mean(lis[:len(lis)//2]),mean(lis[len(lis)//2:])]
axs.scatter(mx,my,marker = 'X',color = 'black')
axs.set_title('Entropy')

plt.savefig('Figure2b.png')


