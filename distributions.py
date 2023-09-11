import matplotlib as mpl
import scipy
import matplotlib.pyplot as plt
from scipy.stats import skew, kurtosis, chi2
import numpy as np

#inputs
coeff = 5 # df in student, scale in exponential
size = 10**6
random_variable_type = 'uniform'
decimals = 5

# code
str_title = random_variable_type
if random_variable_type == 'normal':
    x = np.random.standard_normal(size=size)
elif random_variable_type == 'student':
    x = np.random.standard_t(df=coeff,size=size)
    str_title = str_title + ' df=' + str(coeff)
elif random_variable_type == 'uniform':
    x = np.random.uniform(size=size)
elif random_variable_type == 'exponential':
    x = np.random.exponential(scale=coeff, size=size)
    str_title += ' scale=' + str(coeff)
elif random_variable_type == 'chi-squared':
    x = np.random.chisquare(df=coeff, size=size)
    str_title += ' df=' + str(coeff)

mu = np.mean(x)
sigma = np.std(x)
skew = skew(x)
kurt = kurtosis(x)

str_title += '\n' + 'mean=' + str(np.round(mu,decimals)) \
              + '\n' + 'volatility=' + str(np.round(sigma,decimals)) \
              + '\n' + 'skewness=' + str(np.round(skew,decimals)) \
              + '\n' + 'kurtosis=' + str(np.round(kurt,decimals))

plt.figure()
plt.hist(x,bins=100)
plt.title(str_title)
plt.show()
