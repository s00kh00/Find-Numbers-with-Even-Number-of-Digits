#!/usr/bin/python36
import sys
print("Python version")
print (sys.version)

A = [32,22,7,15,867]
x=0
even_count = 0
for x in range(len(A)):
    element = A[x]
    num_digit = 0
    while element > 1:
        element = element/10
        num_digit = num_digit + 1
    if num_digit % 2 == 0:
        even_count=even_count +1
print (even_count)
        
    
