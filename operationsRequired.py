'''
Created on 31 oct. 2016

@author: Camelia
'''
'''
During a programming contest for students, each contestant had to solve 3 problems (named P1, P2
and P3). Afterwards, an evaluation committee graded the solution to each of the problems solved by
the contestants using integers between 0 and 10. The committee needs a program that will allow
managing the list of scores and establishing the winners. 

'''

def AddResultsToList(l, results):
    '''
    the function returns true if the value given was added and False instead
   Input: l-the list and results-the triplet of results for each problem
   Output: -

    '''
    l.append(results)
    return True


def InsertResultsInList(l, results, p):
    '''
    The function inserts the results given through parameter results into the list l at position p
    Input: the list, the position and the results
    Output: -
    '''
    l.append(results)
    pos = len(l)-1
    while pos > p:
        l[pos], l[pos-1] = l[pos-1], l[pos]
        pos = pos -1

def RemoveLessThan(resultsList, avg):
    for i in range (len(resultsList)):
        if float(AveragePerStudent(resultsList[i])) < avg:
            RemoveAtPositionGiven(resultsList, i)

def RemoveGreaterThan(resultsList, avg):
    for i in range (len(resultsList)):
        if float(AveragePerStudent(resultsList[i])) > avg:
            RemoveAtPositionGiven(resultsList, i)

def RemoveEqualTo(resultsList, avg):
    for i in range (len(resultsList)):
        if float(AveragePerStudent(resultsList[i])) == avg:
            RemoveAtPositionGiven(resultsList, i)

def RemoveAtPositionGiven(l, p):
    '''
    This function sets the results from the problems at position p to 0
    Input: the list l of results and p, the position at which we make settings
    Output:-
    '''
    l[p] = (0, 0, 0)
    return

def RemoveFromStartToEnd(l, start, end):
    '''
    This function sets the results of participants from start to end positions given to
    0 value
    Input: the start and end positions and the list of results
    Output:-
    '''
    for i in range(start, end+1):
        l[i] = (0, 0, 0)


def ReplaceDatesAtPositionGiven(p, l, problemIndex, grade):
    '''
    This function replaces the result obtained for a problem with the grade given as parameter
    Input: p - the position in the list of the student which will have the grades modified
           l - the list with grades
           problemIndex - the index of the one of the three problems the student has solved
           grade - the grade which will be set for the problem with index above given
    '''
    (x, y, z) = l[p]
    if problemIndex == 1:
        (x, y, z) = (grade, y, z)
    else:
        if problemIndex == 2:
            (x, y, z) = (x, grade, z)
        else:
            (x, y, z) = (x, y, grade)
    l[p] = (x, y, z)
    return
    
def ListGrades(gradesList):
    '''
    The function returns the list of students ;
    '''
    res = ""
    for i in gradesList:
        res += str(i)
        res += "\n"
    return res

def sortList(gradesList, arr):
    """
    This function returns the sorted list of students
    The sorting process consists of creating an array which holds the
    average of each student and ten the function sorts both the list
    and the array, having in account the average for each student
    
    """
    for i in range (0, len(arr)-1):
        for j in range(i+1, len(arr)):
            if float(arr[i]) < float(arr[j]):
                arr[i], arr[j] = arr[j], arr[i]
                gradesList[i], gradesList[j] = gradesList[j], gradesList[i]
    return gradesList


def LessThan(gradesList, avg):
    '''
The function returns the students with the average of their grades less than a given value

    '''
    res = []
    for i in range(0, len(gradesList)):
        average = AveragePerStudent(gradesList[i])
        if average < avg:
            res.append(gradesList[i])
    return res

def GreaterThan(gradesList, avg):
    '''
The function returns the students with the average of their grades greater than a given value

    '''
    res = []
    for i in range(0, len(gradesList)):
        average = AveragePerStudent(gradesList[i])
        if average > avg:
            res.append(gradesList[i])
    return res

def EqualTo(gradesList, avg):
    '''
The function returns the students with the average of their grades equal to a given value

    '''
    res = []
    for i in range(0, len(gradesList)):
        average = AveragePerStudent(gradesList[i])
        if average == avg:
            res.append(gradesList[i])
    return res

def AveragePerStudent(student):
    finalAverage = 0.0
    (a, b, c) = student
    finalAverage += float(float(a)+float(b)+float(c))/3
    return finalAverage

def CreateArrayOfAverages(resultsList):
    arr = []
    for i in range(len(resultsList)):
        (a, b, c) = (resultsList[i])
        arr.append(float((int(a)+int(b)+int(c))/3))
    return arr

from copy import deepcopy

def sorte (resultsList):
    arr = CreateArrayOfAverages(resultsList)
    listt = deepcopy(resultsList)
    listt = sortList(listt, arr)
    return listt

def AverageOfAveragesBetweenPositions(gradesList, pos1, pos2):
    '''
    This function returns the average of the averages the participants have
    '''
    finalAverage = 0.0
    for i in range(pos1, pos2+1):
        finalAverage += AveragePerStudent(gradesList[i])
    return finalAverage/(pos2-pos1+1)

def MinOfAveragesBetweenPositions(gradesList, pos1, pos2):
    '''
    The function returns the minimum of the averages in a list of results
    given as parameter
    '''
    minAvg = AveragePerStudent(gradesList[pos1])
    for i in range(pos1+1, pos2+1):
        if AveragePerStudent(gradesList[i]) < minAvg:
            minAvg = AveragePerStudent(gradesList[i])
    return minAvg

def sortStudentsByAverage(gradesList):
    '''
sorts the list of top n students with the gratest averages
    '''
    arr = []
    for i in range (len(gradesList)):
        arr.append(AveragePerStudent(gradesList[i]))
    sortList(gradesList, arr)

def ReturnTopNStudents(gradesList, n):
    '''
returns the list of n first students
'''
    finalList1 = deepcopy(gradesList)
    finalList1 = sorte(finalList1)
    finalList = []
    for i in range(n):
        finalList.append(finalList1[i])
    return finalList
    
def TopNGradeIndexed(gradesList, index, n):
    '''
returns the list of students who have obtained the greatest grades at a certain problem

    '''
    aux = gradesList
    arr = []
    for i in range (len(aux)):
        arr.append(aux[i][index])
    sortList(aux, arr)
    flist = ""
    for j in range (n):
        flist += str(gradesList[j])
        flist += "\n"
    return flist

def backup(gradesList, undoList, nrOfUndoes):
    gradesList2 = deepcopy(gradesList)
    undoList = undoList+[gradesList2][:]
    nrOfUndoes = int(nrOfUndoes)+1
    return gradesList2, undoList, nrOfUndoes

def undo(gradesList, undoList, nrOfUndoes):
    '''
    this function undoes the last operation
    input:
    the list of grades, the list of all modifications and the number of current
    modification
    output: gradesList' - the list of all results after undoing
    undoList' - the new list of undoed operations    
    nrOfUndoes'- the number
    '''
    nrOfUndoes -= 1
    gradesList2 = deepcopy(undoList[nrOfUndoes][:])
    undoList.pop()
    return gradesList2, undoList, nrOfUndoes
