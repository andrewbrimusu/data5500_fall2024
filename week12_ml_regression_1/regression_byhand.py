'''
This program reviews how Regression is used to fit "or learn" the coefficients
in a dataset

'''

import os

# os.system("sudo pip3 install networkx")
# os.system("sudo apt-get install libjpeg-dev zlib1g-dev")
# os.system("sudo pip3 install Pillow")
# os.system("sudo pip3 install matplotlib")


import numpy as np
import matplotlib.pyplot as plt

curr_dir = os.path.dirname(__file__) # get the current directory of this file

# This functions mathematically calculates the coefficients
def estimate_coef(x, y):
    # number of observations/points
    n = np.size(x)
 
    # mean of x and y vector
    m_x = np.mean(x)
    m_y = np.mean(y)
 
    # calculating cross-deviation and deviation about x
    SS_xy = np.sum(y*x) - n*m_y*m_x
    SS_xx = np.sum(x*x) - n*m_x*m_x
 
    # calculating regression coefficients
    coeff = SS_xy / SS_xx
    interc = m_y - coeff * m_x
 
    return (interc, coeff)
 
# The function plots the line and saves it to a file
def plot_regression_line(x, y, b):
    # plotting the actual points as scatter plot
    plt.scatter(x, y, color = "m",
               marker = "o", s = 30)
 
    # predicted response vector
    y_pred = b[0] + b[1]*x
 
    # plotting the regression line
    plt.plot(x, y_pred, color = "g")
 
    # putting labels
    plt.xlabel('x')
    plt.ylabel('y')
 
    # function to show plot
    plt.show()
    plt.savefig(curr_dir + "/output/regression_byhand.png")
 
 
# create dataset and run regression
def main():
    # observations / data
    x = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    y = np.array([2, 3, 4, 5, 7, 8, 8, 9, 15, 20])
 
    # estimating coefficients
    interc, coeff = estimate_coef(x, y)
    print("intercept: ", interc)
    print("coeff: ", coeff)
 
    # plotting regression line
    plot_regression_line(x, y, (interc, coeff))
 
if __name__ == "__main__":
    main()