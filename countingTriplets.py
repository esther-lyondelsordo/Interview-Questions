#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'getTripletCount' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER d
#

def getTripletCount(a, d):
    tripletCount = 0
    n = len(a)
    for i in range(0,n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                if ((a[i]+a[j]+a[k]) % d == 0):
                    tripletCount+=1
    return tripletCount

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a_count = int(input().strip())

    a = []

    for _ in range(a_count):
        a_item = int(input().strip())
        a.append(a_item)

    d = int(input().strip())

    result = getTripletCount(a, d)

    fptr.write(str(result) + '\n')

    fptr.close()


# Trying to be faster below but failed tests:
#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'getTripletCount' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER d
#

def waysToChooseTwo(n):
    return n*(n-1) // 2

def waysToChooseThree(n):
    return n*(n-1)*(n-2) // 6

def getTripletCount(a, d):
    tripletCount = 0
    n = len(a)
    
    # make array that holds number of elements at in index divisible by d
    remainders = [0]*d
    for elmt in a:
        remainders[elmt%d]+=1
    
    # count triplets
    for i in range(d):
        for j in range(i,d):
            k = (-i-j)%d
            if k<j:
                continue
            if i==j==k:
                tripletCount+=waysToChooseThree(remainders[i])
            elif i==j:
                tripletCount+=waysToChooseTwo(remainders[i])*remainders[k]
            elif j==k:
                tripletCount+=remainders[i]*waysToChooseTwo(j)
            else:
                tripletCount+=remainders[i]*remainders[j]*remainders[k]
    
    return tripletCount

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a_count = int(input().strip())

    a = []

    for _ in range(a_count):
        a_item = int(input().strip())
        a.append(a_item)

    d = int(input().strip())

    result = getTripletCount(a, d)

    fptr.write(str(result) + '\n')

    fptr.close()


# Stay Positive
#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'minStart' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def minStart(arr):
    rollingSum = x = 0
    for elmt in arr:
        rollingSum+=elmt
        if rollingSum<1:
            x += 1 - rollingSum
            rollingSum = 1
    return x
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = []

    for _ in range(arr_count):
        arr_item = int(input().strip())
        arr.append(arr_item)

    result = minStart(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
