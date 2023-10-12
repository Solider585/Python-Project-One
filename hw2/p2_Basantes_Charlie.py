# -*- coding: utf-8 -*-
"""
Created on Wed Feb  5 22:29:31 2020

@author: solid
"""
#import math

'''
a) Write a list comprehension that returns all tuples (a,b,c), with a,b,c integers,
such that 1<=a,b,c<=100 and a2+b2=c2
 '''
#nested for loops to go through each value from 1-100 and checks if a^2+b^2 = c^2. otherwise run until loop ends
list_comprehension_a = [ (a, b, c) for a in range(1,101)  for b in range(1,101)  for c in range(1,101)  if((a*a + b*b) == (c*c)) ] #simplified
print(list_comprehension_a)
#to space out each part 
print("")


'''
b) Consider a list of strings, like this: ['one', 'seven', 'three', 'two', 'ten']. Write a list comprehension that
produces a list with tuples where the first element of the tuple is the length of an element in the initial
list, the second element of the tuple is the element of the initial list capitalized, and the resulting list
contains only tuples for strings with the length longer than three characters
''' 

strings_list = ['one', 'seven', 'three', 'two', 'ten' ,]
#finds the length of the string array, capitalizes very character. then checks the length of each word if it 
#is greater than 3 characters and prints the length of the string array, and the element with more than 3 characters 
list_comprehension_b = [ (len(strings_list[i]), strings_list[i].upper()) for i in range(len(strings_list)) if len(strings_list[i]) > 3]
print(list_comprehension_b)  
#to space out each part   
print("")


'''
c) Consider a list of full names (formatted “Firstname Lastname”), like["Jules Verne", "Alexandre
Dumas", "Maurice Druon"]. Write a list comprehension that produces a list with the full names in this
format: “Lastname, Firstname”. 
'''     

name_list = ["Jules Verne", "Alexandre Dumas", "Maurice Druon"]
#go through the string and look for the space between the first and last name. place evreything after the space first, place a comma and then place what was previously in front of the space next
#that was the last name is displayed then the first name is displayed: (last, first). since using a single list using a for-in loop to go through the whole list 
list_comprehension_c = [adjust_name[adjust_name.index(' ') + 1:] + ',' + adjust_name[0:adjust_name.index(' ')] for adjust_name in name_list]
print(list_comprehension_c)
#to space out each part 
print("")

'''
d) Write a function called concatenate that takes as parameter a separator (a string) and an arbitrary
number of additional arguments, all strings, and that returns the concatenation of all given strings using
the given separator.
'''

def concatenate(seperator, *string_list):
    list_plus_seperator = seperator.join(string_list)
    #print(list_plus_seperator)
    return list_plus_seperator #returns now

#prints them here now instead of in function
print(concatenate(': ', "one", "two", "three"))
print(concatenate(' and ', "Bonny", "Clyde"))
print(concatenate(' and ', "single"))