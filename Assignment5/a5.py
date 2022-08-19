import math
import random as rn
from re import A
from xml.etree.ElementTree import TreeBuilder


########################
# PROBLEM 1
########################

#INPUT positive number n
#RETURN log of number base 2
def log_2(n):
    return(math.log(n))/(math.log(2))

#INPUT list of immutable objects
#RETURN list of probability distribution
def makeProbability(xlst):
    dict = {}
    lst = []
    for i in xlst:
        if i in dict.keys():
            dict[i]+=1
        else:
            dict[i]=1
    for key in dict.keys():
        dict[key] = dict[key]/len(xlst)
    for j in dict.keys():
        lst += [dict[j]]
    return lst

#INPUT probability distribution
#RETURN non-negative number entropy
# You CANNOT use count()
def entropy(xlst):
    # Step 1: Get the probability of each element
    # Step 2: Get summation of entropy function
    # Step 3: Round summation to 2 decimal places
    y = 0
    for i in makeProbability(xlst):
        x = i*log_2(i)
        y += x
        e = -(y)
    return round(e,2)






########################
# PROBLEM 2
########################

#INPUT list of 0s 1s
#OUTPUT longest list of 1s
def L(x):
    count,max_val = 0,0
    for i in x:
        count = count +1 if i == 1 else 0
        max_val = max(count, max_val)
    return max_val





########################
# PROBLEM 3
########################

#INPUT non-negative integer
#OUTPUT True if divisible by 9, False otherwise
# You CANNOT use modulus (%) AND you CANNOT directly divide by 9
def div_9(x):
    total = 0
    t_total = 0
    for each_digit in str(x):
        total = total + int(each_digit)
    for final_digit in str(total):
        t_total = t_total + int(final_digit)
    if t_total == 9 or t_total == 0:
        return True
    else:
        return False

        




########################
# PROBLEM 4
########################

#INPUT set of recurrence equations
#OUTPUT implement recursively, tail recursive generator
def p(n):
    if n == 0:
        return 10000
    else:
        return p(n-1) + 0.02 *p(n-1)

def p_t(n,v=0):
    if n==0:
        return v
    else:
        return p(n-1) + 0.02 *p(n-1)

def p_g():
    a = 10000
    while True:
        yield a 
        a = a + 0.02*a
    



def c(n):
    if n ==1:
        return 9
    else:
        return 9*c(n-1) + 10**(n-1) - c(n-1)

def c_t(n,v=0):
    if n ==v:
        return 9
    else:
        return 9*c(n-1) + 10**(n-1) - c(n-1)

def c_g():
    b = 1
    while True:
        yield b
        b = 9*b + 10**b - b



def d(n):
    if n==0:
        return 1
    else:
        return 3*d(n-1) + 1

def d_t(n,v=1):
    if n==0:
        return v
    else:
        return 3*d(n-1) + 1

def d_g():
    b = 1
    while True:
        yield b
        b = 3*b + 1




########################
# PROBLEM 5
########################

#INPUT list of numbers
#OUTPUT list sorted ascending using potato-smith

#INPUT list of numbers
#OUTPUT return sorted ascending
def insertion(a):
    i = 1
    while i < len(a):
        j = i
        while j >0:
            if a[j] < a[j-1]:
                a[j] = a[j-1]
                a[j-1] = a[j]
            j-=1
        i += 1
    return a

#INPUT list of numbers
#OUTPUT sorted list ascending using potato and insertion
def potato(x): 
    size = 2
    length = len(x)
    while size < length:
        list = []
        for i in range (0,length,size):
            list +=insertion(x[i:i+size])
        x = list
        size = size*2
        x = insertion(x[0:])
        return x





########################
# PROBLEM 6
########################

#INPUT list of numbers
#OUTPUT  [a,b,c] where:
#    a = start index
#    b = end index
#    c = maximal sum of these indices
# You may use sum(list)
# Be cautious to use sum correctly - don't use it as a variable. It's a built-in function name.
def msi(x):
    [start,stop,max] = [0,0,0]
    for i in range (len(x)):
        for j in range (i+1, len(x)):
            my_sum = sum (x[i:j+1])
            if my_sum > max:
                max = my_sum
                start = i
                stop = j
    return [start,stop+1,max]





########################
# PROBLEM 7
########################

#INPUT positive number w/ two decimal places
#OUTPUT [q,d,n,p] which is the minimal amount of coins needed
def dollars(x):
    q = int(round(x,2)//0.25)
    d = int(round((x-0.25*q),2)//0.10)
    n = int(round((x-0.25*q-0.1*d),2)//0.05)
    p = int(round((x-0.25*q-0.1*d-0.05*n),2)//0.01)
    return [q,d,n,p]





if __name__ == "__main__":
#     # Feel free to add your own tests here to help with error handling. 
#     print("This is the code file. To see test results, please run 'test_a5.py'")
#     print("Feel free to write your own tests here. The tests you write below will not be graded.")

    # #Problem 1
    # s0 = ["a", "b", "a", "c", "c", "a"]
    # print(entropy(s0))
 
    # #Problem  2
    # x = [0,1,1,1,0,0,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
    # print(L(x))

    # #Problem 3
    # xlst = [99,0,18273645,22,27]
    # for i in xlst:
    #     print(div_9(i))

    # Problem 4
    # for i,j in zip(range(10),p_g()):
    #     print(i,p(i),p_t(i),j)
    '''
    0 10000 10000 10000
    1 10200.0 10200.0 10200.0
    2 10404.0 10404.0 10404.0
    3 10612.08 10612.08 10612.08
    4 10824.3216 10824.3216 10824.3216
    5 11040.808031999999 11040.808031999999 11040.808031999999
    6 11261.62419264 11261.62419264 11261.62419264
    7 11486.8566764928 11486.8566764928 11486.8566764928
    8 11716.593810022656 11716.593810022656 11716.593810022656
    9 11950.925686223109 11950.925686223109 11950.925686223109
    '''
    # for i,j in zip(range(1,10),c_g()):
    #     print(i,c(i),c_t(i),j)
    '''
    1 9 9 9
    2 82 82 82
    3 756 756 756
    4 7048 7048 7048
    5 66384 66384 66384      
    6 631072 631072 631072   
    7 6048576 6048576 6048576
    8 58388608 58388608 58388608
    9 567108864 567108864 567108864
    '''
    # for i,j in zip(range(10),d_g()):
    #     print(i,d(i),d_t(i),j)
    '''
    0 1 1 1
    1 4 4 4
    2 13 13 13      
    3 40 40 40      
    4 121 121 121   
    5 364 364 364   
    6 1093 1093 1093
    7 3280 3280 3280
    8 9841 9841 9841
    9 29524 29524 29524
    '''
    #Problem 5
    # lst = [rn.randint(0,100) for _ in range(rn.randint(1,20))]

    # print(lst)
    # print(potato(lst))
    
    
    #Problem 6

    # x = [7, -9, 5, 10, -9, 6, 9, 3, 3, 9]
    # data = [(-1)**rn.randint(0,1)*rn.randint(1,10) for _ in range(10)]
    # print(msi(x))
    # print(data)
    # print(msi(data))

    #Problem 7
    # xlt = [2.24,1.19,4.16,1.01,1.10,2.00]
    # for i in xlt:
    #     print(dollars(i))
