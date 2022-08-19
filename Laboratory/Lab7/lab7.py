###########################################################
# factorial
###########################################################

def factorial(n):
    """
    Recursive function to calculate the factorial of n

    Input:
        n (an integer)
    Returns:
        n! = n*(n-1)*...*2*1
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def tail_factorial(n, a=1):
    """
    Tail-recursive function to calculate the factorial of n

    Input:
        n (an integer)
    Returns:
        n! = n*(n-1)*...*2*1
    """
    if n == 0:
        return a
    else:
        return tail_factorial(n-1, a = a * n)

d = {}
def memo_factorial(n):
    """
    Memoized function to calculate the factorial of n

    Input:
        n (an integer)
    Returns:
        n! = n*(n-1)*...*2*1
    """
    if n not in d.keys():
        if n <= 1:
            d[n] = 1
        else:
            d[n] = n * memo_factorial(n-1)
    return d[n]

###########################################################
# only_ints
###########################################################
xlist = [1,2,3,4,5,"dog","cat"]
def only_ints(xlist):
    """
    Recursive function to return a list with all non-ints taken
    out of it.

    Input:
        xlist - a list of elements
    Returns:
        xlist, but with only the 'int'-type elements kept.

    """
    if xlist == []:
        return xlist
    if type(xlist[0]) == int:
        return [xlist[0] + only_ints(xlist[1:])]
    else:
        return only_ints(xlist[1:])



def tail_only_ints(xlist, a=[]):
    """
    Recursive function to return a list with all non-ints taken
    out of it.

    Input:
        xlist - a list of elements
    Returns:
        xlist, but with only the 'int'-type elements kept.

    """
    if xlist == []:
        return a
    if type(xlist[0]) == int:
        return tail_only_ints(xlist[1:], a + xlist[0])
    else:
        return tail_only_ints(xlist[1:], a)

d_only = {}
def memo_only_ints(xlist):
    """
    Recursive function to return a list with all non-ints taken
    out of it.

    Input:
        xlist - a list of elements
    Returns:
        xlist, but with only the 'int'-type elements kept.

    """
    xtup = tuple(xlist)
    if xtup not in d_only.keys:
        d_only[xtup] = []
    elif type(xlist[0]) != int:
        d_only[xtup] = memo_only_ints(xlist[1:])
    else: 
        d_only[xtup] = [xlist[0]] + memo_only_ints(xlist[1:])




if __name__ == "__main__":
    # Write your own print statements here
    # to briefly test your code
    """
    fibonaci sequence
    """
    def fib(n):
        if n == 0 or n == 1:
            return n
        else:
            return fib (n-1) + fib (n-2)
    dictionary = {}
    def memo_fib(n):
        if memo_fib(n) in dictionary.keys():
            return dictionary[n]
        if n == 0 or n == 1:
            dictionary[n] = n
        else:
            dictionary[n] = memo_fib(n-1) + memo_fib(n-2)
        return memo_fib(n)
    pass