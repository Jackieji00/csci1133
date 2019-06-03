#recursion:
#   statement
#   reduction
# def foo(n):
#   if n == 1:
#     return 1
#   return foo(n-1)+n
"how to" problem:
    find a suitable problem


    identify a base-case
def listsum(alist): #sum up all the list
    if listsum(alist) == 0:
        return 0
    return listsum(alist[?-1] + alist[1])
def isPalinedrone(s):
    if len(s) <= 1:
        return true
    return s[0] == s[-1] and isPalinedrone(s[1:-1])
