# -*- coding: utf-8 -*-
"""
Tenting Schedule Optimizer

Created on Sat Jan 22 20:05:25 2022

@author: jmann

2 at all times during the day
30 minute windows (except for night)
equalize open windows- close to same time, same number of nights especially

"""
#Starting Info
#%%Packages and starting data
import pandas as pd
import numpy as np
import random as ran

peeps = 4 #Number of tenters
daynum = 2 #Black/Blue = 2, White = 1
nightnum = 1 #Black = 10, Blue = 6, White = 2

dayslots = [0]*peeps
totnights = [0]*peeps

#%% Functions for assignment

# of nights per week = 7*nightnum /peeps
def nights(daylist):
    #randomly assign nights- will need human fixing
    for i in range(len(allthedays)): #for 0 to 7
        fuck = np.array([]) #all indexes of available
        a = list(np.where(allthedays[i][-1] == 0)[0])
        for j in range(len(a)):
            fuck = np.append(fuck,int(a[j]))
        fuck = fuck.astype(int)
        fuck = list(fuck) #if anyone besides me ever reads this, no u didnt :)
        if len(fuck) >= nightnum:
            q = ran.sample(fuck,nightnum) #selects nightnum worth of indexes from var fuck
            for k in q:
                allthedays[i][-1][k] = 1 #should assign these variables 1- occupado
            pass
        else:
            for k in range(len(allthedays[i][-1])):
                if allthedays[i][-1][k] == 0:
                    allthedays[i][-1][k] = 1
                else:
                    allthedays[i][-1][k] = 3
           
            
def dayweights():
    dayweights = [] #VERY IMPORTANT LIST
    zip_object = zip(ogslots, dayslots)
    for ogslots_i, dayslots_i in zip_object:
        dayweights.append(ogslots_i-dayslots_i)
    return dayweights


def weightsample(sequence, weights = None, k = 1):
    fin = [] #won't be an index
    for i in range(k):        
        while len(fin) < k:
            temp = ran.choices(sequence, weights, k = 1)
            if temp not in fin:            
                fin.append(temp)
                continue
    return fin
            
def indexlist(): #puts names with index numbers (str) for input at start of days
    fin = ''
    names = list(df.columns[0:peeps])
    for q in range(peeps):
        fin = fin + '{} = {}, '.format(names[q],q)
    return fin[:-2]+'.'

def inputtolist(string): #str sep by spaces
    a = string.split()
    for i in range(len(a)):
        a[i] = int(a[i])
    return a

def decision(improw): #Piece of trash- completely ignore
    temp = []
    for i in range(len(improw)):
        temp[i] = improw[i]
    if temp.count(0) <= 1:    #everyone's busy condition
        for index, elem in enumerate(temp):
            if elem != 0:
                temp[index] = 3
                #print(f"{item} is found at index {index}")
                
def godown(day, personlist):
    for i in personlist:
        break
        
    

# %% Load and manipulate data
#Load data from excel and create DataFrame
df = pd.read_excel("SampleSchedule.xlsx", index_col=0) #0=available, -1=not

# df.shape gives dimensions

daystartindex = np.arange(0,(peeps+2)*7,peeps+2) #CHANGE THE 2 IF THERE ARE MORE SLOTS BETWEEN
for k in daystartindex:  # Num of collums // tenters = days? 
    #creates variables day1 through day7 :)
    if k == daystartindex[0] or k==daystartindex[-1]:
        globals()['day{}'.format(list(daystartindex).index(k)+1)] = df.iloc[:,k:k+peeps].values  
    else:
        globals()['day{}'.format(list(daystartindex).index(k)+1)] = df.iloc[:-3,k:k+peeps].values
allthedays = [day1,day2,day3,day4,day5,day6,day7] #Error code = stupid
day1,day2,day3,day4,day5,day6,day7 = allthedays #Extremely not legit code, but fixes vars

#%%Start doin shit
"""
desired outcome- For each slot,
    When there are two people available- assign those two until end
    When there are more than two spaces available- select two and put them on until shift end
        Selection is random at first, then based on whoever has least hours

"""
#weighted probability
#%% Turning 0s into 1s

#%%NIGHTS
nights(allthedays)
#%%%DAYS

slotspp = (2*(len(day1)-1)+5*(len(day2)-1)*peeps*(daynum/peeps))/peeps
ogslots = [slotspp]*peeps #start at the value, will be subtracted

#if assigned at night, assign randomly through the rest of the first available day slot.
"""
nightbefore = input("What indexes slept the night before this sheet started?"+
                    " Insert in brackets sep by SPACE.\nFor reference: "
                    +indexlist()+'\nIndexes: ')
nightbefore = inputtolist(nightbefore)"""
### FOR TESTING PURPOSES GOING TO JUST SELECT 0 and 2
nightbefore = [0,2]
### AGAIN, DELETE THIS VAR WHILE TESTING


for i in range(len(allthedays)): #for 0 to 7
    pass


#%% TROUBLESHOOTING/CHECKS     
print(day1) #could cause errors... if you're fucking stupid

dw = dayweights()
print(dw)
print(nightbefore)











"""ATTEMPT TO CONVERT TO ARRAYS- DATAFRAME IS BETTER
#what you want for each row is: print(data.iloc[b, 1:peeps+1].copy())

#print(range(len(data.iloc[:, 1].copy())))

for b in range(0,len(data.iloc[:, 1].copy())):
    #np.append(fulldata,list(data.iloc[b, 1:peeps+1].copy()))
    pass
    #fulldata = fulldata+ list(data.iloc[b, 1:peeps+1].copy())

print(fulldata)
#print(list(data.iloc[0, 1:peeps+1].copy()))

#Creates variables p1 through p[peeps]

 EVEN EARLIER ATTEMPT- BAD
cols = {}
for a in range(1, peeps+1):
    cols["p{}".format(a)] = data.iloc[:, a].copy()

rows = {}
for b in range(0,len(cols['p1'])):
    rows["time{}".format(b)] = data.iloc[b, 1:peeps+1].copy()
    """



#print(cols["p3"])
