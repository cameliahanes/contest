'''
Created on 31 oct. 2016

@author: Camelia
'''
def Menu():
    string = "\n"
    string += "Valid commands: \n"
    string += "add <P1 score> <P2 score> <P3 score> \n"
    string += "insert <P1 score> <P2 score> <P3 score> at <position> \n"
    string += "remove <position> \n"
    string += "remove <start position> to <end position> \n"
    string += "remove [< | = | > ] <score> \n"
    string += "replace <position> P1/P2/P3 with <new score> \n"
    string += "list \n"
    string += "list sorted \n"
    string += "avg <position1> to <positon2> \n"
    string += "min <position1> to <position2> \n"
    string += "top <number> \n"
    string += "top <number> <P1|P2|P3> \n"
    string += "help \n"
    string += "exit \n"
    print(string)

from allCommands import*
from copy import deepcopy
from Tests import*

def start():
    gradesList = []
    undoList=[]
    TestInit(gradesList)
    nrOfUndoes = -1

    gradesList2 = deepcopy(gradesList)
    undoList = undoList+[gradesList2][:]
    nrOfUndoes = int(nrOfUndoes)+1
                    
    undoneCommands = ["add", "insert", "replace", "remove"]
    commandList = {"add":AddResultsToListCommand, "top":TopCommand, "min":MinOfAveragesBetweenPositionsCommand, "avg":AverageOfAveragesBetweenPositionsCommand, "list":listCommand, "insert":InsertResultsInListCommand, "replace":ReplaceDatesAtPositionGivenCommand, "remove":RemoveCommand}
    while True:
        command, parameters = readCommand()
        if command == "help":
            Menu()
        elif command == "undo" and parameters == "":
            if nrOfUndoes < 0:
                print("There's no operation to be undone.")
            else:
                gradesList, undoList, nrOfUndoes = undo(gradesList, undoList, nrOfUndoes)
        elif command == "exit":
            break  
        elif command in commandList:
            if ValidParameters(command, parameters)==True:
                commandList[command](gradesList, parameters)
                if command in undoneCommands:
                    gradesList2 = deepcopy(gradesList)
                    undoList = undoList+[gradesList2][:]
                    nrOfUndoes = int(nrOfUndoes)+1
        else:
            print("Invalid command.")
