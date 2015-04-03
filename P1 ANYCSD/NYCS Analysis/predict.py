import numpy
import pandas




def normalize_features(array):
    """
    Normalize the features in our data set.
    """
    array_normalized = (array - array.mean())/array.std()
    mu = array.mean()
    sigma = array.std()

    return array_normalized, mu, sigma


def compute_cost(features, values, theta):
    """
    Compute the cost function given a set of features / values, and values for our thetas.
    """
    m = len(values)
    sum_of_square_errors = numpy.square(numpy.dot(features, theta) - values).sum()
    cost = sum_of_square_errors / (2*m)

    return cost

def gradient_descent(features, values, theta, alpha, num_iterations):
    """
    Perform gradient descent given a data set with an arbitrary number of features.
    """

    m = len(values)
    cost_history = []
    for i in range(num_iterations):
        predicted_values = numpy.dot(features,theta)
        theta = theta - alpha/m*numpy.dot((predicted_values-values),features)
        cost = compute_cost(features,values,theta)
        cost_history.append(cost)    
    return theta, pandas.Series(cost_history)

def predict(dataframe):
    dummy_units = pandas.get_dummies(dataframe['UNIT'], prefix='unit')
    features = dataframe[['rain', 'precipi', 'hour', 'meantempi']].join(dummy_units)
    values = dataframe[['ENTRIESn_hourly']]
    m = len(values)

    features, mu, sigma = normalize_features(features)

    features['ones'] = numpy.ones(m)
    features_array = numpy.array(features)
    values_array = numpy.array(values).flatten()

    #Set values for alpha, number of iterations.
    alpha = 0.1 # please feel free to play with this value
    num_iterations = 25 # please feel free to play with this value

    #Initialize theta, perform gradient descent
    theta_gradient_descent = numpy.zeros(len(features.columns))
    theta_gradient_descent, cost_history = gradient_descent(features_array, values_array, theta_gradient_descent,
                                                            alpha, num_iterations)
    #plot = plot_cost_history(alpha, cost_history)
    predictions = numpy.dot(features_array, theta_gradient_descent)
    return predictions

    
    
    
def compute_r_squared(data, predictions):
    # Write a function that, given two input numpy arrays, 'data', and 'predictions,'
    # returns the coefficient of determination, R^2, for the model that produced 
    # predictions.
    # 
    # Numpy has a couple of functions -- np.mean() and np.sum() --
    # that you might find useful, but you don't have to use them.

    # YOUR CODE GOES HERE
    SST = ((data-numpy.mean(data))**2).sum()
    SSReg = ((predictions-data)**2).sum()
    r_squared = 1 - SSReg/SST
    return r_squared


if __name__ == "__main__":
    input_filename = "improved-dataset/turnstile_weather_v2.csv"
    data = pandas.read_csv(input_filename)
    observed = data #data.loc[data['rain']==1]
    predicted_values = predict(data)
    r_squared = compute_r_squared(observed['ENTRIESn_hourly'], predicted_values)
    
    print "r_squared:              %s" % r_squared