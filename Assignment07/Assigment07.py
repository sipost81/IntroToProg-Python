#-----------------------------------------------------#
# Title: Assignment 07
# Dev:   Tim Sipos
# Date:  May 13th, 2019
# Description: This script is based on assignment 06,
#  this had improvements to the menu system validation
#  as well as importing and exporting the data in a 
#  pickle format. The script attempts to import the file 
#  as a pickle object, if the file is not in the correct 
#  format the script will just proceed without importing 
#  anything. If the user creates new items and saves the 
#  info it will be exported in the pickle format.
#-----------------------------------------------------#

# Modules to import:
import pickle
import os
import sys

# This class contains the necessary variables that are commonly reused.
#  It also has the methods that can be used to manipulate the data
class ToDo:

    # This method initalizes the variables to be used. The last item is
    #  a call to a method to import the data from the text file and 
    #  populate the variables
    def __init__(self):
        self.objFileName = "listofstuff.txt"
        self.strData = ""
        self.dicRow = {}
        self.lstTable = []
        self.pickle_obj = None
        self.import_from_file()

    # This method imports data from the external text file
    def import_from_file(self):

        # If the expected file exists at the start it will be attmpted for import
        if os.path.exists(self.objFileName):
            # Create an object for opening the file in read-only and Binary mode
            objFile = open(self.objFileName, "rb")
            
            # This will try to load the data stored in the file. If it is a valid pickle file this will succeed
            try:
                self.pickle_obj = pickle.load(objFile)
                self.lstTable = self.pickle_obj
            
            # If the file is not a valid pickle formatted file the attempt will fail and the script will exit
            except:
                sys.exit("The format of the file is not a valid pickle file, the script is exiting")
            objFile.close()

    # This method shows the contents of the table
    def show_table(self):
        print("******* The current items ToDo are: *******")
        
        # This prints the contents of the table, each row is a dictionary
        for row in self.lstTable:
            print(row["Task"] + "(" + row["Priority"] + ")")
        print("*******************************************")
        return

    # This method adds the provided data to the table
    def add_to_table(self, strTask, strPriority):
        # Create a dictionary with the provided data
        self.dicRow = {"Task":strTask,"Priority":strPriority}
        
        # Appends the dictionary to the existing list
        self.lstTable.append(self.dicRow)
        print("Current Data in table:")
        return

    # This method removes the specified item from the table if the item exists
    def remove_from_table(self, strKeyToRemove, intRowNumber, blnItemRemoved):
        
        # Loop through the table and if a match for the string is found it is 
        #  removed otherwise the loop continues until all rows have been checked.
        while(intRowNumber < len(self.lstTable)):
            
            # If the string to remove is found in the list of dictionaries that list index is removed
            if(strKeyToRemove == str(list(dict(self.lstTable[intRowNumber]).values())[0])): #the values function creates a list!
                del self.lstTable[intRowNumber]
                blnItemRemoved = True
            #end if
            intRowNumber += 1
        #end for loop
        #5b-Update user on the status
        
        # This simply reports if the task was found an removed
        if(blnItemRemoved == True):
            print("The task was removed.")
        else:
            print("I'm sorry, but I could not find that task.")
        return

    def write_to_file(self):
        # Create an object for the file to be written out as binary
        objFile = open(self.objFileName, "wb")
        # for self.dicRow in self.lstTable:
        #     objFile.write(self.dicRow["Task"] + "," + self.dicRow["Priority"] + "\n")
        pickle.dump(self.lstTable, objFile)
        objFile.close()
        return

# This is the main function and will provide the user the menu and loop the 
#  menu performing the desired task selected by the user
def main():

    # This is initializing the ToDo class, nothing is passed in since the imported text 
    #  file is used to initialize the necessary variables
    todo_class = ToDo()

    # This keeps looping the menu until the user chooses to exit the script
    while(True):
        input_valid = False

        print("""
        Menu of Options
        1) Show current data
        2) Add a new item.
        3) Remove an existing item.
        4) Save Data to File
        5) Exit Program
        """)
        strChoice = input("Which option would you like to perform? [1 to 5] - ")

        # This try block is validating that the input value is a digit and is within the accepted range
        strChoice = strChoice.strip()
        try:
            # Checks to ensure user input a digit
            strChoice.isdigit() 

            # Checks to ensure value is within accept range for menu
            if 0 <= int(strChoice) <= 5:
                pass
            else:
                # If the value is not correct an exception is raised
                raise Exception("Incorrect value used")
            input_valid = True
        
        # The the input data is not valid than the user is prompted with the same menu and input options
        except:
            print("The number input is not valid, please try again")
            input_valid = False

        if input_valid:
            # Show the current items in the table
            if (strChoice == '1'):
                
                # This calls the show_table method from the ToDo Class
                todo_class.show_table()

            # Add a new item to the list/Table
            elif(strChoice == '2'):
                # Get user input
                strTask = str(input("What is the task? - ")).strip()
                strPriority = str(input("What is the priority? [high|low] - ")).strip()
                
                # This calls the add_to_table method from the ToDo Class and passes in the user input
                todo_class.add_to_table(strTask,strPriority)

                #Show the current items in the table
                todo_class.show_table()
                continue #to show the menu

            # Remove a new item to the list/Table
            elif(strChoice == '3'):
                blnItemRemoved = False #Creating a boolean Flag
                intRowNumber = 0

                todo_class.show_table()
                # This gets the users input of the string to remove
                strKeyToRemove = input("Which TASK would you like removed, enter the name? - ")

                # This calls the remove_from_table method from the ToDo Class and passes in the user input
                todo_class.remove_from_table(strKeyToRemove, blnItemRemoved, intRowNumber)

                #Show the current items in the table
                todo_class.show_table()
                continue #to show the menu

            # Save tasks to the ToDo.txt file
            elif(strChoice == '4'):
                #Show the current items in the table
                todo_class.show_table()

                #Ask if they want save that data
                if("y" == str(input("Save this data to file? (y/n) - ")).strip().lower()):
                    # This calls the write_to_file method from the ToDo Class
                    todo_class.write_to_file()
                    input("Data saved to file! Press the [Enter] key to return to menu.")
                else:
                    input("New data was NOT Saved, but previous data still exists! Press the [Enter] key to return to menu.")
                continue #to show the menu
            elif (strChoice == '5'):
                break #and Exit the program

# This is what is ran by pyhton when you start the script. This in turn calls the main function
if __name__ == '__main__':
    main()