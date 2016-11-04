'''
Created on 31 oct. 2016

@author: Camelia
'''
from ConsoleCommands import*
from ConsoleMenu import*

def contr ():
    string = ""
    string += "Which UI do you want to use? Type 1 for command based and 2 for menu based respectively.\n"
    print(string)
    try:
        choice = int(input(""))
        if choice == 1:
            start()
        elif choice == 2:
            Main()
        else:
            print("Invalid option.\n")
    except ValueError:
        print("Invalid option.\n")

contr()
