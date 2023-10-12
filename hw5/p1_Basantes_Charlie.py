# -*- coding: utf-8 -*-
"""
Created on Sun Apr  1 15:47:13 2020

@author: solid
"""
#import math

#Part A
class RndSeq:
    
    def __init__(self, x0, n):
        self.x0 = x0
        self.n = n
        self.m = pow(2,32)
        self.a = 22695477
        self.c = 1
        self.count = 0
        
    def  __iter__(self):  
        self.x = self.x0
        return self
                
    def __next__(self):        
        
        #Should run infinitly if n is a negative number
        self.count += 1
        if self.count > self.n and self.n >= 0:
            raise StopIteration
        else:
            self.x = (self.a * self.x + self.c) % self.m
        
        return self.x
    
#Part B    
def rnd_gen(x0, n):
    m = pow(2,32)
    a = 22695477
    c = 1
    x = x0
    count = 0
    
    #runs infinitly if n is negative
    while count < n or count > n:
        x = (a * x + c) % m
        yield x
        count += 1

print("Class RndSeq Sequence method: ")
rnd = RndSeq(1, 10)
print([i for i in rnd])    
print()       
print('-' * 20)

print("Generator rnd_gen method: ")
print([i for i in rnd_gen(1, 10)])
print(list(rnd_gen(1,3)))      
print()
print('-' * 20)

rnd = RndSeq(1,2)
it = iter(rnd)
print(next(it))
print(next(it))
print("if I call next() one more time, program will raise StopIteration and exit, so I commented it out.")
#print(next(it))

    
def main():
    print('-' * 20)
    print()
    print("Printing lists with the first 10 random numbers with seed 2")
    print()
    print("Class RndSeq Sequence method: ")
    rnd = RndSeq(2, 10)
    for i in rnd:
        print(list(rnd))
        
    print('-' * 20)
    print("Generator rnd_gen method: ")
    print(list(rnd_gen(2,10)))
        
    
if __name__ == "__main__":
    # execute only if run as a script
    main()
