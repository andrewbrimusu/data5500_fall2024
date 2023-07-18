'''
This program uses Linear Regression model from the sklearn library to fit the coefficients
of the Boston Housing Dataset.
This is a well known dataset, that you can read more on the data science site Kaggle.

Review boston_housing_description.txt for more info.

'''


import os
# os.system("sudo pip3 install sklearn")

import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, linear_model, metrics
import pandas as pd

###################################################
# Load the dataset directory from the sklearn repositor
# using the load_boston function provided
curr_dir = os.path.dirname(__file__) # get the current directory of this file


# load the boston dataset
boston = datasets.load_boston(return_X_y=False)
 
# defining feature matrix(X) and response vector(y)
X = boston.data
y = boston.target

df_x = pd.DataFrame(X)
df_x.to_csv(curr_dir + "/output/boston_data_X.csv")

df_y = pd.DataFrame(y)
df_y.to_csv(curr_dir + "/output/boston_data_y.csv")


# X = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]).reshape(-1,1)
# y = np.array([2, 3, 4, 5, 7, 8, 8, 9, 15, 20]).reshape(-1,1)
 
###################################################
# splitting X and y into training and testing sets
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4,
                                                    random_state=1)
 
 
###################################################
# create linear regression object
reg = linear_model.LinearRegression()
 
 
###################################################
# train the model using the training sets
reg.fit(X_train, y_train)
 
###################################################
# View Results
# regression coefficients
print('Coefficients: ', reg.coef_)
 
# variance score: 1 means perfect prediction
print('Variance score: {}'.format(reg.score(X_test, y_test)))
 
# plot for residual error
 
## setting plot style
plt.style.use('fivethirtyeight')
 
## plotting residual errors in training data
plt.scatter(reg.predict(X_train), reg.predict(X_train) - y_train,
            color = "green", s = 10, label = 'Train data')
 
## plotting residual errors in test data
plt.scatter(reg.predict(X_test), reg.predict(X_test) - y_test,
            color = "blue", s = 10, label = 'Test data')
 
## plotting line for zero residual error
plt.hlines(y = 0, xmin = 0, xmax = 50, linewidth = 2)
 
## plotting legend
plt.legend(loc = 'upper right')
 
## plot title
plt.title("Residual errors")
 

## method call for showing the plot
plt.show()
plt.savefig(curr_dir + "/output/regression_boston_housing.png")
