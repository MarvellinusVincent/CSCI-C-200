import math

from numpy import true_divide

#problem 1
#input real
#return real
def g(x):
  if x == 0:
    return 1
  else:
    return x+2
    pass


#problem 2
#input year 1977-1997
#return percent income or "error: year" if year 
#is outside range
def f(t):
    t = t - 1977
    if 0 <= t <= 7:
        t = (2/7*t) + 12
    elif 7 < t <= 10:
        t = t + 7
    elif 10 < t <= 20:
        t = (3/5*t) + 11
    else:
        return ("error: year")
    return t
    pass


#problem 3
#input t years = 0
#output dollars
def h_0(t):
    t = 110/((0.5*t)+1)
    return t
    pass

def h_1(t):
    t = (26*((0.25*(t**2))-1)**2)+52
    return t
    pass 

def h(t):
    t = h_0(t)-h_1(t)
    return t
    pass


#problem 4
#input tuple (a,b,c) coefficients
#output tuple roots (x_1, x_2) where x_1 >= x_2
def q(coefficients):
    import math
    a = coefficients[0]
    b = coefficients[1]
    c = coefficients[2]
    q = (-b+(((b**2)-(4*a*c))**0.5))/(2*a),(-b-(((b**2)-(4*a*c))**0.5))/(2*a)
    return q
    pass

#problem 5
#input [arg1,op,arg2,ans]
#output arg1 op arg2 == ans
def eq(lst):
    if lst[1] == "+":
        return lst[0] + lst[2] == lst[3]
    elif lst[1] == "-":
        return lst[0] - lst[2] == lst[3]
    elif lst[1] == "*":
        return lst[0] * lst[2] == lst[3]
    else:
        return lst[0] / lst[2] == lst[3]
        
#problem 6
#input list of swithes
#output True if path from start to end
def path(lst):
    a = lst [0]
    b = lst [1]
    c = lst [2]
    d = lst [3]
    e = lst [4]
    if a == 0:
        return False
    elif a and c == 1:
        return True
    elif a and b and d == 1:
        return True
    elif a and b and e == 1:
        return True
    else:
        return False
    pass

#problem 7
#INPUT two numbers
#RETURN maximum of the two
#You cannot use Python's max function
#You must use if, elif, else (or some combination)
def max2d(x,y):
    if x > y:
        return x
    else:
        return y
    pass

#INPUT 3 numbers
#RETURN maximum of the three
#You must use your max2D function
def max3d(x,y,z):
    max3d = max2d(x,max2d(y,z))
    return max3d
    pass

#from homework
def m(x,y):
    return (x > y)*x + (x <= y)*y

if __name__ == "__main__":
    """
    The code in "__main__" is not being graded, but a tool for you to test 
    your code outside of the unit testing Feel free to add print statements. 
    You should uncomment *after* you've completed the function
    """

    #problem 1 
    # print(g(0))
    # print(g(1))
    # print(g(1.01))

    #problem 2
    # print(f(1976))
    # print(f(1977))
    # print(f(1985))
    # print(f(1988))
    # print(f(2000))

    #problem 3
    # print(h(0))
    # print(h(1))
    # print(h(2))

    #problem 4
    # print(q((1,0,-1)))
    # print(q((6,-1,-35)))
    # print(q((1,-7,-7)))

    #problem 5
    # print(eq([14, "/",2, 7]))
    # print(eq([20, "*",19, 381]))
    # print(eq([20, "*",19, 380]))

    #problem 6
    # print(path([1,0,1,0,0]))
    # print(path([1,1,1,0,0]))
    # print(path([1,0,0,1,0]))

    #problem 7
    # print(max3d(1,2,3))
    # print(max3d(1,3,2))
    # print(max3d(3,2,1))