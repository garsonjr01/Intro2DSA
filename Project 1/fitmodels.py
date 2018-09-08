import numpy as np
def area(*args):
    weights=[20615.868798490148, 5.287695862982692]
    res=np.zeros(len(args[0]))
    if len(weights)==len(args)+1:
        for x in range(1,len(args)+1):
            res+=weights[x]*args[x-1]
        res+=weights[0]
        return res
    else:
        print('Error in model definition: Unexpected number of inputs!')



import numpy as np
def area_nesterov(*args):
    weights=[20613.143127058487, 5.287257731652961]
    res=np.zeros(len(args[0]))
    if len(weights)==len(args)+1:
        for x in range(1,len(args)+1):
            res+=weights[x]*args[x-1]
        res+=weights[0]
        return res
    else:
        print('Error in model definition: Unexpected number of inputs!')



import numpy as np
def areaFront(*args):
    weights=[-229935.44569470512, 3.1903322976569575, 933.5660873119294]
    res=np.zeros(len(args[0]))
    if len(weights)==len(args)+1:
        for x in range(1,len(args)+1):
            res+=weights[x]*args[x-1]
        res+=weights[0]
        return res
    else:
        print('Error in model definition: Unexpected number of inputs!')



import numpy as np
def areaFront_nesterov(*args):
    weights=[-229908.78336043213, 3.18843956920988, 933.9652115883405]
    res=np.zeros(len(args[0]))
    if len(weights)==len(args)+1:
        for x in range(1,len(args)+1):
            res+=weights[x]*args[x-1]
        res+=weights[0]
        return res
    else:
        print('Error in model definition: Unexpected number of inputs!')



