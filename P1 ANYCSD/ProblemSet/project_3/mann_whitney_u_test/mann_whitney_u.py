import numpy as np
import scipy
import scipy.stats
import pandas as pd


def mann_whitney_plus_means(turnstile_weather):
    '''
    This function will consume the turnstile_weather dataframe containing our final turnstile-Subway data. This 
    function should return the mean number of entries with rain, the mean number of entries without rain, and the
    Mann-Whitney U statistic and p-value.  You should feel free to use scipy's Mann-Whitney implementation, and also
    might find it useful to use numpy's mean function.  Here's some documentation on that:

    http://docs.scipy.org/doc/numpy/reference/generated/numpy.mean.html
    
    
    Here's the correct output:
    (1105.4463767458733, 1090.278780151855, 1924409167.0, 0.024999912793489721)
    
    Is the distribution of the number of entries statistically different between rainy and non-rainy days? Yes, since the p-value obtained is 
    smaller than the significance level ((2*0.0245)<0.05), there is indication of a difference in the number of entries between rainy and non rainy days,
    there tend to be more entries in rainy days.
    
    Since the p-value obtained is smaller than the significance level (0.049<0.05), there is indication of a difference in the number of entries between rainy and non rainy days.
    ''' 

    wet = turnstile_master[(turnstile_master['rain']==1)]
    dry = turnstile_master[(turnstile_master['rain']==0)]
    with_rain_mean = wet.ENTRIESn_hourly.mean()
    without_rain_mean = dry.ENTRIESn_hourly.mean()
    U, p = scipy.stats.mannwhitneyu(wet.ENTRIESn_hourly,dry.ENTRIESn_hourly)

    return with_rain_mean, without_rain_mean, U, p
    
if __name__ == "__main__":
    input_filename = "turnstile_data_master_with_weather.csv"
    turnstile_master = pd.read_csv(input_filename)
    student_output = mann_whitney_plus_means(turnstile_master)

    print student_output
    

