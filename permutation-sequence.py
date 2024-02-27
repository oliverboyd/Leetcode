# https://leetcode.com/problems/permutation-sequence/

import math

def factorial_quotients(n,k):
    array = []
    for i in range(n,0,-1):
        array.append(k // math.factorial(i))
        k = k % math.factorial(i)
    return array

def increment(array,r):
    num = 1 
    while r >= 0:
        if num in array:
            num += 1
            continue
        else:
            if r > 0:
                num += 1
            r -= 1
    return num

def get_permutation(n, k):
    quotients = factorial_quotients(n,k-1)
    quotients.append(0)
    if quotients[0] == 1:
        return "".join(str(elm) for elm in range(n,0,-1))
    else:
        array=[]
        for i in range(1,n+1):     
            array.append(increment(array,quotients[i]))
        return "".join(str(elm) for elm in array)     