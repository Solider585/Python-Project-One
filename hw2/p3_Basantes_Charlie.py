# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 19:06:25 2020

@author: solid
"""

'''
a) Write a function that adds a contact to a contact list. If the contact name existed before in the list then
it will be changed to the new entry and the function returns False. Otherwise, the function should
return True.
'''
#change, contacts being used as parameter
def add_contacts(name, nick_name, phone_number, contacts):
    
    for i in range(len(contacts)):
        #checking if anything is existed before, change it, return false
        if(contacts[i][0] == name or  contacts[i][1] == nick_name or contacts[i][2] == phone_number):
            contacts[i] = (name,nick_name,phone_number)
            return False
    contacts.append((name, nick_name, phone_number))
    #sort alphabetically
    contacts.sort(key = lambda x: x[0])
    return contacts

'''
b) Write a function that removes a contact from a contact list. If the contact name existed before in the
list then the function returns True. Otherwise, the function should return False.
'''
#change, contacts being used as parameter
def remove_contacts(name, nick_name, phone_number, contacts):
    remove = 0
    contact_found = False
    #go through the list
    for i in range(len(contacts)):
        #see if contact already exists within the list and if found remove it
        if(contacts[i][0] == name or  contacts[i][1] == nick_name or contacts[i][2] == phone_number):
            remove = i
            contacts.pop(remove)
            contact_found = True
        else:
            contact_found = False
    
    return contact_found

'''
c) Write a function that finds a contact tuple from a contact list by passing the contact name or contact
nickname. Use default parameter values to deal with this choice. The function returns the tuple if the
contact is found and returns None otherwise
'''  
#None  is equivalent to a null ptr  
def find_contact_byname_or_nickname(name = None, nick_name = None, *contacts):
      if name is not None:
          for i in contacts:
              if name in i:
                  return i
          return i
              
      if nick_name is not None:
          for i in contacts:
              if nick_name in i:
                  return i
          return None
      
'''        
d) Write a function that saves a contact list to a .CSV file. The function takes as parameter the file
name. The CSV file format must have name, nickname, phone# on a line for each contact in the list.
'''
#change, contacts being used as parameter so it know what it is
def save_csv_file(file_name, contacts):
    #open takes agrument file to open, and write indicated with w and writes into the file
    file = open(file_name,"w")
    file.write("name, nick_name, phone_number\n")
    for i in contacts:
        #unsure how to use join() so left it alont since this still works
        file.write("{}, {}, {}\n".format(i[0], i[1], i[2]))

'''
e) Write a function that reads a contact list from a .CSV file with the format described for part d). The
function takes as parameter the file name and returns the contact list object (… sorted alphabetically).
'''
def read_csv_file(file_name):
    #Open takes agrument file name, and read indicated with r and reads the contents of the filefile
    file = open(file_name, "r")
    read = file.readline()
    list_of_contacts = []
    
    while(read):
        list_of_contacts.append(tuple(read.split(",  ")))
        read = file.readline()
    #sort the list
    list_of_contacts.sort(key = lambda x: x[0])
    return  list_of_contacts

'''
f) Write a main function that tests all the functions above.
'''

def main():
    contacts = [] #no longer a global variable, whoops, fixed that, will be added as extra parameter
    try:
        add_contacts("Earl Simmons", "DMX", "305-1010101",contacts)
        add_contacts("Cardie B", "Belcalis", "305-4399521",contacts)
        add_contacts("Beyonce Knowles", "bey" , "561-1234321",contacts)       
        print("\n Contacts added succussfully.")
        print(contacts)
    except:
        print("There was an error while adding a contact.\n")
        
    to_remove = input("Would you like to test remove contact from the list?: ")
    if(to_remove == 'yes' or to_remove == 'Yes'):
        try:
            remove_contacts("Earl Simmons", "DMX", "305-1010101", contacts)
            print("\n Contact was removed successfully.")
            print(contacts)
        except:
            print("There was an error when attempting to remove the contact.\n")
    
    add_contacts("Earl Simmons", "DMX", "305-1010101", contacts)
    
    try:
        find_contact_byname_or_nickname("Beyonce Knowles", "bey", contacts)
        print("contact found")
        print(find_contact_byname_or_nickname("Beyonce Knowles", "bey", contacts))
        save_csv_file("contacts_file.csv", contacts)
        print(read_csv_file("contacts_file.csv"))
    except:
        print("Unable to find the contact")
        
'''
testing all functions
'''        
main()        