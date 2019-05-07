#-------------------------------------------------#
# Title: Assignment 06
# Dev:   Tim Sipos
# Date:  May 6th, 2019
# Description: This script presents the user with a 
#  menu and capabilities to manipulate data in a 
#  table which is data read in from a text file.
#  The script takes advantage of using a class and
#  methods to perform the necessary actions. This
#  helps reduce the code that might be repeated
#  thus increasing the maintainability of the script
#-------------------------------------------------#

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
        self.import_from_file()

    # This method imports data from the external text file
    def import_from_file(self):
        objFile = open(self.objFileName, "r")
        
        # For each line in the file it is split apart based on a comma and then the data is added 
        #  to a dictionary. That dictionary is added to a list of dictionaries
        for line in objFile:
            self.strData = line.split(",") # readline() reads a line of the data into 2 elements
            self.dicRow = {"Task":self.strData[0].strip(), "Priority":self.strData[1].strip()}
            self.lstTable.append(self.dicRow)
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
        for self.dicRow in self.lstTable:
            print(self.dicRow)
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
        objFile = open(self.objFileName, "w")
        for self.dicRow in self.lstTable:
            objFile.write(self.dicRow["Task"] + "," + self.dicRow["Priority"] + "\n")
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
        print("""
        Menu of Options
        1) Show current data
        2) Add a new item.
        3) Remove an existing item.
        4) Save Data to File
        5) Exit Program
        """)
        strChoice = str(input("Which option would you like to perform? [1 to 5] - "))

        # Show the current items in the table
        if (strChoice.strip() == '1'):
            
            # This calls the show_table method from the ToDo Class
            todo_class.show_table()

        # Add a new item to the list/Table
        elif(strChoice.strip() == '2'):
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