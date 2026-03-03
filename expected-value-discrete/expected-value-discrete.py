import numpy as np

def expected_value_discrete(x, p):
    """
    Returns: float expected value
    """
    # Write code here
    ans = 0
    if sum(p)!=1:
        raise ValueError 
    for i in range(len(x)):
        ans+= x[i]*p[i]
    return ans
    pass
