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
    Compute the cost of a list of parameters, theta, given a list of features 
    (input data points) and values (output data points).
    """
    m = len(values)
    sum_of_square_errors = numpy.square(numpy.dot(features, theta) - values).sum()
    cost = sum_of_square_errors / (2*m)

    return cost

def predict(features, theta):
    return numpy.dot(features, theta.T).T
    

def gradient_descent(features, values, theta, alpha, num_iterations):
    """
    Perform gradient descent given a data set with an arbitrary number of features.
    """

    # Write code here that performs num_iterations updates to the elements of theta.
    # times. Every time you compute the cost for a given list of thetas, append it 
    # to cost_history.
    # See the Instructor notes for hints. 
    
    cost_history = []

    for i in range(0,num_iterations):
        m = len(values)
        theta += alpha/m * numpy.dot(values-predict(features, theta), features)
        cost = compute_cost(features, values, theta)
        cost_history.append(cost)

    return theta, pandas.Series(cost_history) # leave this line for the grader


if __name__ == '__main__':

    # Read data into a pandas dataframe.
    data = pandas.read_csv('baseball_stats_regression.csv')

    # Isolate features / values.
    features = data[['height', 'weight']]
    values = data[['HR']]
    m = len(values)

    # Normalize features.
    features, mu, sigma = normalize_features(features)

    # Add a column of ones to features for constant term.
    features['ones'] = numpy.ones(m)
    features_array = numpy.array(features[['ones', 'height', 'weight']])
    values_array = numpy.array(values).flatten()

    # Set values for alpha, number of iterations.
    alpha = 0.01
    num_iterations = 1000

    # Initialize theta and perform gradient descent.
    theta_gradient_descent = numpy.zeros(3)
    theta_gradient_descent, cost_history = gradient_descent(features_array, values_array, theta_gradient_descent,
                                                            alpha, num_iterations)

    print "Theta =\n{theta}\n\nCost History = \n{history}".format(theta=theta_gradient_descent, history=cost_history)
