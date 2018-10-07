def average(values):
    """
        values must be an iterable yielding numbers.
    """
    
    return sum(values)/len(values)
#end def average(values)


def weightedAverage(values, weights):
    """
        values: a listing of data points.
        weights: a listing of weights for each data point corresponding to the data point in "values" with same index.
        Both values must have equal length.
    """


    lV = len(values)
    lW = len(weights)
    
    if lV != lW:
        raise ValueError("Both values and weights must have the same length.")


    vSum = 0
    wSum = 0
    for i in range(0,lV):
        vSum += values[i]*weights[i]
        wSum += weights[i]

    return vSum/wSum
#end def weightedAverage(values, weights)


