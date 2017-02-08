# -*- coding: utf-8 -*-
"""
Created on Wed Jan 25 08:35:51 2017

@author: Owner
"""
#%%
from math import sqrt
value=-100

#condition
if value >= 0: 
    # what to do if condition is true:
    rootValue=sqrt(value)
    print (rootValue)
else:
    # what to do if condition is false:
    print('Sorry, I do not compute square roots of negative numbers')
#%%
from math import sqrt  # no need for this in R

values=[9,25,100]

for value in values:  # for each value in values...
    print(sqrt(value)) # do this
#%%
values=[9,25,100]
rootValues=[] # empty list, we will populate it later!

for value in values:
    rootValues.append(sqrt(value))  # appending an element to the list (populating the list)

# This list started empty, now see what its elements are:
rootValues
#%%
values=[9,25,-100]
rootValues=[]

for value in values:
    rootValues.append(sqrt(value))

# to see the results:
rootValues
#%%
values=[9,25,-100,144,-72]
rootValues=[]

for value in values:
    # checking the value:
    if value <0:
        print('We need to stop, invalid value detected')
        break
    # you will get here if the value is not negative
    rootValues.append(sqrt(value))
        

# to see the results:
rootValues
#%%
import numpy as np

values=[9,None,np.nan, '1000',-100, 144,-72]
for value in values: # notice the order of 'IFs'
    if value==None: # condition1 # when HW:  value==none is changed to np.isnan it will only process numbers
        print ('missing values as input')
        continue
    if isinstance(value, str): #condition2
        print ('string as input')
        continue
    if value < 0: # condition3
        print ('negative value as input')
        continue
    print (sqrt(value), 'is the root of ',value)  
#%%
type(None),type(np.nan)
#%%
10 + None
#%%
values=[9,25,-100,144,-72]

counterOfInvalids=0 # counter 

for value in values:
    if value <0:
        counterOfInvalids +=1 #updating counter

# to see the results:
counterOfInvalids
#%%
values=[9,25,-100,144,-72]
positionInvalids=[]
currentPosition=0 # initial position

for value in values:
    if value <0:
        positionInvalids.append(currentPosition)
    currentPosition+=1 # becareful where you put the 'accumulator'

# to see the results:
positionInvalids 
#%%
# testing:
for pos in positionInvalids:
    print (values[pos])
    print (sqrt(-10)) # what kind of error you get:value error
#%%
values=[10,-10,'10']
#%%
for value in values:
    try:
        print (sqrt(value))
    except ValueError:
        print (value,'is a Wrong number!')
    except TypeError:
        print (value,'is Not even a number!!')
#%%
import pandas as pd
import os
folderName='data'
fileName='people.xlsx'
fileExcel=os.path.join('data','people.xlsx')
dataFromExcel=pd.read_excel('people.xlsx') # table '1'
dataFromExcel
#%%
# what is the oldest age (without using function 'max')
oldestAge=0
for age in dataFromExcel.ages:
    if oldestAge<age:
        oldestAge=age 
# Then:
oldestAge
#%%
# How many people share the oldest age?
countOldest=0
for age in dataFromExcel.ages:
    if oldestAge==age:
        countOldest+=1
# Then:
countOldest
#%%