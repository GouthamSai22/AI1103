# -*- coding: utf-8 -*-
"""Assignment3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Wnme3OqrlQz4NsMFyGqUJnHK_wRQnNKx
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import bernoulli

#Sample size
simlen = 100000
x_simlen = int((0.6)*simlen)
y_simlen = int((0.4)*simlen)
#Generating random variables
data_bern_x = bernoulli.rvs(p=0.96,size=x_simlen)
data_bern_y = bernoulli.rvs(p=0.72,size=y_simlen)
#Calculating reliable shock absorbers
x_reliable = 0
y_reliable = 0
for i in range(x_simlen):
  if data_bern_x[i]==1:
    x_reliable = x_reliable+1
for i in range(y_simlen):
  if data_bern_y[i]==1:
    y_reliable = y_reliable+1 
#Calculating probability
required_probability = y_reliable/(y_reliable+x_reliable)
print("The required probability is: ",required_probability,"\n")
print("Theoretically calculated probability is: 0.334 \n")
print("Since the difference between both these values is: ",abs(required_probability-0.334),", which is very small we can say that they the answer is correct \n")