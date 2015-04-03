import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from ggplot import *


def entries_histogram(turnstile_weather):
    plt.figure()
    wet = turnstile_weather[turnstile_weather["rain"] == 1 ]['ENTRIESn_hourly']
    dry = turnstile_weather[turnstile_weather["rain"] == 0 ]['ENTRIESn_hourly']
    dry.hist(bins=300,alpha=0.8, label='Rainy')
    wet.hist(bins=300,alpha=0.8,label='Dry')
    plt.xlim([0,6000])
    plt.ylim([0,8000])
    plt.legend(loc='upper right')
    return plt

def ridershipTimeofDay(input):
    pd.options.mode.chained_assignment = None
    data = input
    dagg = data[['hour','ENTRIESn_hourly']].groupby('hour',as_index=False).sum()
    plot = ggplot(dagg,aes(x = 'hour',y = 'ENTRIESn_hourly')) + geom_bar(stat="bar") + ggtitle('Hourly Transit NYC Subway')
    return plot
    
    
    
def ridershipDayofWeek(input):
    pd.options.mode.chained_assignment = None
    data = input
    data.DATEn = pd.to_datetime(data.DATEn)
    dagg = data[['DATEn','ENTRIESn_hourly']].groupby('DATEn',as_index=False).sum()
    plot = ggplot(dagg,aes(x = 'DATEn',y = 'ENTRIESn_hourly')) + geom_line(color='coral') +  scale_x_date(labels='%a',breaks=date_breaks('day') ) + ggtitle('Daily Transit NYC Subway')
    return plot



if __name__=='__main__':
    input_filename='improved-dataset/turnstile_weather_v2.csv'
    with open('dayofweek', "wb") as f:
        turnstile_weather = pd.read_csv(input_filename)
        turnstile_weather['datetime'] = turnstile_weather['DATEn'] + ' ' + turnstile_weather['TIMEn']
        gg =  ridershipDayofWeek(turnstile_weather) 
    ggsave('dayofweek', gg)
    
    with open('timeofday', "wb") as f:
        turnstile_weather = pd.read_csv(input_filename)
        turnstile_weather['datetime'] = turnstile_weather['DATEn']
        gg =  ridershipTimeofDay(turnstile_weather)
    ggsave('timeofday', gg)
    
    turnstile_weather = pd.read_csv(input_filename)
    plt = entries_histogram(turnstile_weather)
    plt.show()