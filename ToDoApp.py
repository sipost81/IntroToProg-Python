###############################################################################
# Title: HomeInventory.py
# Owner: Tim Sipos
# Date: 04/27/2019
# Description: This script gather two inputs from the user and ask if they
#  would like to enter any additional items. This loop will continue until they
#  are ready to exit. The values are stored in a tuple in case the data
#  is to be written out to a file. Once they are ready to exit they are asked
#  if they want to write the entered data out to a file
###############################################################################

# Imports
import os

# Variables
todo_list = []
tasks = {}
filename = "listofstuff.txt"

# Open the file ToDo.txt
todo_file = open(filename)

# Read in each line and put it into the tasks dictionary
for line in todo_file:
    # This splits the data out into a list based on the comma in the line
    contents = line.split(",")

    # This is adding the data into a dictionary, also removes any unwanted spaces and carraige return
    tasks[contents[0].strip()] = contents[1].strip()
todo_file.close()

# Add each task from the dictionary to a list
for key, value in tasks.items():
    # the key and its value to the overall list of tasks
    todo_list.append([key, value])

while(True):
    print ("""
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))


    # Step 3 -Show the current items in the table
    if (strChoice.strip() == '1'):
        print(todo_list)
    
    # Step 4 - Add a new item to the list/Table
    elif(strChoice.strip() == '2'):
        new_item = input("Enter the new data in the following format 'task, priority': ")
        
        # Attempt to split the line on a comma, if it fails that means the user did not
        #  enter the correct format so input is ignored
        try:
            new_task = new_item.split(",")
            todo_list.append(new_task)
        except:
            print("The input was not correct")
    
    # Step 5 - Remove a new item to the list/Table
    elif(strChoice.strip() == '3'):
        print(todo_list)
        remove_item = input("Enter the index value of the task you want to delete, index starts at 0: ")
        
        # This removes the desired item from the list
        del todo_list[int(remove_item)]
    
    # Step 6 - Save tasks to the ToDo.txt file
    elif(strChoice.strip() == '4'):
        
        # This loops through the master list of tasks and writes out the contents to a file. 
        #  The file is overwritten by the script since we are giving users the option to remove items
        for task in todo_list:
            todo_file.write(task[0] + ", " + task[1] + "\n")
        todo_file.close()
    
    elif (strChoice.strip() == '5'):
        break #and Exit the program