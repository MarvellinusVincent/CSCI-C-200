import math

###########################################################################
# Functions for Problem 1
###########################################################################
week = {1:"Mon", 2:"Tue", 3:"Wed", 4:"Thu", 5:"Fri", 6:"Sat", 7:"Sun"}

def a(dlst):
    return dlst[2] - ((14-dlst[1])/12)

def b(dlst):
    x = a(dlst) + (a(dlst)/4) - (a(dlst)/100) + (a(dlst)/400)
    return math.floor(x)

def c(dlst):
    return dlst[1] + (12 * ((14-dlst[1])/12)) - 2


# INPUT dlst = [d,m,y]
# RETURN day the week that the given date falls on
def day(dlst):
    day = ((dlst[0] + b(dlst) + (31 * (c(dlst)/12)))%7)
    return week[day]


###########################################################################
# Functions for Problem 2
###########################################################################
#INPUT t = (a,b,c)
#RETURN return complex or real roots
def q(t):
    a = t[0]
    b = t[1]
    c = t[2]
    if (b**2) - (4*a*c) >= 0:
        real_1 = (-b-(((b**2)-(4*a*c))**0.5))/(2*a)
        real_2 = (-b+(((b**2)-(4*a*c))**0.5))/(2*a)
        r_real_1 = round(real_1,2)
        r_real_2 = round(real_2,2)
        return r_real_1,r_real_2
    else:
        not_real_1 = (-b+(((b**2)-(4*a*c))**0.5))/(2*a)
        not_real_2 = (-b-(((b**2)-(4*a*c))**0.5))/(2*a)
        cx_1 = round(not_real_1.real,2) + round(not_real_1.imag,2) * 1j
        cx_2 = round(not_real_2.real,2) + round(not_real_2.imag,2) * 1j
        return (cx_1,cx_2)



###########################################################################
# Functions for Problem 3
###########################################################################
def inner_prod(v0,v1):
    list = []
    for i in range(0,len(v0)):
        product = (v0[i] * v1[i])
        list.append(product)
    return sum(list)

def mag(v):
    return inner_prod(v,v)**0.5

def angle(v0,v1):
    return round((180/math.pi) * math.acos(inner_prod(v0,v1)/(mag(v0)*mag(v1))),2)

def match(people):
  list = []
  for i in people:
      for j in people:
        if i != j:
          new = [[i,j],angle(i,j)]
          list.append(new)
  return list

def best_match(scores):
  list = []
  for i in scores:
    list.append(i[1])
  raw = scores[list.index(min(list))]
  return raw[0][0],raw[0][1],raw[1]



###########################################################################
# Functions for Problem 4
###########################################################################
#INPUT 
#RETURN 
def intersect(d0,d1):
    x_intercept = round((d1[1] - d0[1]) / (d0[0] + (-d1[0])),2)
    y_intercept = round((x_intercept * d0[0]) + d0[1],2)
    return (x_intercept,y_intercept)



###########################################################################
# Functions for Problem 5
###########################################################################
#INPUT List of numbers
#RETURN Various means or error message
def mean(lst):
    return round(sum(lst) / len(lst) , 2)

def variance(lst):
    u = mean(lst)
    sum = 0
    for number in lst:
        sum = sum + ((number-u)**2)
    return round((1/len(lst)) * sum , 2)

def std(lst):
    return round(variance(lst)**0.5 , 2)

def mean_centered(lst):
    list = []
    u = mean(lst)
    for number in lst:
        new_number = number - u
        list.append(new_number)
    return list



###########################################################################
# Functions for Problem 6
###########################################################################
#INPUT x filters
#RETURN fixed cost
def equi(s,d):
    a = s[0] - d[0]
    b = s[1] - d[1]
    c = s[2] - d[2]
    coefficient = (a,b,c)
    return q(coefficient)
if __name__ == "__main__":
    """
    If you want to do some of your own testing in this file, 
    please put any print statements you want to try in 
    this if statement.

    You can uncomment the below print statements to test you code
    but __remember__ to comment them before submitting the final version.

    Note: Do not leave print statements outside the body of the functions.
    All print statements must be commented after you are done testing your
    code and before pushing the final version of your HW.
    """

    # #problem 1
    # print(day([14,2,2000]))
    # print(day([14,2,1963]))
    # print(day([14,2,1972]))

    #problem 2
    # print(q((3,4,2)))
    # print(q((1,3,-4)))
    # print(q((1,-2,-4)))

    # #problem 3
    # people0 = [[0,1,1],[1,0,0],[1,1,1]]
    # print(match(people0))
    # print(best_match(match(people0)))

    # people1 = [[0,1,1,0,0,0,1],
    #            [1,1,0,1,1,1,0],
    #            [1,0,1,1,0,1,1],
    #            [1,0,0,1,1,0,0],
    #            [1,1,1,0,0,1,0]]
    # print(best_match(match(people1)))
    #output is ([1, 1, 0, 1, 1, 1, 0], [1, 0, 0, 1, 1, 0, 0], 39.23)

    # v0,v1 = (2,3,-1), (1,-3,5)
    # print(angle(v0,v1)) #122

    # v0,v1 = (3,4,-1),(2,-1,1)
    # print(angle(v0,v1)) #85

    # v0,v1 = (5,-1,1),(1,1,-1)
    # print(angle(v0,v1)) #85


    # #problem 4
    # l0 = (2,3)
    # l1 = (-1/2,2)
    # print(intersect(l0,l1)) #-2/5,11/5
    # print(intersect((1,4),(-1/2,1/2)))
 
    #problem 5
    # lst = [1,3,3,2,9,10]

    # print(mean(lst))
    # print(variance(lst))
    # print(std(lst))
    # print(mean(mean_centered(lst)))

    #problem 6


