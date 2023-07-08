import pandas as pd
import numpy as np
s = pd.series(np.random.randn(4))
print("is the object empty ")
print(s.empty)