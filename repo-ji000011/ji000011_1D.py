# CSCI 1133 Homework1
# Peiqi Ji
# Problem 1D
def absError(x,y):
    result = abs(x-y)
    result = round(result,5)
    return result
def relError(x,y):
    result = absError(x,y)
    result = result/x
    result = round(result,5)
    return result
