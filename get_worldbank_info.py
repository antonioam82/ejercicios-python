
from pandas_datareader import wb
 
matches = wb.search('total.*population')
print(matches[["id","name"]])
