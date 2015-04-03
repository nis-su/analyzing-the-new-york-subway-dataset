from prediction import predictions

import pandas as pd
import numpy as np

def compute_r_squared(data, predictions):
    # Write a function that, given two input numpy arrays, 'data', and 'predictions,'
    # returns the coefficient of determination, R^2, for the model that produced 
    # predictions.
    # 
    # Numpy has a couple of functions -- np.mean() and np.sum() --
    # that you might find useful, but you don't have to use them.

    # What are coefficients of determination (From Wikipedia)
    # In a general form, R2 can be seen to be related to the unexplained variance, 
    # since the second term compares the unexplained variance (variance of the model's errors) 
    # with the total variance (of the data)
    # The total sum of squares is SS_tot = sum(y_i - ybar)^2 (y is the observed data)
    # The regression sum of squares is SS_reg = sum(f_i - ybar)^2 (f is the predicted data)
    # R^2 = 1 - (SS_reg/SS_tot)
    # The least squares fit line is explained in MST121 book D4, chapter 5
    # 
    SST = ((data-np.mean(data))**2).sum()
    SSReg = ((predictions-data)**2).sum()
    r_squared = 1 - SSReg/SST
    return r_squared


if __name__ == "__main__":
    input_filename = "turnstile_data_master_with_weather.csv"
    turnstile_master = pd.read_csv(input_filename)
    predictions = predictions(turnstile_master)
    r_squared = compute_r_squared(turnstile_master['ENTRIESn_hourly'], predictions)
    print r_squared