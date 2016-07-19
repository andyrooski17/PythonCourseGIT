import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
#%%
3/2
test = np.array([[1, 0],[0, 1]])

print(test)
#%% NUMBERS
2+1
2-1
2*3
#%%
3/2 #python 2 / is a "classic division", truncating decimals can force true division in python 2 by making float
3.0/2 #would work in python2
float(3)/2 #cast 3 as a float
#%%
2**3
2+10*10+1 #order of opps observed
#%%
a = 5
a = a+a
# names can't stat with a numbr or some symbols, can't have spaces
#best practive usually to have lower case...

#%%
income = 1000
taxrate = 0.1
my_taxes = income * taxrate
#%% STRINGS
# single quotes or double quotes
'hello'
# why double quotes
"I'm using a single quote in my string"
# opposite
gettys = ' "four score and seven years..." - Lincoln'
print(gettys)
print('first line \nsecond line')
len(gettys)
gettys[2]