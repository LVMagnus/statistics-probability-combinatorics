import math

def Permutation(elementPoolSize, selectionSize = 0, repetition = False):
    """
       Calculates how many ways n elements can be arranged in p positions when order of elements do matter.
       Invalid or out of bounds selectionSize = short cut for selectionSize equal to elementPoolSize
    """
        
    #TOCONSIDER: When/if error handling in Combination() gets addressed, for consistency's sake,
    #it might be better to raise errors for technically invalid inputs here too instead of using it as a shortcut

    
    if selectionSize <= 0:
        elementPoolSize = selectionSize
    #end if


    result = 1
    if repetition:
        result = n ** p
    else:
        if selectionSize > elementPoolSize:
            return 0
        #end if
        
        for i in range(n, n-p,-1):
            result = result * n
            n -= 1
        #end for
    #end if-else

    return result
#end def Permutation(elementPoolSize, selectionSize, repetition)




def Combination(elementPoolSize, selectionSize, repetition = False):
    """
       Calculates how many ways n elements can be arranged in p positions when order of elements does not matter.
    """

    #TODO: handle input errors, selectionSize <= 0 and selectionSize > elementPoolSize 

    
    if repetition:
        return math.factorial(elementPoolSize) / ( math.factorial(selectionSize) * math.factorial(elementPoolSize-selectionSize))
    else:
        return math.factorial((selectionSize + elementPoolSize - 1)) / ( math.factorial(selectionSize) * math.factorial(elementPoolSize-1))

#end def Combination(elementPoolSize, selectionSize, repetition)




