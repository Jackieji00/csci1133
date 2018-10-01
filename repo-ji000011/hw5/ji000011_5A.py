# CSCI 1133 Homework5
# Peiqi Ji
# Problem 5A
def flattenList(alist):
    n = len(alist)
    if n == 1:         # the case when the alist is like [x] or [[x]]
        if type(alist[0]) == list:    #when the alist still have other list inside
            return flattenList(alist[0])
        else:          # the case when the alist only has the type other than list
            return [alist[0]]
    elif n >1:      # when the contains more than one element, separating them from the last one
        if type(alist[n-1]) == list:  # when the last one is list
            return flattenList(alist[:n-1]) + flattenList(alist[n-1])
        elif type(alist[n-1]) != list:  # when the last one is not list
            return flattenList(alist[:n-1]) + [alist[n-1]]
    elif n == 0:      # the case when the alist contains nonetype
        return []
