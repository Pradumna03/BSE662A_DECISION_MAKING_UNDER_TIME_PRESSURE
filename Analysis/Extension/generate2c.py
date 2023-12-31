import pandas
import matplotlib.pyplot as plt
from statistics import mean

i = 1
l1 = []
l2 = []
l3 = []

while(i<16):
    csvFile = pandas.read_csv('./dataneeded/Participant_'+str(i)+'.csv',usecols=["Choice","Reward (Health Points)","Time Condition","Payoff Condition"])
    data_list = csvFile.T.values.tolist()
    
    rep_resp_unlim = 0
    rep_resp_lim400 = 0
    rep_resp_lim800 = 0
    
    j = 0
    while (j<480):
        if (data_list[0][j] == data_list[0][j-1]):
            if(data_list[2][j-1] == 'Unlimited Time'):
                rep_resp_unlim = rep_resp_unlim + 1
            elif(data_list[2][j-1] == 'Limited Time - 800ms'):
                rep_resp_lim800 = rep_resp_lim800 + 1
            elif(data_list[2][j-1] == 'Limited Time - 400ms'):
                rep_resp_lim400 = rep_resp_lim400 + 1
        j = j + 1
        
    l1.append(rep_resp_lim400/160)
    l2.append(rep_resp_lim800/160)
    l3.append(rep_resp_unlim/160)
    i = i + 1


fig, axs = plt.subplots(figsize=(8, 6))

lis = l1+l2+l3
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

axs.scatter(lis2, lis,c=colors)
mx = ['Limited Time - 400ms','Limited Time - 800ms','Unlimited Time']
my = [mean(lis[:len(lis)//3]),mean(lis[len(lis)//3:(2*len(lis))//3]),mean(lis[(2*len(lis))//3:])]
axs.scatter(mx,my,marker = 'X',color = 'black')
axs.set_title('Repeat Clicks')

plt.savefig('Figure2c.png')


