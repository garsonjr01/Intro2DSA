import numpy as np
def model_area(*args):
    weights=[2.06158688e+04 5.28769586e+00]
    res=np.zeros(len(args[0]))
    if len(weights)==len(args)+1:
        for x in range(1,len(args)):
            res+=weights[x]*args[x-1]
        res+=weights[0]
        return res
    else:
        print('Error in model definition: Unexpected number of inputs!')



import numpy as np
def model_area_nesterov(*args):
    weights=[2.06131431e+04 5.28725773e+00]
    res=np.zeros(len(args[0]))
    if len(weights)==len(args)+1:
        for x in range(1,len(args)):
            res+=weights[x]*args[x-1]
        res+=weights[0]
        return res
    else:
        print('Error in model definition: Unexpected number of inputs!')



import numpy as np
def model_areaFront(*args):
    weights=[-2.29935446e+05  3.19033230e+00  9.33566087e+02]
    res=np.zeros(len(args[0]))
    if len(weights)==len(args)+1:
        for x in range(1,len(args)):
            res+=weights[x]*args[x-1]
        res+=weights[0]
        return res
    else:
        print('Error in model definition: Unexpected number of inputs!')



import numpy as np
def model_areaFront_nesterov(*args):
    weights=[-2.29908783e+05  3.18843957e+00  9.33965212e+02]
    res=np.zeros(len(args[0]))
    if len(weights)==len(args)+1:
        for x in range(1,len(args)):
            res+=weights[x]*args[x-1]
        res+=weights[0]
        return res
    else:
        print('Error in model definition: Unexpected number of inputs!')



