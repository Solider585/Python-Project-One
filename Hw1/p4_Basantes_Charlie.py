# Q4

import math
import matplotlib.pyplot as plt

def plot_function(fun_str, domain, ns):
    xs_list = (domain[1] - domain[0]) / ns
    min_x = domain[0]
    max_x = domain[1]
    xs = [min_x]
    
    while min_x <= max_x:
        min_x += xs_list
        xs.append(min_x)
    ys = []
    
    for x in xs:
        ys.append(eval(fun_str))
    print("{:>10}     {:>10}".format('xs', 'ys'))
    print("----------------------------------------")
    
    for i in range(len(xs)):
        print("x={:>10}     y={:>10}".format(xs[i],ys[i]))
        
        plt.plot(xs,ys)
        plt.show()
        
        
def main():
    fun_str=input("Enter a function with variable x: ")
    n=int(input("Enter number of samples: "))
    x_min=float(input("Enter xmin: "))
    x_max=float(input("Enter xmax: "))
   
    plot_function(fun_str,(x_min,x_max),n)
    
    
    
main()