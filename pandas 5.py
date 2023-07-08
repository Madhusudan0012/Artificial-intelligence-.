import pandas as pd
import numpy as np
s = pd.series([1,2,3,4,5], index=['a','b','c','d','e'])
print(s[0])
print(s[:3])
print(s[-3:])