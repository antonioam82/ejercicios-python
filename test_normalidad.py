import numpy as np
import pandas as pd
import matplotlib as mpl
import scipy
import matplotlib
import matplotlib.pyplot as plt
from scipy.stats import skew, kurtosis, chi2

'''
 Goal: Create a normality test e.g. Jarque-Bera

 step 1: generate random variables
 step 2: visualise histogram
 step 3: what is Jarque-Bera

 '''

# SIMULATE RANDOM VARIABLES
x_size = 10**6
degrees_freedom = 9
type_random_variable = "normal"

if type_random_variable == "normal":
    x = np.random.standard_normal(x_size)
    x_str = type_random_variable
elif type_random_variable == "exponential":
    x = np.random.standard_exponential(x_size)
    x_str = type_random_variable
elif type_random_variable == "normal":
    x = np.random.standard_t(df=degrees_freedom,size=x_size)
    x_str = type_random_variable + ' (df=' + str(degrees_freedom) + ')'
elif type_random_variable == "chi-squared":
    x = np.random.chisquare(size=x_size,df=2)
    x_str = type_random_variable + ' (df=' + str(degrees_freedom) + ')'
    
print(" ")
# COMPUTE RISK METRICS
x_mean = np.mean(x)
s_stdev = np.std(x)
x_skew = skew(x)
x_kurt = kurtosis(x)
x_median = np.percentile(x,95)
x_VaR95 = np.percentile(x,5)
x_cvar95 = np.mean(x[x <= x_VaR95])
x_jb = x_size/6*(x_skew**2 + 1/4*x_kurt**2)
p_value = 1 - chi2.cdf(x_jb,df=degrees_freedom)
is_normal = (p_value > 0.05)

print("MEAN: ",x_mean)        # MEDIA
print("STD_DEV: ",s_stdev)    # VOLATILIDAD
print("SKEWNESS: ",x_skew)    # SIMETRIA
print("KURTOSIS: ",x_kurt)    # LONG COLAS
print("MEDIAN: ",x_median)    # MEDIANA
print("VaR95: ",x_VaR95)      # VALOR EN RIESGO
print("CVaR95: ",x_cvar95)    # VALOR EN RIESGO CONDICIONAL
print("JARQUE-BERA: ",x_jb)   # NORMALIDAD
print("P-VALUE: ",p_value)
print("IS NORMAL: ",str(is_normal))

# PLOT HISTOGRAM
plt.figure()
plt.hist(x,bins=100)
plt.title('Histogram ' + x_str)
plt.show()

