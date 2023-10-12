# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 22:00:08 2020

@author: solid
"""

import pandas as pd

'''
a) Write a function called display_top_collaborations that displays the ranking of tuples 
(director, first billed actor (i.e. Actor1), and number of movies) for movies in which the 
director and actor worked together also listed in the top rated movie list. 
The list should be in descending ordered of the total number of movies that director and 
that actor worked together. For equal values the order does not matter. 

'''
def display_top_collaborations():
    #read excel files
    top_casts = pd.read_csv('imdb-top-casts.csv',header=None)
    top_casts.columns = ['Title','Year','D','A1','A2','A3','A4','A5']
    top_rated = pd.read_csv('imdb-top-rated.csv')
    cast_list = dict()
    
    for index, row in top_rated.iterrows():
        movie_title = row['Title']
        find_smae = top_casts.loc[top_casts['Title'] == movie_title]
        if ((find_smae.iloc[0]['D'],find_smae.iloc[0]['A1']) in cast_list):
            cast_list[(find_smae.iloc[0]['D'],find_smae.iloc[0]['A1'])] = cast_list[(find_smae.iloc[0]['D'],find_smae.iloc[0]['A1'])] + 1
        else:
            cast_list[(find_smae.iloc[0]['D'],find_smae.iloc[0]['A1'])] = 1
            
    colab_list = [] 
    
    for key,val in cast_list.items():
        a,b = key
        #print(key)
        #print(val)
        colab_list.append((a,b,val))
    colab_list = sorted(colab_list,key= lambda x: x[2],reverse = True)
    print("Top Collaborations:")
    #range of 5
    for x in range(5):
        print(colab_list[x])
    return colab_list
        
'''
b) Write a function called display_top_directors that displays the ranking of movie 
directors from the top grossing list ordered by the total box office money they produced
'''   
def display_top_directors():
    #read excel files
    top_casts = pd.read_csv('imdb-top-casts.csv',header=None)
    top_casts.columns = ['Title','Year','D','A1','A2','A3','A4','A5']
    top_grossing = pd.read_csv('imdb-top-grossing.csv')
    my_list = dict()
    
    for index, row in top_grossing.iterrows():
        title_of_movie = row['Title']
        money_generated = row['USA Box Office']        
        find_director = top_casts.loc[top_casts['Title'] == title_of_movie]
        
        if (find_director.iloc[0]['D'] in my_list):
            my_list[find_director.iloc[0]['D']] = my_list[find_director.iloc[0]['D']] + money_generated
        else:
            my_list[find_director.iloc[0]['D']] = money_generated
        
    top_directors_list  = []
    
    for key,val in my_list.items():
        top_directors_list.append((key, val))
    
    top_directors_list = sorted(top_directors_list,key =  lambda x: x[1], reverse = True)

    for i in range(5):
        print(top_directors_list[i])
        
    return top_directors_list  
       
        
    '''
    c) Write a main() function that tests the code from parts a) and b).

    '''
def main():
    display_top_collaborations()
    print('-' * 20)
    display_top_directors()
    
main()