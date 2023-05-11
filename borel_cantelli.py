import numpy as np
import pandas as pd
import matplotlib as mpl
import scipy
import matplotlib
import matplotlib.pyplot as plt
from scipy.stats import skew, kurtosis, chi2

'''
 Goal: Generate 'Borel-Cantellí' simulation.
'''

# SIMULATE RANDOM VARIABLES
times = input("Enter max times: ")
is_normal = True
counter = 0

### Borel-Cantellí: P[all test are normal = True] = 0
while is_normal == True and counter < int(times):
    x_size = 10**6
    degrees_freedom = 9
    # GENERATE DISTRIBUTION
    x = np.random.standard_normal(x_size) 
    
    print(" ")
    # COMPUTE RISK METRICS
    x_mean = np.mean(x)
    s_stdev = np.std(x)
    x_skew = skew(x)
    x_kurt = kurtosis(x)
    x_median = np.percentile(x,95)
    x_VaR95 = np.percentile(x,5)
    x_jb = x_size/6*(x_skew**2 + 1/4*x_kurt**2)
    p_value = 1 - chi2.cdf(x_jb,df=degrees_freedom)
    is_normal = (p_value > 0.05)

    print("MEAN: ",x_mean)
    print("STD_DEV: ",s_stdev)
    print("SKEWNESS: ",x_skew)
    print("KURTOSIS: ",x_kurt)
    print("MEDIAN: ",x_median)
    print("VaR95: ",x_VaR95)
    print("JARQUE-BERA: ",x_jb)
    print("P-VALUE: ",p_value)
    print("IS NORMAL: ",str(is_normal))

    counter+=1
    print('COUNTER ' + str(counter))
    print('------')
