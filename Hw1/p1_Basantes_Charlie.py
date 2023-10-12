# Problem 1 Quadratic Equation Ax^2 + bx + c = 0

import math
import matplotlib.pyplot as plt

# A = a * math.pow(x,2)


#user_Input = 'y'

user_Input = input("Do you want to use my quadratic formula y or n: ")
print(user_Input)

if user_Input == 'y' or user_Input == 'Y':
    user_input =' '
    while user_input != 'n':
        a = input("Value of a: ")
       # print(b)
        A = float(a)
        print(A)
        
        b = input("Value of b: ")
        print(b)
        B = float(b)
        print(B)
        
        c = input("Value of c: ")
        print(c)
        C = float(c)
        print(C)
        
        b_squared = math.pow(B,2)
        is_real = (b_squared) - (4 * A * C)
        
        
        if is_real < 0 or A == 0:
            print("no real soution")
        elif is_real == 0:
            x_one = ((-B) + math.sqrt(is_real)) /  (2 * A)
            x_two = x_one
            print(x_one, "ond", x_two)
            print("One solution: ", x_one)
        else:
            x_one = ((-B) + math.sqrt(is_real)) /  (2 * A)
            print(x_one)
            x_two = ((-B) - math.sqrt(is_real)) /  (2 * A)
            print(x_two)   
            print("Two solutions: ", x_one, "and ", x_two)
            
        plt.scatter(x_one, x_two)
        plt.show()
            
        user_input = input("Do you want to run again y or n?: ")
        print(user_input)
       
        