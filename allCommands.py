'''
Created on 31 oct. 2016

@author: Camelia
'''
from operationsRequired import *

def ValidParameters(command, parameters):
    x = len(parameters)
    if command == "add":
        if x == 3:
            return True
        else:
            return False
    if command == "insert":
        if x == 5:
            return True
        else:
            return False
    if command == "replace":
        if x == 4:
            return True
        else:
            return False
    if command == "remove":
        if x == 1 or x == 3 or x == 2:
            return True
        else:
            return False
    if command == "list":
        if x == 0 or x == 1 or x == 2:
            return True
        else:
            return False
    if command == "avg":
        if x == 3:
            return True
        else:
            return False
    if command == "min":
        if x == 3:
            return True
        else:
            return False
    if command == "top":
        if x == 1 or x == 2:
            return True
        else:
            return False
    if command == "undo":
        if x == 0:
            return True
        else:
            return False

def AddResultsToListCommand(resultsList, cmd):
    try:
        grade1 = (cmd[0])
        grade2 = (cmd[1])
        grade3 = (cmd[2])
        gradePosibilities = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
        if grade1 in gradePosibilities:
            if grade2 in gradePosibilities:
                if grade3 in gradePosibilities:
                    student = (int(cmd[0]), int(cmd[1]), int(cmd[2]))
                    AddResultsToList(resultsList, student)
                else:
                    print("Invalid grade.")
                    return
            else:
                print("Invalid grade.")
                return
        else:
            print("Invalid grade.")
            return
    except ValueError:
        print("The input is invalid, the results couldn't be added, try again.")
    
def InsertResultsInListCommand(resultsList, cmd):
    if cmd[3]!="at":
        print("Invalid syntax.")
        return
    try:
        grade1 = (cmd[0])
        grade2 = (cmd[1])
        grade3 = (cmd[2])
        position = int(cmd[4])
        if position > len(resultsList)-1 or position < 0:
            print("Invalid input.")
            return
        gradePosibilities = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
        if grade1 in gradePosibilities:
            if grade2 in gradePosibilities:
                if grade3 in gradePosibilities:
                    student = (int(cmd[0]), int(cmd[1]), int(cmd[2]))
                    InsertResultsInList(resultsList, student, position)
                else:
                    print("Invalid grade.")
                    return
            else:
                print("Invalid grade.")
                return
        else:
            print("Invalid grade.")
            return
    except ValueError:
        print("The input is invalid, the results couldn't be added, try again.")
        

def RemoveResultsFromListCommand(resultsList, cmd):
    try:
        position = int(cmd[0])
        if position < 0 or position > len(resultsList)-1 or len(cmd[0]) == 0:
            print("Invalid input, the results can't be added.")
            return
        RemoveAtPositionGiven(resultsList, position)
    except ValueError:
        print("Invalid input.")
        
def RemoveFromStartToEndCommand(resultsList, cmd):
    if cmd[1]!="to":
        print("Invalid syntax.")
        return
    try:
        start = int(cmd[0])
        end = int(cmd[2])
        if start < 0 or end < 0 or start > len(resultsList)-1 or end > len(resultsList)-1 or start > end:
            print("Invalid input, try again.")
            return
        RemoveFromStartToEnd(resultsList, start, end)
    except ValueError:
        print("Invalid input.")

def RemoveSignThanCommand(resultsList, cmd):
    if cmd[0] in [">", "<", "="]:
        try:
            avg = float(cmd[1])
            if cmd[0] == ">":
                RemoveGreaterThan(resultsList, avg)
            if cmd[0] == "<":
                RemoveLessThan(resultsList, avg)
            if cmd[0] == "=":
                RemoveEqualTo(resultsList, avg)
        except ValueError:
            print("Invalid parameters. ")
    else:
        print("Invalid syntax.")
        return

def RemoveCommand(resultsList, cmd):
    if len(cmd)==1:
        RemoveResultsFromListCommand(resultsList, cmd)
    elif len(cmd)==2:
        RemoveSignThanCommand(resultsList, cmd)
    else:
        RemoveFromStartToEndCommand(resultsList, cmd)

def ReplaceDatesAtPositionGivenCommand(resultsList, cmd):
    if cmd[2]!="with":
        print("Invalid command.")
        return
    if len(resultsList) == 0:
        print("There are no entries.")
        return
    try:
        position = int(cmd[0])
        problemIndex = cmd[1]
        newGrade = int(cmd[3])
        validIndexes = ["P1", "P2", "P3"]
        if position < 0 or position > len(resultsList)-1 or newGrade < 0 or newGrade > 10 or problemIndex not in validIndexes:
            print("Invalid input, try again.")
            return
        if problemIndex == "P1":
            index = 1
        elif problemIndex == "P2":
            index = 2
        else:
            index = 3
        ReplaceDatesAtPositionGiven(position, resultsList, index, newGrade)
    except ValueError:
        print("Invalid input.")

def listCommandOP(resultsList):
    if len(resultsList)==0:
        print("There are no entries.")
        return
    print(ListGrades(resultsList))

from copy import* 

def listSortedCommand(resultsList, cmd):
    if cmd[0] != "sorted":
        print("Invalid syntax.")
        return
    if len(resultsList) == 0:
        print("There are no entries, the list is empty.")
        return
    listt=sorte(resultsList)
    print(ListGrades(listt)) 

def listOptionThanCommand(resultsList, cmd):
    signs = ["<", "=", ">"]
    try:
        score = int(cmd[1])
        if cmd[0] in signs:
            if cmd[0] == "<":
                print(ListGrades(LessThan(resultsList, score)))
            elif cmd[0] == "=":
                print(ListGrades(EqualTo(resultsList, score)))
            else:
                print(ListGrades(GreaterThan(resultsList, score)))
    except ValueError:
        print("Invalid input.")
        return

def listCommand(gradesList, cmd):
    if len(cmd) == 0:
        listCommandOP(gradesList)
    if len(cmd) == 1:
        listSortedCommand(gradesList, cmd)
    if len(cmd) == 2:
        listOptionThanCommand(gradesList, cmd)

def AverageOfAveragesBetweenPositionsCommand(resultsList, cmd):
    if cmd[1]!="to":
        print("Invalid syntax.")
        return
    try:   
        pos1 = int(cmd[0])
        pos2 = int(cmd[2])
        if pos1 < 0 or pos1 > len(resultsList)-1 or pos2 < 0 or pos2 > len(resultsList)-1 or pos1 > pos2:
            print("Invalid positions, try again.")
            return
        print(AverageOfAveragesBetweenPositions(resultsList, pos1, pos2))
    except ValueError:
        print("Invalid input.")

def MinOfAveragesBetweenPositionsCommand(resultsList, cmd):
    if cmd[1]!="to":
        print("Invalid syntax.")
        return
    try:
        pos1 = int(cmd[0])
        pos2 = int(cmd[2])
        if pos1 < 0 or pos2 < 0 or pos1 > len(resultsList)-1 or pos2 > len(resultsList)-1 or pos1 > pos2:
            print("Invalid indexes, try again.")
            return
        print(MinOfAveragesBetweenPositions(resultsList, pos1, pos2))
    except ValueError:
        print("Invalid input.")

def TopNProblemCommand(resultsList, cmd):
    if cmd[1] in ["P1", "P2", "P3"]:
        try:
            n = int(cmd[0])
            if n < 0 or n > len(resultsList):
                print("Invalid number for top grades.")
                return
            if cmd[1] == "P1":
                index = 0
            if cmd[1] == "P2":
                index = 1
            if cmd[1] == "P3":
                index = 2
            print(TopNGradeIndexed(resultsList, index, n))
        except ValueError:
            print("Invalid input parameters.")
    else:
        print("Invalid syntax.")
        return

def TopNStudentsCommand(resultsList, cmd):
    try:
        n = int(cmd[0])
        resultsList2 = deepcopy(resultsList)
        return ReturnTopNStudents(resultsList2, n)
    except ValueError:
        print("Invalid input.")
    
def TopCommand(resultsList, cmd):
    if len(cmd)==1:
        resultsList2 = deepcopy(resultsList)
        print(ListGrades(TopNStudentsCommand(resultsList2, cmd)))
    if len(cmd)==2:
        resultsList2 = deepcopy(resultsList)
        TopNProblemCommand(resultsList2, cmd)

def UndoCommand(resultsList, undoList, nrOfUndoes):
    if nrOfUndoes <= 0:
        print("There is no operation to be undone.")
        return
    return undo(gradesList, undoList, nrOfUndoes)

def readCommand():
    """
The function returns the command and the list of parameters

    """
    cmd = input("Command: ")
    if cmd.find(" ") == -1:
        command = cmd
        parameters = ""
    else:
        command = cmd[0:cmd.find(" ")]
        parameters = cmd[cmd.find(" ")+1:]
        parameters = parameters.split(" ")
    return (command, parameters)

