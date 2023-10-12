# -*- coding: utf-8 -*-
"""
Created on Wed Feb  5 20:21:27 2020

@author: solid
"""

'''
This function reads the file indicated by the first parameter and writes its 
lines prefixed by the line number to the file represented by the second parameter
'''

def line_number(file1,file2):

  f1=open(file1, "r")
  f2 = open(file2, "w")
  try: 
      for x in f1.readlines():
          f2.write(x)
      f2.close()
  except: 
      print("text file is empty,or does not exist.")

def parse_functions(py_file):
    function_list=[]
    try:
        with open(py_file,"r") as read_file:
            line_number = 1
            function_name =''
            function_body =""
            for line in read_file.readlines():
                if "def" in line:
                    
                    if("#" in line):
                          tup=line_number,function_name,function_body
                          print(tup)
                          function_list.append(tup)
                    else:
                          function_body=""
                    
                    function_name = line[line.index("def")+3:line.index('\n')].strip()
                    function_body = line

                else:
                    function_body+=line
                line_number+=1
            tup=line_number,function_name,function_body
            function_list.append(tup)
        return tuple(function_list)
    except:
        print('Unable to read/write the file:')



def main():
    #got this to work
    line_number('test.txt', 'test.py.txt')
    #thinks every function is main...
    print(parse_functions('test.py'))
    
    
main()
