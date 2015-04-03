import numpy
import scipy.stats
import pandas

    
    


    
def areMeansEqual(filename):
    data = pandas.read_csv(filename)
    rainy = data.loc[data['rain']==1]
    nonrainy = data.loc[data['rain']==0]
    tval = scipy.stats.ttest_ind(rainy.ENTRIESn_hourly,nonrainy.ENTRIESn_hourly,equal_var=False)
    if tval[1]<0.05:
        return (False,tval)
    else:
        return (True,tval)

def doMWUTest(filename):
    data = pandas.read_csv(filename)
    rainy = data.loc[data['rain']==1]
    nonrainy = data.loc[data['rain']==0]
    U, p = scipy.stats.mannwhitneyu(rainy.ENTRIESn_hourly,nonrainy.ENTRIESn_hourly)

    return U, p
    
    

if __name__ == '__main__':
    r = areMeansEqual('improved-dataset/turnstile_weather_v2.csv')
    print "-*-*--*| Student's T-Test |*--*-*-"
    print "Are Means Equal: %s" % r[0]
    print "t-value:         %s" % r[1][0]
    print "p-value:         %s" % r[1][1]
    print "p-critical:      0.05"
    
    print "\n"
    U,p = doMWUTest('improved-dataset/turnstile_weather_v2.csv')
    print "-*-*--*| Mann Whitney U Test |*--*-*-"
    print "u-value:         %s" % U
    print "p-value:         %s" % p
    print "p-critical:      0.05"
    print "\n"