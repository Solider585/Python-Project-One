# Q2
import math

user_input = input("Input a  number greater than zero that is a whole number: ")
n = int(user_input)

def  find_Pythagorean(n):
    a = 1
    while a < n:
        #print(a)
        b = a
        while b < n:
            #print(b)
            B = math.pow(b,2)
            A = math.pow(a,2) 
            C = ((A + B))
            #print(C)
            #print(math.sqrt(C))
            c = (math.sqrt(C))
            if c % 1 == 0 and c <= n:
                print(a, b, int(c))
            b += 1
        a += 1
    
if  n > 0:
    find_Pythagorean(n)   