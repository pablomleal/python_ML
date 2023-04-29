import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
#%matplotlib inline

mi = pd.MultiIndex.from_arrays((list('abc'), list('def')))
mi.names = ['level_1', 'level_2']


print(mi)