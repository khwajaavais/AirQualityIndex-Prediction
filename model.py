# -*- coding: utf-8 -*-
"""
Created on Fri Jul 17 20:26:02 2020

@author: khwaj
"""
import numpy as np
import pandas as pd

import warnings
warnings.filterwarnings('ignore')

data = pd.read_csv('Real_Combine.csv')

# Reading first 5 rows
data.head()

data.isnull().sum()

# if we have minimum null values we can drop null values
data = data.dropna()
# We don`t have null values

X = data.drop(['PM 2.5'], axis=1) # Droping the Target Variable i.e. PM 2.5
Y = pd.DataFrame(data['PM 2.5']) # Assigning the Target Vatiavle to Y

from sklearn.model_selection import train_test_split

X_train, X_test, Y_train,Y_test = train_test_split(X, Y, test_size=0.3, train_size=0.7, random_state=0)

from sklearn.ensemble import RandomForestRegressor

# For selecting the best Parameters
from sklearn.model_selection import RandomizedSearchCV

# Randomized Search CV

# No.of Decision-Trees in Random Forest
n_est = [int(x) for x in np.linspace(start=100,stop=1200,num=12)]

# No,of Features to consider at every split
max_feat = ['auto','sqrt']

# Maximum no of levels in trees
maximum_depth = [int(x) for x in np.linspace(start=5,stop=30,num=6)]

# Minimum no.of samples required to sperate a node
minimum_sample_split = [2,5,10,15,100]

# Minimum no.of samples required at each leaf node
minimum_sample_leaf = [1,2,5,10]

RandomForestRegressor()

# All these parameters are the Parameters of RandomForestRegressor()
random_grid = {
    'n_estimators' : n_est,
    'max_depth' : maximum_depth,
    'min_samples_split' : minimum_sample_split,
    'min_samples_leaf' : minimum_sample_leaf,
    'max_features' : max_feat
}
print(random_grid)

# Using random_grid  to search for best parameter

# Creating the best Parameter to tune
rand_forrest = RandomForestRegressor()

rf_random = RandomizedSearchCV(estimator= rand_forrest ,
                                  param_distributions= random_grid, 
                                  scoring='neg_mean_squared_error', 
                                  n_iter=100, cv=5, verbose=2 ,random_state= 42)

rf_random.fit(X_train,Y_train)

import pickle
# Open a file 
file = open('model.pkl', 'wb')

# dump information to that file
pickle.dump(rf_random,file)

# Loading model to compare the results
model = pickle.load(open('model.pkl','rb'))
print(model.predict([[1,1,1,1,1,1,1,1]]))
