import scipy.stats as stats
import numpy as np
data=[10,12,13,15,14,11,9,10,12,11]
t_stat,p_value=stats.ttest_1samp(data,popmean=11)
print("one sample test result is:")
print(f"T-statistics:{t_stat}")
print(f"P-value:{p_value}")
