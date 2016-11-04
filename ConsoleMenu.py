'''
Created on 31 oct. 2016

@author: Camelia
'''
def Menu():
    string = "\n"
    string += "Choose option: \n"
    string += "1-Add a new entry; \n"
    string += "2-Remove a specific entry; \n"
    string += "3-List; \n"
    string += "4-Obtain different characteristics of participants; \n"
    string += "5-Establich the podium; \n"
    string += "6-Undo; \n"
    string += "x-Exit;\n"
    print(string)

from operationsRequired import*
from read import*
from Tests import*
from allCommands import*

def readCommand():
    command = input("Enter the command: ")
    return command

def AddUI():
    string = "OptionS for adding the data entered: \n"
    string += "1-Simple add to the list; \n"
    string += "2-Insert at a specific position in list."
    string += "x-exit; \n"
    print(string)

def addMenu(l):
    data = ReadNewData()
    AddUI()
    AddPosibility = ["1", "2", "0"]
    choice = readCommand()
    if choice not in AddPosibility:
        print("You entered an invalid command, try again.\n")
    elif choice == "x":
        return
    elif choice == "1":
        AddResultsToList(l, data)
    elif choice == "2":
        while True:
            try:
                res = readPosition()
                if res == -1:
                    break
                else:
                    if positionIsValid(res, len(l)):
                        InsertResultsInList(l, data, res)
                        break
                    else:
                        print("You entered an invalid position, try again.\n")
            except ValueError:
                print("Invalid position.")


def positionIsValid(pos, length):
    if pos != int(pos):
        return False
    if pos < 0 or pos > length:
        return False
    return True

def readPosition():
    res = int(input("Enter the position at which the new values will be added(-1 to exit): \n"))
    return res
    
def DeleteUI():
    string = "Enter your command for deleting options: \n"
    string += "1-Remove results at a specific position; \n"
    string += "2-Remove results from a specific position to another; \n"
    string += "3-Replace certain results; \n"
    string += "4-Delete less than, greater than or equal to a given value; \n"
    string += "x - Exit; \n"
    print (string)

def readPositionDelete():
    pos = int(input("Enter the position at which the results will be set to 0, 0, 0: \n"))
    return pos

def readPosDelete2():
    while True:
        try:
            pos = int(input("Position: "))
            return pos
        except ValueError:
            print("Invalid index.")
def readProblemIndex():
    while True:
        try:
            index = int(input("Give the index of the problem for which the results will be changed: \n"))
            return index
        except ValueError:
            print("You entered an invalid index, try again.\n")

def readPosDelete3Replacing():
    while True:
        try:
            pos = int(input("Give the position in the list at which the results will be changed: "))
            return pos
        except ValueError:
            print("Invalid position, try again.\n")

def MenuDelete3Replacing(l):
    position = readPosDelete3Replacing()
    if positionIsValid(position, len(l)):
        problemIndex = [1, 2, 3]
        while True:
            problemInd = readProblemIndex()
            if problemInd not in problemIndex:
                print("You entered an invalid problem index, try again.\n")
            else:
                print("Enter the grade you want to replace the actual one with: ")
                grade = readGrade()                                     
                ReplaceDatesAtPositionGiven(position, l, problemInd, grade)
                break
            break                     
    else:
        print("You entered a position that exceeds the limits of the list, try again.\n")

def MenuDelete1(l):
    while True:
        try:   
            pos = int(readPosDelete2())
            if positionIsValid(pos, len(l)):
                RemoveAtPositionGiven(l, pos)
                break
            else:
                print("You entered an invalid position, try again.\n")
        except ValueError:
            print("Invalid position.")

def MenuDelete2(l):
    pos1=0
    pos2=0
    print("Enter the starting position of the replacing process: ")
    pos1 = readPosDelete2()
    if positionIsValid(pos1, len(l)):
        while True:
            print("Enter the ending position of the replacing process: ")
            pos2 = readPosDelete2()
            if positionIsValid(pos2, len(l)):
                break
            else:
                print("Position 2 of your entry exceeds the limits of the list, try again. \n")
    else:
        print("Position 1 of your entry exceeds the limits of the list, try again. \n")
    if pos1 <= pos2:
        RemoveFromStartToEnd(l, pos1, pos2)
    else:
        print("Invalid indexes. \n")
    
def uiDeleteThan():
    string = ""
    string += "= - Delete equal to; \n"
    string += "< - Delete less than; \n"
    string += "> - Delete greater than; \n"
    string += "x - exit command;\n"
    print(string)

def MenuDeleteThan(resultsList):
    choice  = readCommand()
    DeletePossibilityThan = ["<", "=", ">", "x"]
    if choice in DeletePossibilityThan:
        if choice == "x":
            return
        else:
            while True:
                try:
                    grade = int(input("Enter the grade related to which the results will be modified: "))
                    if grade > 10 or grade < 0:
                        print("Invalid grade.\n")
                    else:
                        if choice == ">":
                            RemoveGreaterThan(resultsList, grade)
                            break
                        elif choice == "<":
                            RemoveLessThan(resultsList, grade)
                            break
                        else:
                            RemoveEqualTo(resultsList, grade)
                            break
                except ValueError:
                    print("Invalid grade.\n")
    else:
        print("The command is invalid.\n")

def deleteMenu(l):
    DeletePossibility = ["1", "2", "3", "4", "x"]
    choice = readCommand()
    if choice == "x":
        return
    elif choice == "1":
        MenuDelete1(l)
    elif choice == "2":
        MenuDelete2(l)
    elif choice == "3":
        MenuDelete3Replacing(l)
    elif choice == "4":
        uiDeleteThan()
        MenuDeleteThan(l)
    else:
        print("Invalid command. ")

def listUI():
    string = ""
    string += "1 - print all results; \n"
    string += "2 - print the sorted list of results; \n"
    string += "3 - print the list of grades with average less than, greater than or equal to a given value; \n"
    string += "x - exit; \n"
    print (string)

from copy import deepcopy

def listThanUI():
    string = ""
    string += "= - List equal to; \n"
    string += "< - List less than; \n"
    string += "> - List greater than; \n"
    string += "x - exit command;\n"
    print(string)


def listThanMenu(l):
    ops = ["=", ">", "<", "x"]
    listThanUI()
    term = readCommand()
    if term in ops:
        if term == "x":
            return
        else:
            try:
                grade = int(input("Enter the grade related to which the results will be displayed: "))
                if grade > 10 or grade < 0:
                    print("Invalid grade.\n")
                if term == "<":
                    if len(LessThan(l, grade)) == 0:
                        print("There are no such entries.\n")
                    else:
                        ListGrades(LessThan(l, grade))
                elif term == ">":
                    if len(GreaterThan(l, grade))==0:
                        print("There are no such entries.\n")
                    else:
                        ListGrades(GreaterThan(l, grade))
                else:
                    if len(EqualTo(l, grade)) == 0:
                        print("There are no such entries.\n")
                    else:
                        ListGrades(EqualTo(l, grade))
            except ValueError:
                print("Invalid grade.\n")
    else:
        print("Invalid command.\n")

def listMenu(l):
    listPossibilities = ["1", "2", "3", "x"]
    choice = readCommand()
    if choice == "x":
        return
    elif choice == "1":
        listCommandOP(l)
    elif choice == "2":
        list2 = deepcopy(l)
        ListGrades(sorte(l))
    elif choice == "3":
        listThanMenu(l)

def charactUI():
    res = ""
    res += "1 - obtain the average of averages from a psition to another; \n"
    res += "2 - obtain the lowest average score from a position to another; \n"
    print(res)

def ObtainCharacteristicsMenu(l):
    charactUI()
    options = ["x", "1", "2"]
    op = readCommand()
    if op in options:
        if op == "x":
            return
        else:
            while True:
                try:
                    pos1 = int(input("Enter the first index of the interval: "))
                    pos2 = int(input("Enter the second index of the interval: "))
                    if pos1 < 0 or pos2 < 0 or pos1 > 10 or pos2 > 10 or pos1 >= pos2:
                        print("Invalid indexes.")
                    else:
                        if op == "1":
                            print("The average of averages is: ", AverageOfAveragesBetweenPositions(l, pos1, pos2))
                            break
                        elif op == "2":
                            print("The lowest average between the given positions is: ",MinOfAveragesBetweenPositions(l, pos1, pos2) )
                            break
                except ValueError:
                    print("Invalid given indexes.\n")
    else:
        print("Invalid command.\n")

def PodiumUI():
    string = ""
    string += "1 - Top of a given number of participants: \n"
    string += "2 - Top of a given number of participants for a certain problem; \n"
    string += "x - exit; \n"
    print(string)

def PodiumGradeUI():
    string = ""
    string += "p1 - the first problem; \n"
    string += "p2 - the grade for the second problem; \n"
    string += "p3 - the grade for the third problem; \n"
    string += "x - exit; \n"
    print (string)

def PodiumMenu(l):
    PodiumUI()
    commandsAV = ["1", "2", "x"]
    com = readCommand()
    if com in commandsAV:
        if com == "x":
            return
        else:
            while True:
                try:
                    n = int(input("Give the number of participants of the displayed top: "))
                    if n < 0 or n > len(l):
                        print("Invalid number of participants. \n")
                    else:
                        if com == "1":
                            print("The top required is:\n", ListGrades(ReturnTopNStudents(l, n)))
                            break
                        elif com == "2":
                            index = ["p1", "p2", "p3", "x"]
                            PodiumGradeUI()
                            grade = readCommand()
                            if grade in index:
                                if grade == "x":
                                    break
                                elif grade == "p1":
                                    print("The top for the first problem is: \n",TopNGradeIndexed(l, 0, n))
                                    break
                                elif grade == "p2":
                                    print("The top for the second problem is: \n",TopNGradeIndexed(l, 1, n))
                                    break
                                elif grade == "p3":
                                    print("The top for the third problem is: \n",TopNGradeIndexed(l, 2, n))
                                    break
                            else:
                                print("Invalid grade index.\n")
                            
                except ValueError:
                    print("Invalid number of participants.\n ")
    else:
        print("Invalid entered command.\n ")

def undoMenu(l, undoList, nrOfUndoes):
    l, undoList, nrOfUndoes = backup(l, undoList, nrOfUndoes)
    print("Operation undone. \n")

def Main():
    l = []
    TestInit(l)
    uList = []
    nrOfUndoes = -1;
    gradesList2 = deepcopy(l)
    uList = uList+[gradesList2][:]
    nrOfUndoes = int(nrOfUndoes)+1
    while True:
        Menu()
        commandsAvailable = ["x", "1", "2", "3", "4", "5", "6"]
        command = readCommand()
        if command not in commandsAvailable:
            print("You entered an invalid command, try again.\n")
        elif command == "x":
            break
        elif command == "1":
            while True:
                addMenu(l)
                gradesList2, uList, nrOfUndoes = backup(l, uList, nrOfUndoes)
                break
        elif command == "2":
            if len(l)==0:
                print("The option for deleting is unavailable since the list is empty.\n")
            else:
                while True:
                    DeleteUI()
                    deleteMenu(l)
                    gradesList2, uList, nrOfUndoes = backup(l, uList, nrOfUndoes)
                    break
        elif command == "3":
            listUI()
            listMenu(l)
        elif command == "4":
            ObtainCharacteristicsMenu(l)
        elif command == "5":
            PodiumMenu(l)
        elif command == "6":
            if nrOfUndoes < 0:
                print("There is no operation to be undone.\n")
            else:
                l, uList, nrOfUndoes = undo(l, uList, nrOfUndoes)
        else:
            print("Invalid command. \n")
