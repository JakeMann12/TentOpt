# -*- coding: utf-8 -*-
"""
Created on Sun Dec 11 16:32:32 2022

@author: jmann

SCHEDULER MK2

That jmann kid is a clown lol

Fuck line lickers and sesame street still
"""

#Starting Info
#%%Packages and starting data
import pandas as pd
import numpy as np
import random as ran

#Random dict dot calling dont worry abt it
class dotdict(dict):
    """dot.notation access to dictionary attributes"""
    __getattr__ = dict.get
    __setattr__ = dict.__setitem__
    __delattr__ = dict.__delitem__

mydict = {'val':'it works'}
nested_dict = {'val':'nested works too'}
mydict = dotdict(mydict)
mydict.val
# 'it works'

mydict.nested = dotdict(nested_dict)
mydict.nested.val
# 'nested works too'

#%% THINGS TO ADJUST

peeps = 4 #Number of tenters
daynum = 2 #HOW MANY HAVE TO BE THERE DURING DAY     Black/Blue = 2, White = 1
nightnum = 1 #HOW MANY HAVE TO BE THERE DURING NIGHT Black = 10, Blue = 6, White = 2

dayslots = [0]*peeps
totnights = [0]*peeps

#%% MAIN- Load and manipulate data
#Load data from excel and create DataFrame
df = pd.read_excel("SampleSchedule.xlsx", index_col=0) #0=available, -1=not

#PREVIOUS STATS DICTIONARY- FOR WEIGHTED AVG

prevstats = df.iloc[24:27, 0:peeps] #HARDCODED
psdf = pd.DataFrame(prevstats) #previous stats data frame
stats = psdf.to_dict()
refstats = dotdict(stats) #only for troubleshooting really... refstats.Jake["Nights"] === stats['Jake']['Nights'] === 2

df = df[0:20][df.columns.drop(list(df.filter(regex='Unnamed')))] ##SKIPS UNTITLED COLUMS- blanks/times

#for i in range(0,7):
   # day = df.iloc[:,i*peeps:i*peeps+peeps]
  #  print(day)


# df.shape gives dimensions

#%%

def hourperson():
    #gives choice list of Hours - name earlier in list means less hours so far ergo should be given     
    namelist = sorted(stats, key=lambda x: stats[x]['Hours'], reverse=True)
    collist = namelist["ColIndex"] #FIX ME
    return collist
    
def nightperson():
    #ditto with nights
    namelist = sorted(stats, key=lambda x: stats[x]['Nights'], reverse=True)
    return namelist




"""
for k in daystartindex:  # Num of collums // tenters = days? 
    #creates variables day1 through day7 :)
    if k == daystartindex[0] or k==daystartindex[-1]:
        globals()['day{}'.format(list(daystartindex).index(k)+1)] = df.iloc[:,k:k+peeps].values  
    else:
        globals()['day{}'.format(list(daystartindex).index(k)+1)] = df.iloc[:-3,k:k+peeps].values
allthedays = [day1,day2,day3,day4,day5,day6,day7] #Error code = stupid
day1,day2,day3,day4,day5,day6,day7 = allthedays #Extremely not legit code, but fixes vars
"""




#%% Functions for assignment
"""
This will assume that schedule input is in the format in SampleSchedule.xslx
i.e., -1 if available and 0 if busy

Focusing on nights first then days

Nights will be randomly assigned based on weighted average of 

"""










