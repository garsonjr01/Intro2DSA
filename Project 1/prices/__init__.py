# Import Built-in Python Packages

import numpy as np
import scipy as sp
import pandas as pd
import sklearn
import matplotlib.pyplot as plt



# User-defined functions


# Assumes numpy arrays
def standardize(*args):
    res=list()
    for x in args: # for each input, list the standardized values, the scale, and the shift
        tot=list([(x-x.mean())/x.std(),x.std(),x.mean()])
        res.append(tot) 
    return res # output the list for all inputs
# for each variable converted, arg[0] is the values, arg[1] the scale, and arg[2] the shift,
# so calculating arg[0]*arg[1]+arg[2] will recover the original values 

# This calculates unstandardized variables
# Good for things like converting predicted prices to dollar amounts
def unstandardize(val,scale,shift):
    return val*scale+shift

# Unwrap coefficients to produce the model parameters
def unwrap(weights,scales,shifts):
    n=len(weights)
    weightsNew=weights
    if n>1:
        for x in range(1,n):
            weightsNew[0]-=shifts[x-1]/scales[x-1]
            weightsNew[x]/=scales[x-1]
        return weightsNew
    else:
        return weightsNew
    

# This creates a logical index array to pass to data frames selecting
# the entries that are within 3 std deviations in all variables
def allRangeIndex(first,*pars):
    tot=np.array([True,]*len(first))*(first<=3)
    for x in pars:
        tot=tot*(x<=3)
    return tot

# takes numpy array (vector) as argument, returns sum-of-squares value
def ssq(array):
    return sum(array**2)

# Creates a function definition for a given model in writable form
# and stores it in the passed file.
def func_print(weights,name,file):
    strList=list()
    weightsList=list()
    for x in weights:
        weightsList.append(x)
    strList.append(str().join(['import numpy as np','\n']))
    strList.append(str().join(['def ',str(name),'(*args):\n    ','weights=',str(weightsList),'\n    ']))
    strList.append(str().join(['res=np.zeros(len(args[0]))\n    ','if len(weights)==len(args)+1:\n        ']))
    strList.append(str().join(['for x in range(1,len(args)+1):\n            ','res+=weights[x]*args[x-1]\n        ']))
    strList.append(str().join(['res+=weights[0]\n        ','return res\n    ']))
    strList.append(str().join(['else:\n        print(\'Error in model definition: Unexpected number of inputs!\')']))
    strList.append('\n\n\n\n')
    file.write(str().join(strList))