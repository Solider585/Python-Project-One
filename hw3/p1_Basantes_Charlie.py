# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 18:41:19 2020

@author: solid
"""

class NVector:
    '''
    a) constructor. If it has only one argument (besides self) assume it is a sequence of numbers
    (e.g. a tuple or list) and initialize the elements from the NVector accordingly, in a new list object. 
    
    '''
    def __init__(self, argument_1 = tuple):
        self.list = list()
        #self.vect = []
        
        if type(argument_1) is list:
            self.list = argument_1
            #print(self.list)
        elif type(argument_1) is tuple:
            for i in argument_1:
                self.list.append(i)
            #print(self.list)    
                            
                
    '''
    b) the constructor can also take two or more arguments (besides self)
    – which will be the elements of the vector. 
    huh?
    '''
    
    
    
    '''
    c) method __len__ that returns the length of the vector. 
    E.g. NVector([3,0,1, -1]).__len_() returns 4.
    Note: x.__len__() is actually invoked when we call len(x).
    
    '''
    def __len__(self):
        return len(self.list)
    
    '''
    d) the “index operator” [i], with method __getitem__(index). 
    The argument is an index (an int) into the objects element list.        
    E.g. if x== NVector([3,0,1, -1]),  then x[1]==0. 
    Indexing with negative numbers should work like list indexing with standard lists:      
        E.g. if x== NVector([3,0,1, -1]),  then x[-2]==1. 
        Note that it is not required to implement list-style slicing.
    
    '''
    def ___getitem__(self, index):
        temp = abs(index)
        try:
            return self.list[temp]
        except IndexError:
            print("Index is out of range.") 
            return None
        
    '''
    e) the indexed assignment operator [], with method __setitem__(index, value), 
    that will assign value to the element at position index.     
    E.g. if x== NVector([3,0,1, -1]). 
    The call x[2] = 5 will modify the vector to be the same as NVector([3,0,5, -1]. 
    Indexing with negative numbers should work like list indexing with standard lists.

    '''
    def __setitem__(self, index, value):
        temp = abs(index)
        
        try:
            self.list[temp] = value
            return self.list
        except IndexError:
            print("Index is out of range.") 
            return None
        
    '''
    f) __str__ method that returns the string representation of the NVector object. 
    Pick an obvious format.
    '''
    
    def __str__(self):
        string_vector = "["
        for i in self.list:
            string_vector += str(i) + " "
        string_vector += "]"             
        return string_vector
           
    '''
    g) methods __eq__ and __ne__ that take a parameter and
        return true if self is equal (respectively, not equal)
        to the parameter object, and false otherwise. 
        For __eq__ to return true, self must be compared to another NVector object and 
        corresponding elements with the same index should be equal.
    '''
    def __eq__ne__(self,compare):
        if len(self.list) == len(compare):
            print("Vectors share the same length:", len(self.list), "=", len(compare))
            
            if (self.list == compare.list):
                print("Vectors share same values too:", self.list, "=", compare.list)
                return True
            else:
                print("However, their values are different:", self.list, " ", compare.list)
                return False
        else:
            print("Vectors do not share the same length:", len(self.list), "!=", len(compare))
            return False
        
    '''
    h) method __add__ for addition with another NVector (done element-wise) 
        or with a number (applied to all elements), 
        and method __radd__ implementing “reflected” addition, as described in the book. 
        E.g.  
        NVector([3,0,1, -1]) + NVector([1,2,3,4]) results in NVector([4, 2, 4, 3])       
        NVector([3,0,1, -1]) + 10 results in NVector([13, 10, 11, 9])        
        10 + NVector([3,0,1, -1]) results in NVector([13, 10, 11, 9])
        
        not fully correct doin weird stuff
    '''
    def __add__(self, number): 
        temp = self.list
        temp_2 = number.list
        other = []
        if len(self.list) == len(number):
            for i in self.list:
                other = temp[i] + temp_2[i]
                
        else:
            return self.list + number
        
        return self.list    
    
    '''
    i) methods __mul__ and __rmul__, for scalar multiplication with another NVector or a number 
        and “reflected” multiplication. 
        If B is a number, A * B = ∑i=0 len(A)−1 Ai∗B .
        If B is another NVector,  A * B = ∑i=0 len(A)−1 Ai∗Bi 
        E.g.            
        NVector([3,0,1, -1]) * NVector([1,2,3,4]) == 3*1+0*2+1*3+(-1)*4 == 2.

    '''
    def __mul__(self):
        return None
    
def main():
    '''
    n4 = NVector([3,0,1, -1]) or NVector((3,0,1, -1)), the latter using a 4-tuple as parameter
    
    '''
    
    vector_1 = NVector([3, 0, 1, -1])
    vector_2 = NVector((3, 0, 1, -1))
    
    
    #vecter.__init__()
    print('-' * 20)
    print("test length")
    print("The length of the vector_1 is:", vector_1.__len__())
    print("The length of the vector_2 is:", vector_2.__len__())
    
    
    print('-' * 20)
    print("test getitem")
    print("vector_1[0] =", vector_1.___getitem__(0))
    print("vector_1[-2] =", vector_1.___getitem__(-2))
    print("vector_1[4] =", vector_1.___getitem__(4))
        
    print('-' * 20)
    print("test getitem 2")
    print("vector_2[0] =", vector_2.___getitem__(0))
    print("vector_2[-2] =", vector_2.___getitem__(-2))
    print("vector_2[4] =", vector_2.___getitem__(4))
    print('-' * 20)
    
    print('-' * 20)
    print("test setitem 2")
    print(vector_1.__setitem__(3, 12))
    print(vector_1.__setitem__(4, 1))
    print(vector_2.__setitem__(2, -5))
    print(vector_2.__setitem__(0, -3))
    print('-' * 20)
    
    print('-' * 20)
    print("test vector to string")
    print(vector_1.__str__())
    print(vector_2.__str__())
    print('-' * 20)
    
    print('-' * 20)
    print("test equals")
    vector_3 = NVector([3, 0, 1])
    vector_4 = NVector([-3, 0, -5, -1])
    print(vector_2.__eq__ne__(vector_1))
    print(vector_1.__eq__ne__(vector_3))
    print(vector_2.__eq__ne__(vector_4))
    
    print('-' * 20)
    print('-' * 20)
    print("test to add")
    vector_5 = NVector([3, 0, 1, -1])
    vector_6 = NVector([1, 2, 3, 4])
    print(vector_5.__add__(vector_6))
  
    
if __name__ == '__main__':
    main()   
