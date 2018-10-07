def Average(values):
    """
        values must be an iterable yielding numbers.
    """
    
    return sum(values)/len(values)
#end def average(values)


def WeightedAverage(values, weights):
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

def Median(values, ordered=False, orderFunction=sorted):
    """
        values: a listing of data points
        ordered: for optmization purposes. Indicates whether values is already in order or not. It assumes it is not by default.
        orderFunction: for optmization purposes. Should be a function able to return an ordered version of "values" if "ordered" is set to False. By default, it uses the standard function "sorted".
    """
    
    if not ordered:
        values = orderFunction(values)
        
    length = len(values)
    if length % 2: #if odd
        return values[length//2]
    else: #if even
        return (values[length//2 - 1]+values[length//2])/2
#end def Median(values, ordered, orderFunction)



