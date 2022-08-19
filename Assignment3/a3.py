from cmath import sqrt
import math

#Problem 1

#INPUT n0 start colony size, m growth rate, t time
#RETURN final colony size
def N(n_0, m, t):
    bacteria = (n_0*math.exp(m*t))
    return bacteria

#INPUT t days
#RETURN number of teeth
def N_t(t):
    teeth = math.ceil(71.8*math.exp(-8.96*math.exp(-0.0685*t)))
    return teeth

#INPUT pressures Pi, Pf 
#RETURN work joules
def W(P_i, P_f):
    joules = math.ceil(8.314*300*math.log(P_i/P_f))
    return joules

#INPUT V miles per hour, A area, C_l lift coefficient
#RETURN lbs 
def L(V,A,C_l):
    lbs = math.ceil(0.0033*(V**2)*A*C_l)
    return lbs

###########################################################################
# Functions for Problem 2
###########################################################################
#INPUT t = (a,b,c)
#RETURN True if discriminant is real, False otherwise
def q(t):
    a = t[0]
    b = t[1]
    c = t[2]
    if (b**2)-(4*a*c) > 0:
        return (b**2)-(4*a*c) > 0
    else:
        return False


###########################################################################
# Functions for Problem 3
###########################################################################
#INPUT item and list
#RETURN True if item is in the list
#CONSTRAINT You cannot use 'in' -- must use bounded looping
def m(x,lst):
    for number in range(len(lst)):
        if lst[number] == x:
            return True
    return False

def amt(r,no_tax):
    cost_notax = 0
    cost_tax = 0
    cost = 0
    for number in r:
        if m(number[0],no_tax) == True:
            cost_notax = cost_notax + number[1]
        else:
            cost_tax = cost_tax + (number[1] * 1.07)
    cost = cost_notax + cost_tax
    return round (cost,2)

        


###########################################################################
# Functions for Problem 4
###########################################################################
#INPUT p0 = (x0,y0) p1 = (x1,y1)
#RETURN (a,b,c) for line ax + by + c = 0
def f(p0,p1):
    if p0[0] != p1[0]:
        slope = (p1[1] - p0[1]) / (p1[0] - p0[0])
        intercept = p1[1] - (slope*p1[0])
        return (slope,intercept)
    else:
        return (())



###########################################################################
# Functions for Problem 5
###########################################################################
#INPUT List of numbers
#RETURN Various means or error message

err_msg = ["Data Error: 0 values", "Data Error: 0 in data"]

def arithmetic_mean(nlst):
    if nlst != []:
        number = len(nlst)
        total = sum(nlst)
        return total/number
    else:
        return err_msg[0]

def geo_mean(nlst):
    if nlst != []:
        number = len(nlst)
        total = 0
        for each_number in nlst:
            total_log = math.log10(each_number)
            total = total + total_log
        exponent = total/number
        complete = 10**exponent
        return round(complete,2)
    else:
        return err_msg[0]

def har_mean(nlst):
    if nlst != []:
        number = len(nlst)
        total = 0
        for each_number in nlst:
            if each_number == 0:
                return err_msg[1]
            total_number = 1/each_number
            total = total + total_number
        harmonic = number/total
        return harmonic
    else:
        return err_msg[0]
    
def RMS_mean(nlst):
    if nlst != []:
        total = 0
        number = len(nlst)
        for each_number in nlst:
            sum = each_number**2
            total = total + sum
        RMS_raw = total/number
        RMS = RMS_raw ** 0.5
        return round(RMS,2)
    else:
        return err_msg[0]
    

###########################################################################
# Functions for Problem 6
###########################################################################
#INPUT x filters
#RETURN fixed cost
def F(x):
    return 10000

#INPUT x filters
#RETURN variable cost
def V(x):
    if 0 <= x <= 40000:
        return (-0.0001*(x**2)) + (10*x)
    else:
        return None

#INPUT x filters
#RETURN total cost
def C(x):
    return F(x) + V(x)

###########################################################################
# Functions for Problem 7
###########################################################################

#INPUT list [p,i,n] principal, interest rate, payments
#RETURN montly payment float
def Mortgage(house):
    p = house[0]
    i = house[1] / 1200
    n = house[2] * 12
    return round((p * (i * ((1 + i) ** n))) / (((1 + i) ** n) - 1),2)


#INPUT list [p,i,n] principal, interest rate, payments
#RETURN the difference between total payout and value
#of home 
#REQUIRES Mortgage function
def total_paid(house):
    return round((Mortgage(house) * (house[2] * 12)) - house [0],2)

###########################################################################
# Functions for Problem 8
###########################################################################
#INPUT list of numbers
#RETURN True if geometric series, False otherwise
def is_geo(xlst):
    if len(xlst) <= 2:
        return 0
    else:
        ratio = xlst[1]/float(xlst[0])
        for i in range(1, len(xlst)):
            if xlst[i]/float(xlst[i-1]) != ratio:
                return 0
        return 1



if __name__ == "__main__":
    """
    If you want to do some of your own testing in this file, 
    please put any print statements you want to try in 
    this if statement.

    You **do not** have to put anything here
    """
    # #problem 1
    # print(N(500,100,4)) 
    # print(N_t(1000))
    # print(W(10,1))
    # print(L(33.8,512,0.515))

    #problem 2
    # print(q((1,4,-21)))
    # print(q((3,6,10)))
    # print(q((1,0,-4)))

    #problem 3
    # receipt = [[1,1.45],[3,10.00],[2,1.45],[5,2.00]]
    # no_tax = [33,5,2]
    # print(amt(receipt,no_tax))

    # #problem 4
    # print(f((2,3),(6,4)))
    # print(f((1,6),(3,2)))
    # print(f((1,3),(1,5)))
 
    #problem 5
    # print(arithmetic_mean([1,2,3]))
    # print(geo_mean([2,4,8]))
    # print(har_mean([1,2,3]))
    # print(RMS_mean([1,3,4,5,7]))

    #problem 6
    # print(C(0))
    # print(C(100))
    # print(C(1000))

    #problem 7
    # house = [300000,2.9,30]
    # print(Mortgage(house))
    # print(total_paid(house))

    # #problem 8
    # xlst = [1/2,1/4,1/8,1/16,1/32]
    # print(is_geo(xlst))
    # xlst = [1,-3,9,-27]
    # print(is_geo(xlst))
    # xlst = [625,125,25]
    # print(is_geo(xlst))
    # xlst = [1/2,1/4,1/8,1/16,1/31]
    # print(is_geo(xlst))
    # xlst = [1,-3,9,-26]
    # print(is_geo(xlst))
    # xlst = [625,125,24]
    # print(is_geo(xlst))
    # print(is_geo([1/2,1/4]))