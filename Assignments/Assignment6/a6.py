import math
import random as rn
import matplotlib
import matplotlib.pyplot as plt
import numpy as np


########################
# PROBLEM 1
########################

# INPUT positive integers n and k
# RETURN an integer (result of n choose k as per equation 2 in HW PDF)
def C(n, k):
    if k == 0 or k ==n:
        return 1
    else:
        return int(n / k * C(n-1,k-1))

# INPUT positive number m
# RETURN integer (the value of B(m) as per equation 4 in the PDF)
def B(m):
    if m == 0:
        return 1
    else:
        my_sum = 0
        for i in range (0,m):
            a = m + 1
            b = -C(a, i)*B(i)
            my_sum += b
        return my_sum/a





########################
# PROBLEM 2
########################

# INPUT path and file name (read the file as per the format of Table-1 (in the PDF) and) retrn the list as per the output format given below
# RETURNS list of tuples [(0,1650), (10,1750),...,(110,6870)] 
# where each tuple correspond to a particular year (year, population in that year)
def get_data(path,name):
    with open ("Assignment6/pop.txt") as theFile:
       datas = theFile.read()
    
    splitted_data = datas.split("\n")

    lst = []
    for i in splitted_data:
        year,pop = i.split()
        tupl = (int(year), int(pop))
        lst.append(tupl)
    return lst
   
datas = get_data("Assignment6", "pop.txt")

# INPUT year 0,10,20,...,110
# RETURN model population
# calculate the population it as per equation 16 in the PDF
def pop(year):
    return 1436.53*(1.01395)**year

# INPUT population data
# RETURN total error
# calculate total error as per equation 18 and 19
def error(data):
    my_sum = 0
    for i in data:
        a = (i * 10) - pop(i * 10)
        my_sum += a
    return my_sum
     


########################
# PROBLEM 3
########################

# INPUT A string
# OUTPUT boolean (True or False)
def isogram(x):
    upper = x.upper()
    list = []
    for letter in upper:
        if letter.isalpha():
            if letter in list:
                return False
            else:
                list.append(letter)
    return True

        




########################
# PROBLEM 4
########################

# INPUT A string (in hexadecimal format)
# OUTPUT An integer (decimal equivalent of the input string)
def Hex(n):
    final_hex = int(n,16)
    return final_hex



########################
# PROBLEM 5
########################

# INPUT an integer
# OUTPUT boolean (True or False)
# return True if divisible by 11 otherwise False
def div_11(x): 
    total_even = 0
    total_odd = 0
    for i in list(str(x)):
        new_list = list(str(x))
    for even in new_list[::2]:
        total_even += int(even)
    for odd in new_list[1::2]:
        total_odd += int(odd)
    total_sum = total_odd - total_even
    if total_sum == 0:
        return True
    else:
        return False






if __name__ == "__main__":
    pass
    # print("This is the code file. To see test results, please run 'a6_test.py'")
    # print("Feel free to write your own tests here. The tests you write below will not be graded.")

    ###### Problem 1
    # print(C(1, 0)) # 1
    # print(C(3, 1)) # 3
    # print(C(4, 3)) # 4

    # print(B(1)) # -0.5
    # print(B(2)) # 0.16666666


    ##### Problem 2
    ##### Code to plot the graph for error between true population and 
    # prediction from the model

    # Uncomment the below code to plot the graph for model prediction.
    # make sure to save the plot under the Assignment7 directory
    
    # total_error = round(error(data),4)
    # t = np.arange(0.0, 120.0)
    # fig,ax = plt.subplots()

    # ax.plot(t, pop(t),'g')
    # for y,p in data:
    #     ax.plot(y,p,'ro--')

    # ax.set(xlabel ="Time (Year + 1900)", ylabel=r"Pop size $\times 10^6$",
    # title = "Population Growth. Total ave error = %{0}".format(total_error))
    # ax.grid()
    # plt.show()

    
    ##### Problem 3
    # print(is_isogram("hello")) # False
    # print(is_isogram("hlo"))   # True
    # print(is_isogram(""))      # True


    # ##### Problem 4
    # print(hex_dec(C1)) # 193


    # ##### Problem 5
    # print(elevens(11)) # True
    # print(elevens(0))  # True
    # print(elevens(55)) # True