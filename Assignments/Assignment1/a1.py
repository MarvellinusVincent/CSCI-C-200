#input radius r, height h
#return volume

def c(r,h):
    import math
    volume = 1/3*math.pi*r**2*h
    return volume
    pass

#input t days
#output oxygen conten percent of it normal level
def f(t):
    oxygen = (100*((t**2)+(10*t)+100))/((t**2)+(20*t)+100)
    return oxygen
    pass


#input t hours
#return percent watching tv
def P(t):
    if 0 <= t <= 8:
        TV = (0.01354*(t**4))-(0.49375*(t**3))+(2.58333*(t**2))+(3.8*t)+31.60704
    else:
        pass
    return TV

#input x percent
#return millions of dollars
def cost(x):
    if 0 <= x <= 100:
        cost = (0.5*x)/(100-x)
    else:
        pass
    return cost

#input dosage a mg and years t
#return child dosage mg
def D(t,a):
    dosage = (a*(t+1))/24
    return dosage
    pass


if __name__ == "__main__":
    """
    If you want to do some of your own testing in this file, 
    please put any print statements you want to try in 
    this if statement.

    You **do not** have to put anything here  """

    #volume of cone
    # print(c(2,5)) 
    # print(c(3,7))

    #oxygen content
    # print(f(0))
    # print(f(10))

    #tv watching
    # print(P(0))
    # print(P(3))
    # print(P(8))

    #x% cost
    # print(cost(50))
    # print(cost(70))
    # print(cost(90))

    #cowling's rule
    # print(D(4,500))